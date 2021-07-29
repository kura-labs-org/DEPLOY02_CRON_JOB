# Documentation for Second Deployment

## Setup

1. Start a new EC2 Amaxon Linux instance from AWS. With the following Bootstrap script
```
#!/bin/bash
sudo yum update -y 
sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
sudo yum upgrade 
sudo yum install jenkins java-1.8.0-openjdk-devel -y 
sudo systemctl daemon-reload
sudo systemctl start jenkins

sudo yum install git -y

```

2. For security groups set an SSH port of 22, HTTP port of 80, and a Custom TCP Rule with port 8080.
3. Finally launch your EC2 Instance.
4. Once launched ssh into your instance by navigating to the directory which contains your SSH keys and running the following

```
cd {directory where your key is located}
ssh -i {EC2 Keys} ec2-user@{public IPV4 address of your instance}
```
5. Then run the command sudo systemctl status jenkins; to make sure Jenkins is running.
6. Run the following command and copy the output to paste later.
```
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```
7. Once jenkins is running enter the public IPV4 address of your instance with port 8080. Example would be 12.313.123.180:8080
8. Paste what you recently copied from step 7 for the jenkins password.
9. Install suggested plugins for Jenkins.
10. Setup admin account with your email, password, username.
11. Fork the DEPLOY2_CRON_JOB directory and edit your Jenkins file with the following code to create a pipeline with a Build, test, deploy stage.
```
pipeline { 
    agent any 
    options {
        skipStagesAfterUnstable()
    }
    triggers {
        cron('*/10 * * * *')
        
    }
    stages {
        stage('Build') { 
            steps { 
                echo "Currently in the building phase"
            }
        }
        stage('Test'){
            steps {
              echo "Finished the building stage"
               echo "Currently in the testing phase"
            }
        }
        stage('Deploy') {
            steps {
                echo "Finished the testing stage"
                echo "Currently deploying"
            }
        }
    }
}
```
12. For Jenkins to actually read our Jenkins file we need to create a webhook to our github repo
13. Go to your GitHub account settings and create a personal account token, and copy the value and save it somewhere safe(it will disappear).
14. Navigate back to your Jenkins instance and go to the dashboard to create a new item.
15. Name it what you desire such as Jenkins Cron Job, and select the multibranch pipeline.
16. Then add the branch source as GitHub and click on add then click on Jenkins.
17. Add your GitHub account info for the username field, and then enter your personal account token into the password field.
18. For the ID field enter jenkins-webhook-id.
19. Then set credentials next to the add button. Then for the owner field enter your GitHub account info where the forked repository is hosted.
20. Finally save your Pipeline and watch it build every ten minutes.
