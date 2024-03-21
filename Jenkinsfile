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
                bat 'docker build -t a1_image .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                bat 'docker login'
                bat 'docker tag a1_image wisalkhanmv/mlops_assignment:first_tag'
                bat 'docker push wisalkhanmv/mlops_assignment:first_tag'
            }
        }
    }
}