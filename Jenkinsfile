pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stages {
    stage('Build & Test') {
      steps {
        sh '''
        apt-get update
        apt-get install -y python3 python3-pip python3-venv
        python3 -m venv venv
        . venv/bin/activate
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

    stage('Optional Push') {
      when {
        expression { return env.PUSH_TO_REGISTRY == "true" }
      }
      steps {
        withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
          sh 'docker tag aceest:jenkins $DOCKER_USER/aceest:latest'
          sh 'docker push $DOCKER_USER/aceest:latest'
        }
      }
    }
  }
}
