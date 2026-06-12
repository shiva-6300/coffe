pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/shiva-6300/coffe.git'
            }
        }

        stage('Verify Files') {
            steps {
                sh 'ls -la'
                sh 'cd webpage && ls -la'
            }
        }

        stage('Run Python Script') {
            steps {
                dir('webpage') {
                    sh 'python3 car.py'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}