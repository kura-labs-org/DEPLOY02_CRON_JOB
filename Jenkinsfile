CRON_JOB ='''  */10 * * * * ''' 
pipeline {
    agent any
    triggers{
        cron(CRON_JOB)
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
