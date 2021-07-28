pipeline {
    agent any
    options([pipelineTriggers([cron('H/1* * *')])])
    stages {
        stage('build') { 
            steps {
                echo 'Build Stage Success' 
            }
        }
        stage('test') { 
            steps {
                echo 'Test Stage Success' 
            }
        }
        stage('deploy') { 
            steps {
                echo 'Deploy Stage Success' 
            }
        }
    }
}
