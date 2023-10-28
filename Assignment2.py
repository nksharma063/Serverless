import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    neeraj_s3 = boto3.client('s3')
    bucket_name = 'neeraj-s3-test'  # Replace with your bucket name

    # Calculate the date 30 days ago
    thirty_days_ago = (datetime.now() - timedelta(days=30)).isoformat()

    # List objects in the specified bucket
    objects = neeraj_s3.list_objects_v2(Bucket=neeraj-s3-test)

    # Delete objects older than 30 days
    for obj in objects.get('Contents', []):
        if obj['LastModified'].isoformat() < thirty_days_ago:
            neeraj_s3.delete_object(Bucket=neeraj-s3-test, Key=obj['Key'])

            # Print the names of deleted objects for logging purposes
            print("Deleted:", obj['Key'])
