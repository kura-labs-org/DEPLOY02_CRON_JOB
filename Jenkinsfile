pipline{
    agent {label 'Test'}
    triggers {
        cron('*/10 * * * *')
    }
    stages{
        stage ('Build'){
            sh 'python3 bin/build.py'
        }
        stage ('Test'){
            sh 'python3 /bin/test.py'
        }
        stage ('Deploy'){
            sh 'python3 /bin/deploy.py'
        }
    }
}
