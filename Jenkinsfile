pipeline {
  agent any

  stages {

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build & Test') {
      steps {
        sh '''
        echo "Running tests inside Python Docker container..."

        docker run --rm \
          -v $(pwd):/app \
          -w /app \
          python:3.11 \
          sh -c "
            pip install --upgrade pip &&
            pip install -r requirements.txt &&
            pytest -q
          "
        '''
      }
    }

    stage('Build Docker') {
      steps {
        sh 'docker build -t aceest:jenkins .'
      }
    }

  }
}
