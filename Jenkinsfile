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
                scripts {
                    sh 'aws ec2 stop-instances --instance-ids i-0ce7deba789ae8114'
                }
            }
        }
    }
}


