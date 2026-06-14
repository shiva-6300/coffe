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

                # create venv only if not exists
                if [ ! -d "venv" ]; then
                    python3 -m venv venv
                fi

                # install flask (fast + safe)
                venv/bin/pip install flask

                # stop previous running app
                pkill -f "car.py" || true

                # start new app
                nohup venv/bin/python car.py > app.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo "✅ SUCCESS: Flask app deployed on EC2 (MAIN branch)"
        }

        failure {
            echo "❌ FAILED: Check Jenkins console logs"
        }

        always {
            echo "🔁 PIPELINE FINISHED"
        }
    }
}
