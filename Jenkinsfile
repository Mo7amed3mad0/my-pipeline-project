pipeline {
    agent any

    environment {
        DEPLOY_DIR = "/var/www/myapp"          // غيّرها لمسار الـ deploy عندك
        PYTHON    = "python3"
        VENV_DIR  = "venv"
    }

    stages {

        // ──────────────────────────────────────
        // STAGE 1 : CHECKOUT
        // ──────────────────────────────────────
        stage('Checkout') {
            steps {
                echo '🔵 Checking out source code from GitHub...'
                checkout scm          // بيجيب الكود من الـ repo اللي ربطته في Jenkins
                echo '✅ Checkout done.'
            }
        }

        // ──────────────────────────────────────
        // STAGE 2 : BUILD  (إنشاء بيئة Python)
        // ──────────────────────────────────────
        stage('Build') {
            steps {
                echo '🔵 Setting up Python virtual environment...'
                sh '''
                    ${PYTHON} -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
                echo '✅ Build done — dependencies installed.'
            }
        }

        // ──────────────────────────────────────
        // STAGE 3 : TEST
        // ──────────────────────────────────────
        stage('Test') {
            steps {
                echo '🔵 Running pytest...'
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pytest test_app.py -v --html=report.html --self-contained-html
                '''
                echo '✅ All tests passed.'
            }
            post {
                always {
                    // بينشر الـ HTML report جوه Jenkins
                    publishHTML(target: [
                        allowMissing         : false,
                        alwaysLinkToLastBuild: true,
                        keepAll              : true,
                        reportDir            : '.',
                        reportFiles          : 'report.html',
                        reportName           : 'Pytest Report'
                    ])
                }
            }
        }

        // ──────────────────────────────────────
        // STAGE 4 : DEPLOY
        // ──────────────────────────────────────
        stage('Deploy') {
            steps {
                echo '🔵 Deploying application...'
                sh '''
                    mkdir -p ${DEPLOY_DIR}
                    cp -r . ${DEPLOY_DIR}
                    echo "Deployed at: $(date)" > ${DEPLOY_DIR}/deploy.log
                '''
                echo '✅ Deployment complete!'
            }
        }
    }

    // ──────────────────────────────────────
    // POST  (بعد ما الـ pipeline يخلص)
    // ──────────────────────────────────────
    post {
        success {
            echo '🎉 Pipeline finished SUCCESSFULLY!'
        }
        failure {
            echo '❌ Pipeline FAILED — check the logs above.'
        }
        always {
            // تنظيف الـ workspace بعد كل run
            cleanWs()
        }
    }
}
