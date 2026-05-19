pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
        PYTHON   = "C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
    }

    stages {

        stage('Checkout') {
            steps {
                echo '🔵 Checkout code...'
                checkout scm
                echo '✅ Done'
            }
        }

        stage('Build') {
            steps {
                echo '🔵 Creating virtual environment...'

                bat """
                    "%PYTHON%" -m venv %VENV_DIR%
                    %VENV_DIR%\\Scripts\\python.exe -m pip install --upgrade pip
                    %VENV_DIR%\\Scripts\\python.exe -m pip install -r requirements.txt
                """

                echo '✅ Build completed'
            }
        }

        stage('Test') {
            steps {
                echo '🔵 Running tests...'

                bat """
                    %VENV_DIR%\\Scripts\\python.exe -m pytest test_app.py -v
                """

                echo '✅ Tests passed'
            }
        }

        stage('Deploy') {
            steps {
                echo '🔵 Deploying app...'

                bat """
                    start "flask-app" /B %VENV_DIR%\\Scripts\\python.exe app.py > app.log 2>&1
                """

                echo '🚀 App running on http://localhost:5000'
            }
        }
    }

    post {
        success {
            echo '🎉 Pipeline SUCCESS'
        }

        failure {
            echo '❌ Pipeline FAILED'
        }
    }
}