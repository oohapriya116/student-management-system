
from flask import Flask, render_template, request, redirect, url_for, flash


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "practice-secret-key"
    app.config["STUDENTS"] = []

    @app.route("/", methods=["GET"])
    def home():
        return render_template(
            "index.html",
            students=app.config["STUDENTS"]
        )

    @app.route("/add", methods=["POST"])
    def add_student():
        name = request.form.get("name", "").strip()
        roll = request.form.get("roll", "").strip()
        course = request.form.get("course", "").strip()

        if not name or not roll or not course:
            flash("Please fill in all fields.")
            return redirect(url_for("home"))

        students = app.config["STUDENTS"]

        if any(student["roll"] == roll for student in students):
            flash("Roll number already exists.")
            return redirect(url_for("home"))

        students.append({
            "name": name,
            "roll": roll,
            "course": course
        })

        flash("Student added successfully.")
        return redirect(url_for("home"))

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
