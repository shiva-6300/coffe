pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git url: 'https://github.com/shiva-6300/coffe.git'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                cd webpage

                python3 -m venv venv
                source venv/bin/activate

                pip install flask

                pkill -f car.py || true
                nohup python car.py > app.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo "✅ DEPLOYMENT SUCCESS: Flask app is running on EC2"
        }

        failure {
            echo "❌ DEPLOYMENT FAILED: Check logs in Jenkins console output"
        }

        always {
            echo "🔁 Pipeline execution completed"
        }
    }
}
