import boto3

def lambda_handler(event, context):
    glue_job_name = event['detail']['jobName']
    status = event['detail']['state']

    if status != 'SUCCEEDED':
        sns = boto3.client('sns')
        sns.publish(
            TopicArn='arn:aws:sns:us-east-1:your-account-id:glue-alerts',
            Subject=f'Glue Job {status}',
            Message=f'The Glue Job "{glue_job_name}" has {status}. Please investigate.'
        )
