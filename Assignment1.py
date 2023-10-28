import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Describe instances with the 'Auto-Stop' and 'Auto-Start' tags
    auto_stop_instances = ec2.describe_instances(Filters=[{'Name': 'tag:Action', 'Values': ['Auto-Stop']}])
    auto_start_instances = ec2.describe_instances(Filters=[{'Name': 'tag:Action', 'Values': ['Auto-Start']}])

    # Stop instances with the 'Auto-Stop' tag
    for reservation in auto_stop_instances['Reservations']:
        for instance in reservation['Instances']:
            ec2.stop_instances(InstanceIds=[instance['InstanceId']])

    # Start instances with the 'Auto-Start' tag
    for reservation in auto_start_instances['Reservations']:
        for instance in reservation['Instances']:
            ec2.start_instances(InstanceIds=[instance['InstanceId']])

    # Print instance IDs that were affected for logging purposes
    affected_instance_ids = [instance['InstanceId'] for reservation in auto_stop_instances['Reservations']] + [instance['InstanceId'] for reservation in auto_start_instances['Reservations']]
    print("Instances affected:", affected_instance_ids)
