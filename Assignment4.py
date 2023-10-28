import boto3

def lambda_handler(event, context):
    # Initialize a boto3 S3 client
    s3_client = boto3.client('s3')

    try:
        # List all S3 buckets
        response = s3_client.list_buckets()
        buckets = response['Buckets']

        unencrypted_buckets = []

        # Detect buckets without server-side encryption
        for bucket in buckets:
            bucket_name = bucket['Name']
            bucket_policy = s3_client.get_bucket_encryption(Bucket=bucket_name)
            if 'ServerSideEncryptionConfiguration' not in bucket_policy:
                unencrypted_buckets.append(bucket_name)

        # Print the names of unencrypted buckets for logging purposes
        if unencrypted_buckets:
            print("Unencrypted S3 Buckets:")
            for bucket_name in unencrypted_buckets:
                print(bucket_name)
        else:
            print("No unencrypted S3 buckets found.")

    except Exception as e:
        print(f'Error detecting unencrypted buckets: {str(e)}')
        raise e
