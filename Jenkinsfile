pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/shiva-6300/coffe.git'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                cd webpage

                # create virtual environment
                python3 -m venv venv

                # install dependencies using venv (no source needed)
                venv/bin/pip install flask

                # stop old running app (if any)
                pkill -f car.py || true

                # start new app in background
                nohup venv/bin/python car.py > app.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo "✅ SUCCESS: Flask app deployed from MAIN branch on EC2"
        }

        failure {
            echo "❌ FAILED: Deployment error - check Jenkins console logs"
        }

        always {
            echo "🔁 PIPELINE COMPLETED"
        }
    }
}
