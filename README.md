# Skillstorm CodeCommit / CodeBuild / CodePipeline / ECR / ECS with Fargate demo

NOTE: I suggest opening a blank text file to copy and paste to, to keep track of all of the names you will be using for the various repositories, images, containers, username, password, etc. You will need to refer to them in later steps.

## Steps:

1) Download this GitHub repository as a .ZIP file. (click the green button **CODE** and choose **Download Zip**)
2) Unzip files into a folder of your choosing on your local machine.
3) Open the folder in VSCODE.
-----------------------------------------------------------------------------------------------------------------------------------------
4) In the AWS management console, choose IAM and create a new User.
5) Choose 'Attach Policies Directly' and search for *'AWSCodeCommitPowerUser'*
6) Click the check box next to the AWS managed policy named *'AWSCodeCommitPowerUser'* and Save.
-----------------------------------------------------------------------------------------------------------------------------------------
7) Generate GIT credentials by clicking into the just created User.
8) Under the **Security Credentials** tab, scroll down until you see **HTTPS Git credentials for AWS CodeCommit**.
9) Click the **Generate Credentials** button.
10) **Copy** the username and password for later use. You can also **download** a .csv file with the username and password.
-----------------------------------------------------------------------------------------------------------------------------------------
11) In the AWS management console, choose CodeCommit and create a new repository.
12) Give the repository a name.
-----------------------------------------------------------------------------------------------------------------------------------------
13) Go back to VSCODE and open the file **'buildspec.yml'**
14) Replace the four occurances of \<NAME OF YOUR IMAGE FILE\> with a name of your choosing. *example: abc-docker-image*
15) This is the name of the image file **docker** will used to build when you run **CodeBuild**. CodeBuild uses **buildspec.yml** to know what to do.
-----------------------------------------------------------------------------------------------------------------------------------------
16) Next open the file **imagedefinitions.json**
17) Replace \<NAME OF YOUR CONTAINER\> with a name of your choosing. *example: abc-docker-container*
18) Replace \<NAME OF YOUR IMAGE FILE\> with the name you chose in Step 14.
-----------------------------------------------------------------------------------------------------------------------------------------
19) In the terminal in VSCODE, we will **connect** to the CodeCommit repository.
20) In the terminal type: (make sure to change \<NAME OF YOUR REPO\> with the name of your CodeCommit repository)
```
git init
git add .
git commit -m "first commit"
git remote add origin https://git-codecommit.us-east-1.amazonaws.com/v1/repos/<NAME OF YOUR REPO>
git branch -M main
git push -u origin main
```
27) You will be prompted to enter your username and password.  Copy the username and password you generated in Step 10.
28) In the AWS management console, choose CodeCommit and ensure your files were pushed to the repository successfully. You now have a **Git Repository** to store all of your source code.
-----------------------------------------------------------------------------------------------------------------------------------------
29) In the AWS management console, choose **CodeBuild -> Build Projects -> Create Build Project.**
30) Give the project a name. *example: abc-codebuild*
31) Under Source Provider choose **AWS CodeCommit**
32) Under Repository choose your CodeCommit repository.
33) Keep the Reference Type as Branch and choose your **main** branch in the dropdown.
34) For Environment Image keep **Managed Image** selected.
35) Choose **Amazon Linux 2** for the Operating System.
36) Choose **Standard** for the Runtime.
37) Choose **aws/codebuild/amazonlinux2-x86_64-standard:4.0** (the last option in the dropdown) for Image.
38) Check the box under **Privileged** that says *"Enable this flag if you want to build Docker images or want your builds to get elevated privileges".* This needs to be selected so you can build images with Docker.
39) Create a new service role and give it a name. *example: abc-codebuild-service-role*
40) Leave the rest as defaults and click **Create build project**
-----------------------------------------------------------------------------------------------------------------------------------------
41) In the AWS management console, choose IAM -> Roles.
42) In the search box, type the name of the role you created in Step 39.
43) Click on the role and under the **Permissions** tab, click **Add Permissions -> Attach Policies**.
44) In the **Search Box** type *'AmazonElasticContainerRegistryPublicFullAccess'* and check the box next to it.
45) Clear the filters for the search box and then type in *'CloudWatchLogsFullAccess'* and check the box next to it.
46) Click **Attach Policies**
-----------------------------------------------------------------------------------------------------------------------------------------
47) In the AWS management console, choose **Elastic Container Registry -> Repositories -> Create Repository.**
48) Keep the Visibility Settings as **Public**
49) For the Repository Name enter in the name of your image file from Step 14. (this doesn't have to be the image file name but doing so keeps it less confusing)
50) Click **Create repository**.
51) You now have an **Elastic Container Repository** where your Docker Image file can be stored when you run your **CodeBuild Build Project**.
-----------------------------------------------------------------------------------------------------------------------------------------
51) In the AWS management console, choose **CodeBuild -> Build Projects -> Click your build project**
52) Click the **Start build** button and monitor the progress of the build.
53) Click the **Phase Details** tab to ensure all of the phases *Succeeded*.
![CodeBuild Phase Details](https://github.com/jonjay80/skillstorm-codebuild-ECS/blob/main/images/CodeBuildPhaseDetailsCapture.PNG)
54) If you get any *Failed* statuses, click the **Build Logs** tab to review the logs and troubleshoot from there.
55) 
