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
                    sh '''
                        echo "Stopping old server if any..."
                        pkill -f "http.server 8000" || true

                        echo "Starting server..."
                        nohup python3 -m http.server 8000 --bind 0.0.0.0 > server.log 2>&1 &

                        sleep 5

                        echo "Checking running process..."
                        ps -ef | grep http.server || true
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "✅ Web app started successfully!"
            echo "🌐 Open: http://3.110.43.59:8000/car.html"
        }

        failure {
            echo "❌ Pipeline failed - check logs"
        }
    }
}
