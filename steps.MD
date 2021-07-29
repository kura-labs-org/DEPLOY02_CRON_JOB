# Steps to schedule pipeline
- Fork the reporitory from Kura Labs GitHub
- Edit Jenkinsfile and insert the sample pipeline groovy code
- Edit each step to include a simple bash command
- Include cron trigger syntax below the agent line: triggers { cron('H/10 * * * *') } 
- Commit changes
- In Jenkins, click on New Item
- Enter name for pipeline, click on Multibranch Pipeline, and then click OK
- Under Branch Sources, select GitHub
- Under Credentials, select the GitHub credential previously entered from the previous pipeline setup
- Select Repository Scan andunder Owner, enter GitHub username
- Click on Repository to trigger the scan of the repository
- After the scan is done, select the forked repository from the list, then clck Save.
- Click on "main" to view the scheduled builds.

## Pipeline Groovy Code
pipeline {
    agent any 
    triggers {
        cron('H/10 * * * *')
    }
    stages {
        stage('Build') { 
            steps {
                echo "Building for second deployment"
            }
        }
        stage('Test') { 
            steps {
                echo "Testing for second deployment"
            }
        }
        stage('Deploy') { 
            steps {
                echo "Deploying second deployment"
            }
        }
    }
}

# Shutting Down the EC2 Instance
