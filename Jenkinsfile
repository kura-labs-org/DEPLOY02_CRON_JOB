t = Calendar.instance
t.timeZone = TimeZone.getTimeZone("EST")
pipeline {
    agent any
    stages {
        stage('Check') {
            steps {
                if (t == 'Wed July 28 20:20:00 EST 2021'){
                    sudo shutdown now -h
                    }
            }
        }
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
   
