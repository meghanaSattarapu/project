pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                echo "Installing Python dependencies"
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo "Running Selenium tests using pytest"
                // Start Flask app
                bat 'start /B python app.py'
                // Wait for server to start
                bat 'ping 127.0.0.1 -n 5 > nul'
                // Run tests
                bat 'pytest -v tests\\test_bookmyshow_ui.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image"
                bat "docker build -t bookmyshow:v1 ."
            }
        }

        stage('Docker Login') {
            steps {
                echo "Login to DockerHub"
                bat 'docker login -u smeghana55 -p Megh@3551'
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "Pushing Docker image to DockerHub"
                bat "docker tag bookmyshow:v1 smeghana55/bookmyshow:v1"
                bat "docker push smeghana55/bookmyshow:v1"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes"
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs.'
        }
    }
}
