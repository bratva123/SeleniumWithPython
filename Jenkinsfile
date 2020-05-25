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
                sh 'pip install PyVirtualDisplay'
                sh 'pip install selenium'
                sh 'pip install pytest'
                sh 'pytest -m  tests/home/login_tests.py '
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
            }
        }
    }
}
