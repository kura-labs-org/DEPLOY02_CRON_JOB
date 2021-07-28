pipeline {
    agent any 
    //triggers {
        //cron('*/10 * * * *')
   // }
    stages {
        stage('Build') { 
            steps {
                sh 'rm -rf deployment2'
                sh 'mkdir deployment2'
                sh 'cd deployment2'
                sh 'touch aboutme.txt'
                sh 'echo "My name is Brittney Jones and I am 24 years old." > aboutme.txt'
                //sh 'cat aboutme.txt'
                
            }
        }
        stage('Test') { 
            steps {
                sh 'cat aboutme.txt'
             //sh 'cd ..'
            //sh 'test -f aboutme.txt'
             //sh 'grep -c "name" aboutme.txt'
            // sh 'grep -c "years" aboutme.txt'
            
            
            }
        }
        stage('Deploy') { 
            steps {
                archiveArtifacts artifacts: 'aboutme.txt'
            }
        }
    }
}
