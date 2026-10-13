pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    environment {
        IMAGE_NAME           = 'aldik15/test'
        REGISTRY_CREDENTIALS = 'dockerhub-credentials'
    }

    stages {
        // Checkout SCM sudah otomatis dijalankan Jenkins (Declarative: Checkout SCM),
        // jadi tidak perlu stage Checkout manual lagi.

        stage('Build') {
            steps {
                bat 'echo Build di Windows'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '''
                    docker build -t %IMAGE_NAME%:%BUILD_NUMBER% .
                    if errorlevel 1 exit /b 1

                    docker tag %IMAGE_NAME%:%BUILD_NUMBER% %IMAGE_NAME%:latest
                    if errorlevel 1 exit /b 1
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: "${REGISTRY_CREDENTIALS}",
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    bat '''
                        @echo off

                        rem Login. Jangan pakai: echo %DOCKER_PASS% | docker login ...
                        rem karena echo menambah spasi/newline ke password.
                        docker login -u "%DOCKER_USER%" -p "%DOCKER_PASS%"
                        if errorlevel 1 exit /b 1

                        docker push %IMAGE_NAME%:%BUILD_NUMBER%
                        if errorlevel 1 exit /b 1

                        docker push %IMAGE_NAME%:latest
                        if errorlevel 1 exit /b 1
                    '''
                }
            }
        }
    }

    post {
        always {
            // Hapus sesi login Docker dari server Jenkins
            bat 'docker logout || exit /b 0'
        }
        success {
            echo "Berhasil push ${IMAGE_NAME}:${BUILD_NUMBER} dan ${IMAGE_NAME}:latest"
        }
        failure {
            echo 'Pipeline gagal. Cek log stage yang merah.'
        }
    }
}
