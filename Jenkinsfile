pipeline {
  agent any
  triggers {
      cron('H/10 * * * *')
  }
  stages {
    stage('Build') {
      steps {
          echo "Building....!"
      }
    }
    stage('Test'){
      steps{
          echo "Testing....!"
      }
    }
    stage('Deploy'){
      steps{
          echo "Deploying...!"
      }
    }
  }
}
