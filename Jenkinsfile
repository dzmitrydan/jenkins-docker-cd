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
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Build') {
            steps {
                sh 'python ./start.py'
            }
        }
        stage('Docker build') {
            agent any
            steps {
                script {
                    sh 'docker build -t flask-app .'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh 'run -it --rm --name running-flask-app flask-app'
                }
            }
        }
    }
}