pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/shiva-6300/coffe.git'
            }
        }

        stage('Deploy on EC2') {
            steps {
                sh '''
                cd webpage

                rm -rf venv
                python3 -m venv venv

                venv/bin/pip install flask

                pkill -f car.py || true

                nohup venv/bin/python car.py > app.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo "✅ DEPLOYED SUCCESSFULLY ON EC2 (13.201.226.142)"
        }

        failure {
            echo "❌ DEPLOYMENT FAILED - CHECK LOGS"
        }

        always {
            echo "🔁 PIPELINE DONE"
        }
    }
}
