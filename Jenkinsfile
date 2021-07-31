CRON_Exampl=''' */10 0-21 * * * ''' 
pipeline {
    agent any
    triggers{
        cron(CRON_Exampl)
    }
    stages {
        stage('Build') {
            steps {
                echo 'Hello'
            }
        }
        stage('Test') {
            steps{
                echo 'Hello'
            }
        }
        stage('Deployment'){
            steps{
                echo 'Hello'
            }
        }
        }
        }
   
