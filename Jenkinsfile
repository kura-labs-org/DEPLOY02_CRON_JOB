pipeline {
    agent any
    triggers {
        cron('10 * * * *')
    }
    stages {
        stage('build') { 
            steps {
                echo 'Build Stage Success' 
            }
        }
        stage('test') { 
            steps {
                'Test Stage Success' 
            }
        }
        stage('deploy') { 
            steps {
                'Deploy Stage Success' 
            }
        }
    }
}
