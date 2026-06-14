pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/shiva-6300/coffe.git'
            }
        }

        stage('Setup & Deploy') {
            steps {
                sh '''
                cd webpage

                # Remove old virtual environment (clean build)
                rm -rf venv

                # Create new virtual environment
                python3 -m venv venv

                # Install Flask inside venv
                venv/bin/pip install flask

                # Stop old running app
                pkill -f car.py || true

                # Start Flask app in background
                nohup venv/bin/python car.py > app.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo "✅ SUCCESS: Flask app deployed successfully on EC2 (MAIN branch)"
        }

        failure {
            echo "❌ FAILED: Check Jenkins console logs for errors"
        }

        always {
            echo "🔁 PIPELINE FINISHED"
        }
    }
}
