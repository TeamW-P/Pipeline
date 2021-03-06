import requests 
import json

# api-endpoint
URL = "http://0.0.0.0:5002/" 


def rnamigos_string(payload):
    '''
    Makes a call to the RnaMigos endpoint

    :param payload: the payload to send
    :return: the raw response from RnaMigos
    '''
    files = []
    headers = {}
    response = requests.request(
        "POST", URL + "rnamigos-string", headers=headers, data=payload, files=files)
    return response
