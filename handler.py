import json


def hello(event, context):
    name = event.get("queryStringParameters", {}).get("name", "stranger")
    body = {
        "message": "Hello, {}. This is your Python Lambda function executed by Serverless Framework!".format(name),
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
