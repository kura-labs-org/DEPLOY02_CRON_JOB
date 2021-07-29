t = Calendar.instance
t.timeZone = TimeZone.getTimeZone("EST")
pipeline {
    agent any
    stages {
        stage('Check') {
            if (t == 'Wed July 28 20:10:00 EST 2021'){
            sh '''#!/bin/bash
            sudo shutdown now -h
            '''
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
        }
