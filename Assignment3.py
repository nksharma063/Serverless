import boto3

def lambda_handler(event, context):
    # Replace 'your_rds_instance_name' with the name of your RDS instance
    rds_instance_name = 'your_rds_instance_name'
    
    # Initialize a boto3 RDS client
    rds_client = boto3.client('rds')

    try:
        # Take a snapshot of the specified RDS instance
        response = rds_client.create_db_snapshot(
            DBSnapshotIdentifier=f'{rds_instance_name}-snapshot-{event["time"]}',  # You can customize the snapshot identifier
            DBInstanceIdentifier=rds_instance_name
        )

        # Print the snapshot ID for logging purposes
        snapshot_id = response['DBSnapshot']['DBSnapshotIdentifier']
        print(f'Snapshot created: {snapshot_id}')

    except Exception as e:
        print(f'Error creating snapshot: {str(e)}')
        raise e

