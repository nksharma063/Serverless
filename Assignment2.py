import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'your-bucket-name'  # Replace with your bucket name

    # Calculate the date 30 days ago
    thirty_days_ago = (datetime.now() - timedelta(days=30)).isoformat()

    # List objects in the specified bucket
    objects = s3.list_objects_v2(Bucket=bucket_name)

    # Delete objects older than 30 days
    for obj in objects.get('Contents', []):
        if obj['LastModified'].isoformat() < thirty_days_ago:
            s3.delete_object(Bucket=bucket_name, Key=obj['Key'])

            # Print the names of deleted objects for logging purposes
            print("Deleted:", obj['Key'])
