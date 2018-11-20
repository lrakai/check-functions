import boto3
import botocore

# Lambda function
def handler(event, context):
	# init session
    client = create_new_session(event).client('iam')
    
    payload = client.get_user(UserName='student')
    
    return True if 'PasswordLastUsed' in payload['User'] else False

# helpers
def create_new_session(event):
    return boto3.Session(
        aws_access_key_id=event['credentials']['credential_id'],
        aws_secret_access_key=event['credentials']['credential_key'],
      	region_name=event['region_id']
    )