pipeline {
    agent any
    
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
    triggers { cron('H/1 * * * *')    }
}
