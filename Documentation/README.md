# DEPLOY02_CRON_JOB
<h1 align=center>Deployment 2</h1>

<h2>Tasks</h2>

    1. Build Software
    2. Test Software
    3. Deploy Software

# Build

To start with the build I needed to make sure the tools needed are available. Tools necessary: g++, python3

    sudo yum install gcc-c++ python3 -y 
This allows you to check if the updated version of python3 is active and install g++ which is being used to compile the C++ example program

Script:

         build.py

Behavior:

This scripts checks if the example software exists. If the example file exists it tries to compile it using g++. On sucessful build it will move it to the testing folder and write the sucsessful log and moves the file onto the testing stage. On error documents the error and exits with error code 1

# Testing

Runs Script to make sure there are no errors before deploying code

Script:

        testing.py
Behavior:

Checks if there is a main file in the testing stage. If there is a file it will execute and check for errors. Moves to deployment stage on successful run.

# Deployment 

Executes Code and deploy

Script:

        deploy.py
Behavior:

Attempts to deploy code then deletes it to test out the cron job to redeploy the build

