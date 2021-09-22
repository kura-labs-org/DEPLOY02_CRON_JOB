# DEPLOY02_CRON_JOB

<h1 align=center>Deployment 2</h1>

Congratulations on completing your first deployment!! Next you will have to make a pipeline script with a Build, Test, and Deployment stage. After you create the script; trigger your build for every 10 minutes. Once you have successfully ran a scheduled job, find a way to schedule your ec2 to shutdown by the end of class. 

- Document the steps it took you to complete this task
- Screenshots at least 2 successful scheduled trigger builds 
- Fork this repo 👉(https://github.com/kura-labs-org/DEPLOY02_CRON_JOB) for the blank Jenkinsfile and make a pull request with:
  1. Documentation
  2. Screenshots
  3. Jenkins pipeline script   

#  **Good Luck!!** :four_leaf_clover: 

![Jenkins](https://www.jenkins.io/images/logos/needs-you/Jenkins_Needs_You-transparent.png)

<h1>Documentation </h1>

<h2>Task:</h2>
Deploy Jenkins on a Linux system to and create a pipeline to include 3 stages (Build, Deploy and Test)
Following this, the parameters of this job must include a build every 10 minutes.
Last, a shutdown at the end of class (Tues-Thurs 9PM, Sat 5PM)

Instructions broken down as followed:
--Set up EC2 Instances
--SSHing and Linux setup
--SSH KEYS
--Git
--Jenkins
--Shutting down at the end of class

<h2>Set up EC2 Instances</h2>
-Set configurations on EC2 with t.2 micro, default storage, and default on tags.
-For network security, allow port 22 on "My IP" and 8080 on "My IP" as well.
-SSH Key, select one or create one and use on the SSH Client of your preference
-Locate your Public IP on the EC2 Dashboard, copy and use on your client

<h2>SSHing and Linux setup</h2>
-Once logged in run the following commands:
sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
sudo yum upgrade
sudo yum install jenkins java-1.8.0-openjdk-devel git -y
sudo systemctl daemon -reload
sudo systemctl start jenkins
#You're using wget to pull the repository from the jenkins web repository, then adding the key to your package maanger rpm to allow access to the repo just added.
#The upgrade will update the repository list and install the respective programs
#The next two commands will reload the system daemon and start jenkins

<h2>SSH KEYS</h2>
#In order to use git ssh, you have to run the following commands
Commands:
ssh-keygen -C "youremailaddress"
cd ./ssh
cat ida_rsa.pub
-Copy that key into the github Settings -> SSH and GPG keys ->Select SSH Key
##To note this is an RSA 2048 bit key, not the ones made in class. to make that, add flag -b and 4096.


<h2>Git</h2>
-Fork the git using the website
-Use the following commands:
mkdir Deployment2
cd Deployment2
git init
git config --global user.name "yourname"
git add remote origin "git@github.com/yoursuser/DEPLOY02_CRON_JOB
git branch -M main
git pull origin main

<h2>Jenkins</h2>+
#Jenkins has started with a webgui on publicIP:8080
-Go to publicIP:8080 on your browser.
-Follow the directions to find the secret password using the listed directory via cat command
-Select New item --> Give it a name --> Select multibranch Pipeline and Ok.
-Go down to Branch Sources, select Github -->add (Jenkins-webhook) --> add username of github and a password or the personal access token.
-Select repository Scan, in the Owner, type in the username of the github if there is nothing popping up
-Select DEPLOY02_cron_job
-Save
-See Jenkinsfile for Code
-Go to Configure --> Scan Repository Triggers --> Check Periodic --> Set for 10 minutes.
##This step was done in lieu of a Build Trigger since this Project item does not seem to have a Build Trigger Function Setting in the Pipeline, and in the branches configuration, there is no way to enable the Build Trigger. However, if a Build trigger cron job was needed. add to cron: */10 * * * * 


<h2>Shutting down at end of class</h2>
#There are two ways of doing this. First is the cron job, and the second is the Instance Scheduler on AWS.
#Cron
-Check time and date of the Linux Machine using command:
date
-Change and check the timezone based on the desired timezone you want to be in:
timedatectl list-timezones
##Find the Timezone for you
sudo timedatectl set-timezone <your_time_zone>
timedatectl
-Adding a cronjob to shutdown
##For cronjobs, you invoke the command based on the user that edits the cron. For this job, this must be invoked from the sbin, so a user with superuser group or even the root user itself.
sudo crontab -e
00 21 * * 2-4 sudo shutdown -h now
00 17 * * 6 sudo shutdown -h now
##The super user will invoke the command and therefore add to the cron jobs to shutdown immediately as the command is down at every 9PM. Even though it's a superuser inputting this, the sudo must be placed in because shutdown is a command that belongs to the sbin, so the sytem will know that this is invoked from sbin instead of bin.
##Last, You can also have the ec2-user do this without the sudo crontab -e and just crontab -e regular if you add them to the sudo group.
-Check that the cron has been successfully placed in.
sudo crontab -l
##Usually with crontab, the commands are checked and verified, so it's harder to make a mistake. It also updates the file and cron service, so no reload/restart of service is needed.
##Read here for AWS Instance scheduler
https://docs.aws.amazon.com/solutions/latest/instance-scheduler/deployment.html#step1
