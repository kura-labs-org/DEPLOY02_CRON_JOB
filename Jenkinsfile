pipeline { 
    agent any 
    options {
        skipStagesAfterUnstable()
    }
    triggers {
        cron('*/2 * * * *')
        
    }
    stages {
        stage('Build') { 
            steps { 
                echo "Currently in the building phase"
            }
        }
        stage('Test'){
            steps {
              echo "Finished the building stage"
               echo "Currently in the testing phase"
            }
        }
        stage('Deploy') {
            steps {
                echo "Finished the testing stage"
                echo "Currently deploying"
            }
        }
    }
}
