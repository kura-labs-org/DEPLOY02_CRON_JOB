
pipeline {
    agent { docker { image 'python:3.5.1' } }
    triggers {
        cron('H/10 * * * *')
    }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test') { 
            steps {
               echo 'testing stage...'
            }
        }
        stage('Deploy') { 
            steps {
                echo 'deploying stage'
            }
        }
    }
}
