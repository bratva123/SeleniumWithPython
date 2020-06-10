pipeline {
    agent any

    stages {
        
        stage('CheckoutModule1') {
        steps {
            sh 'mkdir -p Module1'
            dir("Module1")
            {
                git branch: "master",
                url: 'https://github.com/bratva123/SeleniumWithPython.git'
            }
        }
    }
        stage('Build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
                sh 'pip install pytest'
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
