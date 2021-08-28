pipeline{
  agent any
  triggers {
        cron('H/10 * * * *')
  }  
  stages{
    stage('Build'){
      steps{
        echo "Build was successful"
      }
    }
    stage('Test'){
      steps{
      echo "Testing was successful"
      }
    }
    stage('Deployment'){
      steps{
      echo "Deployment was successful"
      }
    }
  }
}
