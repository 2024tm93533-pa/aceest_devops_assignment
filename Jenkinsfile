pipeline {
  agent any

  environment {
    IMAGE_NAME = "aceest:jenkins"
  }

  stages {

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build & Test') {
      agent {
        docker {
          image 'python:3.11'
        }
      }
      steps {
        sh '''
      echo "Running tests inside Docker agent..."

      ls -la

      python -m pip install --upgrade pip
      pip install -r requirements.txt
      pytest -q
      '''
      }
    }

    stage('Build Docker Image') {
      steps {
        sh '''
        echo "Building Docker image..."
        docker build -t $IMAGE_NAME .
        '''
      }
    }

    stage('Verify Docker Image') {
      steps {
        sh '''
        echo "Listing Docker images..."
        docker images | grep aceest || true
        '''
      }
    }

  }

  post {
    always {
      echo "Pipeline execution completed."
    }
    success {
      echo "Build & tests passed successfully!"
    }
    failure {
      echo "Pipeline failed. Check logs above."
    }
  }
}
