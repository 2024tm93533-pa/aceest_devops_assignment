pipeline {
  agent {
    docker {
      image 'python:3.11'
      args '-u root'   // run as root to avoid permission issues
    }
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
        python -m venv venv
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
