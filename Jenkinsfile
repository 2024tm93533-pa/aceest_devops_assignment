pipeline {
  agent any

  environment {
    IMAGE_NAME = "aceest:jenkins"
    DOCKER_PATH = "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    KUBECONFIG = "$HOME/.kube/config"
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

    stage('Build Docker Image (Minikube)') {
      steps {
        sh '''
        echo "Setting Docker to Minikube environment..."

        export PATH=$DOCKER_PATH:$PATH
        eval $(minikube docker-env)

        echo "Building Docker image inside Minikube..."
        docker build -t $IMAGE_NAME .
        '''
      }
    }

    stage('Verify Docker Image') {
      steps {
        sh '''
        export PATH=$DOCKER_PATH:$PATH
        eval $(minikube docker-env)

        echo "Listing Docker images..."
        docker images | grep aceest || true
        '''
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        sh '''
        echo "Deploying to Kubernetes..."

        kubectl apply -f k8s/deployment.yaml
        kubectl apply -f k8s/service.yaml

        echo "Restarting deployment..."
        kubectl rollout restart deployment aceest-deployment

        echo "Waiting for rollout..."
        kubectl rollout status deployment aceest-deployment
        '''
      }
    }

  }

  post {
    always {
      echo "Pipeline execution completed."
    }
    success {
      echo "CI/CD pipeline executed successfully 🚀"
    }
    failure {
      echo "Pipeline failed. Check logs above."
    }
  }
}