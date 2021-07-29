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
