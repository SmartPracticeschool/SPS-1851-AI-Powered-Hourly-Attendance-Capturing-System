import json
import boto3

dynamo = boto3.resource("dynamodb")

table = dynamo.Table("Attendance_Count")
def lambda_handler(event, context):
    # TODO implement
    res = table.get_item(Key = {"RollNo" : event['RollNo']})
    print(res['Item']['Name'])
    Count = res['Item']['Count']
    Count= Count+1
    inp = {"RollNo" : event['RollNo'], "Count" : Count, "Name" : res['Item']['Name']}
    table.put_item(Item = inp)
    return "Successful"