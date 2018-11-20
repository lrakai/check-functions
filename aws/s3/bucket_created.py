import boto3
import botocore

# Lambda function
def handler(event, context):
    s3 = create_new_session(event).resource('s3')
    return any(s3.buckets.iterator())

# helpers
def create_new_session(event):
    return boto3.Session(
        aws_access_key_id=event['credentials']['credential_id'],
        aws_secret_access_key=event['credentials']['credential_key'],
      	region_name=event['region_id']
    )