
pipeline {
    agent { docker { image 'python:3.9.0' } }
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
