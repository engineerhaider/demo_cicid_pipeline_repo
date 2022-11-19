import json
import hashlib


def lambda_handler(event, context):
    """ get hash """
    print(event)
    body = json.loads(event.get('body',{}))
   
    pass_str = body.get('password', '')
    
    print('event   ', event)
    print('pass_str   ', pass_str)
    
    result = hashlib.md5(pass_str.encode())  # nosec CWE-327
    print('hash ', result.hexdigest())
    
    return {
        'statusCode': 200,
        'body': result.hexdigest()
    }
