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
```
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
```

# Shutting Down (Stop) the EC2 Instance
- Create bash file named ec2instance_stop.sh in user home directory (/home/ec2-user) with: **nano ec2instance_stop.sh**
- Enter the srcipt to stop the EC2 instance at 9pm in this file: **aws ec2 stop-instances --instance-ids i-XXXXXXXXXXXXXX** then save the file
- Edit crontab as an superuser in the /etc irectory with **sudo nano /etc/crontab** 
- Enter cron script to run the bash file to stop the instance at 9pm: **00  21  * * * sh /home/ec2-user/ec2instance_stop.sh > /tmp/ec2instance_stop.log** then save the file
