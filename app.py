import os
import boto3


PARAM_NAME = os.environ.get('PARAM_NAME', 'dynamic_string_param')
ssm = boto3.client('ssm')


def handler(event, context):
    try:
        response = ssm.get_parameter(Name=PARAM_NAME, WithDecryption=False)
        dynamic_string = response['Parameter']['Value']
        html = f"The saved string is {dynamic_string}"
        return {
            'statusCode': 200,
            'body': html
        }
    except ssm.exceptions.ParameterNotFound:
        return {
            'statusCode': 404,
            'body': f'Parameter {PARAM_NAME} not found.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
