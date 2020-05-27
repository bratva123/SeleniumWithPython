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
                sh 'pip install selenium'
                sh 'pip install pytest-html'
                
                sh 'python -m pytest tests/home/login_tests.py --html=reports_and_log/report.html'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
            }
        }
    }
    
    post {
        always {
            emailext attachmentsPattern: '/workspace/SeleniumWithPythonJob/reports_and_log/report.html', body: 'Hi \n Sending reports of testing', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
        }
    }
}
