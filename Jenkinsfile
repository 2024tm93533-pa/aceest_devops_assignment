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
      steps {
        sh '''
        echo "Checking workspace contents..."
        ls -la
        echo "Running tests inside Python Docker container..."

        docker run --rm \
          -v $WORKSPACE:/app \
          -w /app \
          python:3.11 \
          sh -c "
            echo 'Inside container:' &&
            ls -la &&
            python -m pip install --upgrade pip &&
            pip install -r requirements.txt &&
            pytest -q
          "
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
