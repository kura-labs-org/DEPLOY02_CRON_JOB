pipeline{
    agent {label 'Test'}
    triggers {
        cron('*/10 * * * *')
    }
    stages{
        stage ('Build'){
            steps{
            sh 'python3 bin/build.py'
        }
        }
        stage ('Test'){
            steps{
            sh 'python3 /bin/test.py'
        }
        }
        stage ('Deploy'){
            steps{
            sh 'python3 /bin/deploy.py'
        }
    }
    }
}
