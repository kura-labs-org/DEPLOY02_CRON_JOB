

# Documentation

# Setup
I started an EC2 instance with the right network security configurations so that we could access the Jenkins server we'd be making.
I used a bootstrap script to have the instance be loaded with Docker, Git, and Jenkins and all their dependencies when it boots up.
The script also involved running both docker and Jenkins.

Once the instance was running, I was able to connect to the serve on port `8080` and then I followed the same Jenkins process as last time.
*For the most part.* This time, I also added a Docker plugin. The reason I did this was because I wanted to be able to actually "build" something
in the build phase.

It took me quite a while actually to get it set up. I kept getting errors about how it tried to pull from the docker repository but I didn't have the right
permissions. Before that I was getting an error that Docker doesn't exist. To fix the not existing error, I had to just install docker. To fix the missing
permissions error I had to download the docker plugin and then I also had to add the user `jenkins` to have access to docker. I did this by using the `groupmod`
command from the terminal. After that I had to "refresh" the terminal so that the docker instance had the updated permissions.

After this, my Jenkins pipeline was able to run successfully. Below is my JenkinsFile
```
pipeline {
    agent { docker { image 'python:3.5.1' } }
    triggers {
        cron('H/10 * * * *')
    }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test') { 
            steps {
               echo 'testing stage...'
            }
        }
        stage('Deploy') { 
            steps {
                echo 'deploying stage'
            }
        }
    }
}
```
When I ran the pipeline, the console in Jenkins showed that python succesfully installed and it printed out the correct version too.

To make it run on schedule, I added a triggers step in the jenkins file with the cron job `'H/10 * * * *`.

Finally to make the ec2 instance shutdown, I used a cronjob with the set time and had it run the shutdown command at the given time.

![Screen Shot 2021-08-07 at 11 23 51 AM](https://user-images.githubusercontent.com/42876250/128605217-d6cf7216-d150-443f-9c94-ded2d948ffa2.png)

I didn't get to take pictures of the builds on Jenkins, but in my commit history you can see the green checkmarks next to the succesfull builds and the red x next to failed builds and nothing next to a commit when Jenkins wasn't connected.
