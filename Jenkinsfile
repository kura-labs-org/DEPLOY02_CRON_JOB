t = Calendar.instance
t.timeZone = TimeZone.getTimeZone("EST")
if (t == 'Wed July 28 19:40:00 EST 2021'){
     sh '''#!/bin/bash
          sudo shutdown now -h
     '''
}
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
            }
        }
        }
        }
