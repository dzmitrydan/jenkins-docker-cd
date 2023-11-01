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