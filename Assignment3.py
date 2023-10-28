import boto3

def lambda_handler(event, context):
    # Replace 'neeraj_rds' with the name of your RDS instance
    rds_instance_name = 'neeraj_rds'
    
    # Initialize a boto3 RDS client
    rds_client = boto3.client('rds')

    try:
        # Take a snapshot of the specified RDS instance
        snapshot_identifier = f'{rds_instance_name}-snapshot-{event["time"]}'  # Customize the snapshot identifier
        response = rds_client.create_db_snapshot(
            DBSnapshotIdentifier=snapshot_identifier,
            DBInstanceIdentifier=rds_instance_name
        )

        # Print the snapshot ID for logging purposes
        snapshot_id = response['DBSnapshot']['DBSnapshotIdentifier']
        print(f'Snapshot created: {snapshot_id}')

    except Exception as e:
        print(f'Error creating snapshot: {str(e)}')
        raise e
