// Build once a day
CRON_SETTINGS = '''*/1 * * * *'''

// Multi-branch pipeline. Build once a day from a "master" branch only
CRON_SETTINGS = BRANCH_NAME == "main" ? '''*/1 * * * *'''

pipeline {
    agent any
        triggers {
            cron(*/1 * * * *)
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
