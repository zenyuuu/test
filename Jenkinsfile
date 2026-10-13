pipeline {
    agent any

    environment {
        IMAGE_NAME = 'aldik15/test'
        REGISTRY_CREDENTIALS = 'dckr_pat_9k3PfZHZG5oHDG7v_tVjXM8CArw'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'echo Build di Windows'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME%:%BUILD_NUMBER% .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: REGISTRY_CREDENTIALS,
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    bat 'echo %DOCKER_PASS% | docker login -u "%DOCKER_USER%" --password-stdin'

                    bat 'docker push %IMAGE_NAME%:%BUILD_NUMBER%'

                    bat 'docker tag %IMAGE_NAME%:%BUILD_NUMBER% %IMAGE_NAME%:latest'

                    bat 'docker push %IMAGE_NAME%:latest'
                }
            }
        }
    }
}
