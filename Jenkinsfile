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
                sh 'ls -la webpage'
            }
        }

        stage('Run Web App') {
            steps {
                dir('webpage') {
                    sh 'nohup python3 -m http.server 8000 > server.log 2>&1 &'
                }
            }
        }
    }

    post {
        success {
            echo "Web app started successfully!"
            echo "Open: http://3.110.43.59:8000/car.html"
        }

        failure {
            echo "Pipeline failed!"
        }
    }
}
