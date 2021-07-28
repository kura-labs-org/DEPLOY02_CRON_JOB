pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'rm -rf deployment2'
                sh 'mkdir deployment2'
                sh 'cd deployment2'
                sh 'touch aboutme.txt'
                sh 'echo "My name is Brittney Jones." > aboutme.txt'
                sh 'echo "I am 24 years old." > aboutme.txt'
                sh 'echo "I am from New York but born and partially raised in Trinidad and Tobago." > aboutme.txt'
            }
        }
        stage('Test') { 
            steps {
             sh 'cd ..'
             sh 'test -f aboutme.txt'
            // sh 'grep -c "name" aboutme.txt'
            // sh 'grep -c "years" aboutme.txt'
            // sh 'grep -c "raised" aboutme.txt'
            }
        }
        stage('Deploy') { 
            steps {
                archiveArtifacts artifacts: 'deployment2/'
            }
        }
    }
}
