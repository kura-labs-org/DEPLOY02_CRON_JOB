pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                mkdir deployment2
                touch deployment2/aboutme.txt
                echo "My name is Brittney Jones." > deployment2/aboutme.txt
                echo "I am 24 years old." > deployment2/aboutme.txt
                echo "I am from New York but born and partially raised in Trinidad and Tobago." > deployment2/aboutme.txt
            }
        }
       // stage('Test') { 
           // steps {
           //    test -f deployment2/aboutme.txt'
            //  grep "name" aboutme.txt'
              // sh 'grep "years" aboutme.txt'
               //sh 'grep "raised" aboutme.txt'
            //}
        //}
       // stage('Deploy') { 
         //   steps {
           //     archiveArtifacts artifacts: 'deployment2/'
            //}
        //}
    }
}
