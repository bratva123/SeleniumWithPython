pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
                sh 'pip install pytest'
                sh 'pip install PyVirtualDisplay'
                sh 'pip install selenium'
                
                sh 'python -m pytest tests/home/login_tests.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
            }
        }
    }
}
