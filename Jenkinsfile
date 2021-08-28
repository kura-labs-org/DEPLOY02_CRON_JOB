CRON_MIN=''' * * * * * '''
pipeline{
  agent any
  triggers{
        cron(CRON_MIN)
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
