# Documentation for Second Deployment

## Setup

1. Start a new EC2 Amaxon Linux instance from AWS. With the following Bootstrap script
```
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
3. Finally launch your EC2 Instance
