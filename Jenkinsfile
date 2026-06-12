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

        stage('Run Python Script') {
            steps {
                dir('webpage') {
                    sh 'python3 car.py'
                }
            }
        }

        stage('Run Web App') {
            steps {
                dir('webpage') {
                    sh '''
                        echo "Stopping old server..."
                        pkill -f "http.server 8000" || true

                        echo "Starting web server..."
                        nohup python3 -m http.server 8000 --bind 0.0.0.0 > server.log 2>&1 &

                        sleep 5

                        echo "Checking server..."
                        ps -ef | grep http.server || true
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline executed successfully!"
            echo "🌐 Open: http://3.110.43.59:8000/car.html"
        }

        failure {
            echo "❌ Pipeline failed. Check logs."
        }
    }
}
