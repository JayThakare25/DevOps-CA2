pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from branch
                checkout scm
            }
        }
        stage('Setup Dependencies') {
            steps {
                bat '''
                    python -m venv venv
                    call .\\venv\\Scripts\\activate.bat
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run Selenium Tests') {
            steps {
                bat '''
                    call .\\venv\\Scripts\\activate.bat
                    pytest -v test_form.py
                '''
            }
        }
    }
}
