pipeline {
    agent none
    stages {
        stage('Install Environment') {
            agent {
                docker {
                    image 'python:3.8'
                }
            }
            steps {
                sh 'python --version'
            }
        }
        stage('Docker build') {
            agent any
            steps {
                script {
                    sh 'docker build -t flask-app-dev${IMAGE_TAG} .'
                }
            }
        }
        stage('Deploy') {
            agent any
            steps {
                script {
                    sh 'docker run -d -p 5001:5000 --rm --name running-flask-app-dev flask-app-dev${IMAGE_TAG}'
                }
            }
        }
    }
}