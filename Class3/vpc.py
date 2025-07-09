import boto3

ec2 = boto3.client('ec2', region_name='us-west-2')
vpcs = ec2.describe_vpcs()

for vpc in vpcs['Vpcs']:
    vpc_id = vpc['VpcId']
    is_default = vpc.get('IsDefault', False)

    if is_default:
        print(f"Skipping default VPC: {vpc_id}")
        continue

    name_is_kaizen = False
    for tag in vpc.get('Tags', []):
        if tag['Key'] == 'Name' and tag['Value'] == 'kaizen':
            name_is_kaizen = True
            break

    if name_is_kaizen:
        print(f"Skipping VPC with name 'Kaizen': {vpc_id}")
        continue

    try:
        ec2.delete_vpc(VpcId=vpc_id)
        print(f"Deleted VPC: {vpc_id}")
    except Exception as e:
        print(f"Failed to delete {vpc_id}: {e}")





