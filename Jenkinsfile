
pipeline {
    agent { docker { image 'python:3.5.1' } }
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
