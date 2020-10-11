import boto3
import requests
import datetime
import time
import cv2

client=boto3.client('rekognition',
                    aws_access_key_id="ASIA5GJGJ3KQFMRYQ3WM",
                        aws_secret_access_key="c5zaKNagvl1HqK6MtwSApGQ3pwNw3Nf3FkLvOLt+",
                        aws_session_token="FwoGZXIvYXdzEE8aDKk/7wywb3mJP1Q+NiLKAQqSF4kFT7eCeCHxcIkH5CAxaWrin675aiYthVW87olU437C/mnrCgi4WlvDmtXE+S3Q8C802705IWf7AcgpdVZnxXhnY8mWFHDTxDVdlGPy4ZwwKdOvC5dnkgoGyG1lKloHGFfOvL2ZQXHm2Hhkq3y8ZCYWgzR0XlvMQfZZOqQVCR212ZFw9E33WRp/TPFqLBYbIArZzXOqV14LrX5UsJEnAUYzjavlLOuSkI2qsd7X9xwFEORVEwVS7df8pn+9y4Y3D53waiRii0oowZ+M/AUyLZEMlQehQTWduBHpBoS0cE8rUrxV9QigVOGfkcJMomxXX1w4qy/pBkokltUsxA==",
                        region_name='us-east-1')


for hr in range(0, 5):
    current_time = datetime.datetime.now().strftime("%d-%m-%y  %H-%M-%S ")
    print(current_time)
    cam = cv2.VideoCapture(0)
    for i in range(20):
        value, image = cam.read()
        if (i == 19):
            cv2.imwrite('images/' + current_time + '.jpg', image)
    del (cam)

    clients3 = boto3.client('s3', region_name='us-east-1')
    clients3.upload_file("images/"+current_time+'.jpg', 'count-attendance', current_time+'.jpg')



    with open(r'images/Chandler01.jpg','rb') as source_image:
        source_bytes = source_image.read()
    print(type(source_bytes))

    print("Recognition Service")
    response = client.detect_custom_labels(
        ProjectVersionArn='arn:aws:rekognition:us-east-1:906855307936:project/HourlyAttendanceCapturingSystem/version/HourlyAttendanceCapturingSystem.2020-10-10T19.06.48/1602337008460',
       
        Image={
            'Bytes':source_bytes

        },
       
    )

    print(response)
    if not len(response['CustomLabels']):
        print('Person not identified')

    else:
        str=response['CustomLabels'][0]['Name']
        url="https://zdjdrlb439.execute-api.us-east-1.amazonaws.com/test?rollNo="+str
        resp = requests.get(url)
        print(resp)
        
        time.sleep(3600)