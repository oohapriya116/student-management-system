
import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Student Management System" in response.data


def test_add_student(client):
    response = client.post(
        "/add",
        data={
            "name": "Ravi",
            "roll": "24CS101",
            "course": "CSE"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Ravi" in response.data
    assert b"24CS101" in response.data


def test_duplicate_roll_number(client):
    data = {
        "name": "Ravi",
        "roll": "24CS101",
        "course": "CSE"
    }

    client.post("/add", data=data)

    response = client.post(
        "/add",
        data={
            "name": "Priya",
            "roll": "24CS101",
            "course": "IT"
        },
        follow_redirects=True
    )

    assert b"Roll number already exists." in response.data
    assert b"Priya" not in response.data


def test_empty_fields(client):
    response = client.post(
        "/add",
        data={"name": "", "roll": "", "course": ""},
        follow_redirects=True
    )

    assert b"Please fill in all fields." in response.data
