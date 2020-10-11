import json
import boto3

dynamo = boto3.resource("dynamodb")
table = dynamo.Table("Attendance_Count")

def lambda_handler(event, context):
    # TODO implement
    response = table.scan()
    items = response['Items']
    for i, j in enumerate(items):
        print(j['RollNo'],j['Count'],j['Name'])
        
    return items