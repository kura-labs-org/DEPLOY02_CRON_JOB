// Build once a day
CRON_SETTINGS = '''*/10 * * * *'''

// Multi-branch pipeline. Build once a day from a "master" branch only
CRON_SETTINGS = BRANCH_NAME == "main" ? '''*/10 * * * *'''

pipeline {
    agent any
    triggers {
    cron(CRON_SETTINGS)
        }
      stages {
        stage('Build') {
            steps {
                echo 'Building - Hello World'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing - Hello World'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying - Hello World'
            }
        }
    }
}
