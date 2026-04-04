pipeline {
  agent any

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
          args '-u root:root'
        }
      }
      steps {
        sh 'python -m pip install --upgrade pip'
        sh 'pip install -r requirements.txt'
        sh 'pytest -q'
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
