CRON_example= ''' */10 0-21 * * * '''
pipeline {
    agent any
    triggers{
        cron('*/10 * * * *')
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
   
