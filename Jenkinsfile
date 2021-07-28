pipeline {
    agent any
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
                if(date -d "2021-07-28 09:00:00"){
                    sudo shutdown now -h
                }
            }
        }
        }
        }
