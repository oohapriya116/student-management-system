
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'oohapriya1176/student-management-system'
    }

    stages {
        stage('Install and Test') {
            steps {
                bat 'python -m pip install -r requirements.txt'
                bat 'python -m pytest tests -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME%:v1 -t %IMAGE_NAME%:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKERHUB_USER',
                        passwordVariable: 'DOCKERHUB_PASS'
                    )
                ]) {
                    powershell '''
                        $env:DOCKERHUB_PASS |
                        docker login --username $env:DOCKERHUB_USER --password-stdin
                    '''

                    bat 'docker push %IMAGE_NAME%:v1'
                    bat 'docker push %IMAGE_NAME%:latest'
                }
            }
        }
    }
}
