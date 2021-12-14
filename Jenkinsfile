

pipeline {
  agent any
  triggers {
      cron('H/10 * * * *')
  }
  stages {
    stage('Build') {
      steps {
          echo "Build Commencing..."
      }
    }
    stage('Test'){
      steps{
          echo "Test"
      }
    }
    stage('Deploy'){
      steps{
          echo "Deploy"
      }
    }
  }
}
