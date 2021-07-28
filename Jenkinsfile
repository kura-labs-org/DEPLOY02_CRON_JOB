pipeline {
    agent any 
    triggers {
        cron('H/10 * * * *')
    }
    stages {
        stage('Build') { 
            steps {
                echo "Building for second deployment"
            }
        }
        stage('Test') { 
            steps {
                echo "Testing for second deployment"
            }
        }
        stage('Deploy') { 
            steps {
                echo "Deploying second deployment"
            }
        }
    }
}
