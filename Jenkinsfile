pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/wisalkhanmv/mlops_assignment'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t a1_image .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh "echo 'done'"
            }
        }
    }
}