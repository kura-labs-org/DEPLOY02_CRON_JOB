# DEPLOY02_CRON_JOB

<h1 align=center>Deployment on Jenkins with cronjob</h1>

Click below to view my docs

https://docs.google.com/document/d/1pFUNuBkOsdp1UQSBUXJ3u4yVM-z82NT4TCfALEn78u4/edit?usp=sharing

I tried to ssh into my ec2 and got this error “ssh: connect to host 3.86.203.87 port 22: Connection timed out”
I changed my ssh inbound setting to anywhere and it worked
I tried to set up a pipeline in Jenkins and my first build failed.  I got this error “Error cloning remote repo 'origin'
I then installed git to my ec2 using sudo yum install git -y
I created a new job and selected a multibranch pipeline.
I added my github credentials and the access token in order for Jenkins to have access to my Github.
The first few builds failed and I watched a youtube video and realized I had to change the branch from main to master.
I changed the branch specifier from master to main and the build was a success
I set a cron job that would run the job every 10 minutes. I created a cron job variable and I used https://crontab.guru/#*_*_*_* to help me set up the cron job syntax (That was a struggle for me lol). The variable and its value was was  CRON_JOB = '''  */10 * * * * '''. I called on the variable in my trigger. 


![image](https://user-images.githubusercontent.com/16675605/138933752-7d6b6ad1-5dd6-45cc-a099-dba408fbc303.png)

![image](https://user-images.githubusercontent.com/16675605/138933861-5c2a4066-786d-406a-82f6-f6d9c6659716.png)
