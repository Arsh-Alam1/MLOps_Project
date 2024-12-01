pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "ml-model"
        CONTAINER_NAME = "ml-model-container"
    }

    stages {
        // Clone the Git Repository
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Arsh-Alam1/MLOps_Project.git'
            }
        }

        // Build the Docker Image
        stage('Build Docker Image') {
            steps {
                // Ensure the Dockerfile and app.py are in the correct directory
                sh 'docker build -t $DOCKER_IMAGE ./src'  // Adjust path if needed
            }
        }

        // Deploy using Terraform
        stage('Deploy with Terraform') {
            steps {
                sh '''
                cd terraform
                terraform init
                terraform apply -auto-approve
                '''
            }
        }

        // Test the Deployment
        stage('Test Deployment') {
            steps {
                // Adding a sleep to allow container startup
                sh '''
                sleep 10  # Wait for the container to start
                curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"features": [2]}'
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Pipeline failed. Check the logs.'
        }
    }
}
