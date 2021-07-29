# 2nd Deployment
# ----------------------------------**First Stage**-------------------------------
# Creating a jenkins pipeline with automatic deployments
### Step 1: 
#### SSH into your EC2 instance that has jenskins installed
![Screenshot 2021-07-29 135707](https://user-images.githubusercontent.com/60336145/127541828-b51409d6-ba1e-4652-9a77-0a07b96f435a.png)
### Step 2: 
####  type http://(your instance public IP):8080 into your browser then log into jenkins 
## if you forgot your jenkins password like me you can follow these steps.  [if not skip to step 3](https://github.com/hector6921/DEPLOY02_CRON_JOB/new/main#step-3)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
## cd / to go back to your top directory
## cd var/lib/jenkins/
## sudo nano config.xml and change the <useSecurity>true<useSecurity> tag to <useSecurity>false<useSecurity> and save
![Screenshot 2021-07-29 124830](https://user-images.githubusercontent.com/60336145/127543898-73b0b5cc-f17f-4311-ae60-56e4918e1bf8.png)
## Restart jenkins
![Screenshot 2021-07-29 124928](https://user-images.githubusercontent.com/60336145/127545675-3f47563e-d4f4-4c0c-982e-c730ead97692.png)
## refresh your jenkins login page, now it should not ask you for a password
## if you wish to make another account you can do so by going into manage jenkins
![Screenshot 2021-07-29 124952](https://user-images.githubusercontent.com/60336145/127544276-c8254a98-cf20-4491-96d7-e52e05a53aa9.png)
## Then configure global security
![Screenshot 2021-07-29 125023](https://user-images.githubusercontent.com/60336145/127544368-aa54a264-e08d-458f-85d6-c8b6d8c0deee.png)
## make sure you check the (Allow users to sign up) option
![Screenshot 2021-07-29 125055](https://user-images.githubusercontent.com/60336145/127544493-aca91377-6174-4ecd-b714-040ab2682db0.png)
## then you should see the option to sign up at the top right corner 
![Screenshot 2021-07-29 125118](https://user-images.githubusercontent.com/60336145/127544709-57c36198-5b0e-4a0c-84c9-47e6d7ba10ae.png)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
### step 3:
# Go to your jenkinsfile on yout forked repository
![Screenshot 2021-07-29 143350](https://user-images.githubusercontent.com/60336145/127547211-3e16b1cc-8f9e-4b44-afa0-e1fef20dd917.png)
# Add the pipeline script
![Screenshot 2021-07-29 142511](https://user-images.githubusercontent.com/60336145/127545915-712eb997-e68e-4e01-bf8f-b092b4334a5d.png)
### step 4:
# Create a multiple branch jenkins pipeline and add the pipeline script, click on New Item
![Screenshot 2021-07-29 142723](https://user-images.githubusercontent.com/60336145/127546203-3b217658-4d90-4ff6-b622-8dc4a31710c0.png)
# Then multibranch pipeline, press OK
![Screenshot 2021-07-29 142622](https://user-images.githubusercontent.com/60336145/127546081-4595b71a-d1fe-40e2-909a-b8462747dd3c.png)
# after you named your project insert the URL of your forked repository 
![Screenshot 2021-07-29 142826](https://user-images.githubusercontent.com/60336145/127548126-b8aa7b6d-c7bd-4b15-8950-e68cc36cade3.png)
![Screenshot 2021-07-29 142909](https://user-images.githubusercontent.com/60336145/127548232-ef0a4b48-68f1-411b-b46f-596422d9f781.png)
# Add credentials (*UserNameyour: * github username, *Password: * access token from yout settings->developer settings->personal token. create one if you don't have one, and the *ID: * is your project's name)
![Screenshot 2021-07-29 143022](https://user-images.githubusercontent.com/60336145/127548598-b4ff68f6-3870-4f8e-851c-160e03b41c17.png)
# Finally set your periodic builds to every 10 mins to check any new commits to your branch
![Screenshot 2021-07-29 143048](https://user-images.githubusercontent.com/60336145/127548910-ce145d3d-3b15-462a-801f-df7bb57118f4.png)
# After these steps you will be taken to the Scan repositoy page, it will tell if it successfully scanned your repository or not
![Screenshot 2021-07-29 123742](https://user-images.githubusercontent.com/60336145/127549320-1dc7ace4-c7f4-4563-b22c-077b83f3db2f.png)
# If you click on the UP icon it will take you your branches 
![Screenshot 2021-07-29 145254](https://user-images.githubusercontent.com/60336145/127549686-420b5789-24b0-41ad-84d1-959d6901c238.png)
# Clicking on you branche's name will show you the builds
![Screenshot 2021-07-29 125206](https://user-images.githubusercontent.com/60336145/127549801-68dcf136-bba4-4a70-b54e-92575a36a983.png)
# If you wait some time it will show the automatic deployments that take place every 10 minutes it there are new commits on your branch
![Screenshot 2021-07-29 133748](https://user-images.githubusercontent.com/60336145/127549907-76253457-79a5-4ca8-80e6-191d92ade64f.png)
# ----------------------------------**Second Stage**-------------------------------
# Stopping your instance with a cronjob
### 1st method
# sudo shutdown -P 00:00 choose your desired time
![Screenshot 2021-07-29 134721](https://user-images.githubusercontent.com/60336145/127550579-af78b342-3400-49c3-b19d-76e69bbdf895.png)
### 2nd Method
# using anacrontab's cron.hourly located in etc/cron.hourly add the hourly functionality into the anacrontab
![Screenshot 2021-07-29 150443](https://user-images.githubusercontent.com/60336145/127551146-f3589a6e-321a-434c-a796-66c217e2bab2.png)
# Write a script that will live in your cron.hourly folder (keep in mind the script will run every hour).  Using AWS CLI commands as will as other commands to get the info you need in this case the *Instance ID* is require for the ec2-stop command to work as well as AWS IAM credential (you will need to configure it with the root account).  This method work also if you need to terminate the instance since you can't do it fro the sustem itself.
![Screenshot 2021-07-29 134523](https://user-images.githubusercontent.com/60336145/127551799-0ace0fb8-81dd-41ee-843e-7184464a2383.png)
# now you should see your instance's state code change from 16 to 64 this means its being stopped and 48 if terminated 
  
* 0 : pending
* 16 : running
* 32 : shutting-down
* 48 : terminated
* 64 : stopping
* 80 : stopped
  
![Screenshot 2021-07-29 134829](https://user-images.githubusercontent.com/60336145/127551845-1b723111-1d97-4a79-89bb-0a4709f31636.png)





 
