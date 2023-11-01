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
                    sh 'docker build -t flask-app-dev .'
                }
            }
        }
        stage('Deploy') {
            agent any
            steps {
                script {
                    sh 'docker run -d -p 5001:5000 flask-app-dev'
                }
            }
        }
    }
}