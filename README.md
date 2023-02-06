# Skillstorm CodeCommit / CodeBuild / CodePipeline / ECR / ECS with Fargate demo

##Steps:

1) Download this GitHub repository as a .ZIP file.
2) Unzip files into a folder of your choosing on your local machine.
3) Open the folder in VSCODE.
-----------------------------------------------------------------------------------------------------------------------------------------
4) In the AWS management console, choose IAM and create a new User.
5) Choose 'Attach Policies Directly' and search for **'AWSCodeCommitPowerUser'**
6) Click the check box next to the AWS managed policy named 'AWSCodeCommitPowerUser' and Save.
-----------------------------------------------------------------------------------------------------------------------------------------
7) Generate GIT credentials by clicking into the just created User.
8) Under the **'Security Credentials'** tab, scroll down until you see **'HTTPS Git credentials for AWS CodeCommit'**.
9) Click the **'Generate Credentials'** button.
10) **Copy** the username and password for later use. You can also download a .csv file with the username and password.
-----------------------------------------------------------------------------------------------------------------------------------------
11) In the AWS management console, choose CodeCommit and create a new repository.
12) Give the repository a name.
-----------------------------------------------------------------------------------------------------------------------------------------
13) Go back to VSCODE and open the file **'buildspec.yml'**
14) Replace the four occurances of \<NAME OF YOUR IMAGE FILE\> with a name of your choosing. example: abc-docker-image
15) This is the name of the image file docker will build when you run **CodeBuild**. CodeBuild will run this **buildspec.yml** file.
-----------------------------------------------------------------------------------------------------------------------------------------
16) Next open the file **'imagedefinitions.json'**
17) Replace \<NAME OF YOUR CONTAINER\> with a name of your choosing. example: abc-docker-container
18) Replace \<NAME OF YOUR IMAGE FILE\> with the name you chose in Step 14.
-----------------------------------------------------------------------------------------------------------------------------------------
19) In the terminal in VSCODE, we will **connect** to the CodeCommit repository.
20) In the terminal type: 
```
21) **git init**
22) **git add .**
23) **git commit -m "first commit"**
24) **git remote add origin https://git-codecommit.us-east-1.amazonaws.com/v1/repos/\<NAME OF YOUR REPO\>**
25) **git branch -M main**
26) **git push -u origin main**
```
27) You will be prompted to enter your username and password.  Copy the username and password you generated in Step 10.
28) In the AWS management console, choose CodeCommit and ensure your files were pushed to the repository successfully.
-----------------------------------------------------------------------------------------------------------------------------------------

