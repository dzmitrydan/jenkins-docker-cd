if ( IMAGE_TAG == null ) {
    IMAGE_TAG = "1.0"
}
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
                    sh 'docker build -t flask-app-main:v${IMAGE_TAG} .'
                }
            }
        }
        stage('Deploy') {
            agent any
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 --rm --name running-flask-app-main flask-app-main:v${IMAGE_TAG}'
                }
            }
        }
    }
}