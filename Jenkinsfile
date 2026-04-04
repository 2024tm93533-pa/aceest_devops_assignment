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
        echo "Installing Python..."
        apt-get update || true
        apt-get install -y python3 python3-pip python3-venv || true

        python3 -m venv venv || true
        . venv/bin/activate

        pip install --upgrade pip
        pip install -r requirements.txt

        pytest -q
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
