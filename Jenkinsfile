pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo "📥 Cloning repository..."
                git branch: 'main',
                    url: 'https://github.com/shiva-6300/coffe.git'
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                set -e

                cd webpage

                echo "🧹 Removing old venv..."
                rm -rf venv

                echo "🐍 Creating virtual environment..."
                python3 -m venv venv

                echo "⬆️ Upgrading pip..."
                venv/bin/pip install --upgrade pip

                echo "📦 Installing dependencies..."
                venv/bin/pip install flask gunicorn
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                set -e

                cd webpage

                echo "🛑 Stopping old process..."
                pkill -f "gunicorn.*car:app" || true

                echo "🚀 Starting Flask app with Gunicorn (public access)..."
                nohup venv/bin/gunicorn \
                    --workers 3 \
                    --bind 0.0.0.0:8000 \
                    --access-logfile access.log \
                    --error-logfile error.log \
                    car:app > app.log 2>&1 &

                echo "✅ App running on port 8000"
                '''
            }
        }
    }

    post {
        success {
            echo "🎉 DEPLOYED SUCCESSFULLY"
            echo "👉 Open: http://<EC2-PUBLIC-IP>:8000"
        }

        failure {
            echo "❌ DEPLOYMENT FAILED"
        }

        always {
            echo "🔁 PIPELINE FINISHED"
        }
    }
}
