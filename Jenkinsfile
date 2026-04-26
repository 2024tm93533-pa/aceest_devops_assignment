pipeline {
  agent any

  environment {
    IMAGE_NAME = "aceest:jenkins"
    DOCKER_PATH = "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
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
        echo "Setting up virtual environment..."

        python3 -m venv venv
        . venv/bin/activate

        pip install --upgrade pip
        pip install -r requirements.txt

        echo "Fixing Python path..."
        export PYTHONPATH=$(pwd)

        echo "Running tests..."
        pytest -v
        '''
      }
    }

    stage('Build Docker Image') {
      steps {
        sh '''
        echo "Fixing PATH for Docker..."
        export PATH=$DOCKER_PATH:$PATH

        echo "Checking Docker..."
        docker --version

        echo "Building Docker image..."
        docker build -t $IMAGE_NAME .
        '''
      }
    }

    stage('Verify Docker Image') {
      steps {
        sh '''
        export PATH=$DOCKER_PATH:$PATH

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