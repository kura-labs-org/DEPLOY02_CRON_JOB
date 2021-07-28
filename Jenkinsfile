pipeline{
    agent any
    triggers {
        cron('*/1 * * * *')
    }
    stages{
        stage ('Build'){
            steps{
            sh 'python3 bin/build.py'
        }
        }
        stage ('Test'){
            steps{
            sh 'python3 bin/testing.py'
        }
        }
        stage ('Deploy'){
            steps{
            sh 'python3 bin/deploy.py'
        }
    }
    }
}
