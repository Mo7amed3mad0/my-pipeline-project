pipeline {
    agent any

    environment {
        DEPLOY_DIR = "C:\\DeployedApp\\myapp"
        VENV_DIR   = "venv"
    }

    stages {

        // ──────────────────────────────────────
        // STAGE 1 : CHECKOUT
        // ──────────────────────────────────────
        stage('Checkout') {
            steps {
                echo '🔵 Checking out source code from GitHub...'
                checkout scm
                echo '✅ Checkout done.'
            }
        }

        // ──────────────────────────────────────
        // STAGE 2 : BUILD
        // ──────────────────────────────────────
        stage('Build') {
            steps {
                echo '🔵 Setting up Python virtual environment...'
                bat '''
                    python -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate.bat
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
                echo '✅ Build done.'
            }
        }

        // ──────────────────────────────────────
        // STAGE 3 : TEST
        // ──────────────────────────────────────
        stage('Test') {
            steps {
                echo '🔵 Running pytest...'
                bat '''
                    call %VENV_DIR%\\Scripts\\activate.bat
                    pytest test_app.py -v
                '''
                echo '✅ All tests passed.'
            }
        }

        // ──────────────────────────────────────
        // STAGE 4 : DEPLOY
        // ──────────────────────────────────────
        stage('Deploy') {
            steps {
                echo '🔵 Deploying application...'
                bat '''
                    if not exist %DEPLOY_DIR% mkdir %DEPLOY_DIR%
                    xcopy /E /Y /I . %DEPLOY_DIR%
                    echo Deployed successfully > %DEPLOY_DIR%\\deploy.log
                '''
                echo '✅ Deployment complete!'
            }
        }
    }

    post {
        success {
            echo '🎉 Pipeline finished SUCCESSFULLY!'
        }
        failure {
            echo '❌ Pipeline FAILED — check the logs above.'
        }
        always {
            cleanWs()
        }
    }
}
