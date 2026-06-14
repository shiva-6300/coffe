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
}
