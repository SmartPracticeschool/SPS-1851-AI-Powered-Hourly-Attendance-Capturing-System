# SPS-1851-AI-Powered-Hourly-Attendance-Capturing-System
## Problem
Maintaining attendance is very important in all the institutes for checking the attendance percentage of Students. Every institute has its own method in this regard. Some are taking attendance manually on the register for every hour and later they will upload every hour data of a class to the server or file-based approach and some have adopted methods of automatic attendance using some biometric techniques. But these methods are inefficient and time-consuming, AI can definitely find a solution to this problem.
## Proposed Solution
The proposed solution/application shall capture hourly attendance without any manual intervention. develop a smart device that can be integrated with a camera that will capture the images of class for every hour and send the images to model.  Then the model will use AWS Rekognition Service to recognize the student’s faces & push the images to S3(Simple Storage Service) for storage and also updates the attendance automatically in a database. build a web-based dashboard to visualize all the student’s attendance information. 
## Project Flow:
<ul>
<li>Store the Images of Students in S3 Bucket

<li>Capture the image on an Hourly basis

<li>Load the image to Face comparison algorithm (compares the faces in s3 bucket)

<li>Mark the attendance for compared faces and store in DynamoDb

<li>Create a rest API using API gateway and lambda function to connect to dynamo DB through web app

<li>Create a web-based dashboard to visualize the attendance
</ul>

## Proposed Technical Architecture
<img src="Project-Architecture.png" alt="Architecture">

## Demo Link
<a href="https://drive.google.com/file/d/1WAscOaCp-AY7B0CBY3PupHlZCpZTkT6h/view?usp=sharing">Demo</a>
