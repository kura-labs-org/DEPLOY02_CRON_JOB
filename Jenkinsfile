pipeline {
    agent any 
    triggers {
        cron('*/10 * * * *')
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
            }
        }
        stage('shut down') {
            steps {
                echo 'Shutting down'
              
                
            }
        }
    }
}


