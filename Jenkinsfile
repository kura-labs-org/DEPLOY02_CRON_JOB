pipeline { 
    agent any 
    triggers {
        cron('*/10 * * * *')
        
    }
    stages {
        stage('Build') { 
            steps { 
                echo " in the building phase"
            }
        }
        stage('Test'){
            steps {
               echo " in the testing phase"
            }
        }
        stage('Deploy') {
            steps {
                echo " deploying"
            }
        }
    }
}
