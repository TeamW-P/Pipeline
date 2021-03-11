# this is where we will make HTTP calls to the TwoAdder container
# it'll only be pure http call, as in send the inputs and receive the outputs
# manipulation of that data should be done elsewhere
import requests 
import json
URL = "http://0.0.0.0:5002/" 

def rnamigos_string(payload):
    '''
    Makes a call to the BayesPairing endpoint

    :param payload: the payload to send
    :return: the raw response from BayesPairing
    '''
    data = {"graphs": payload}
    files = []
    headers = {}
    response = requests.request(
        "POST", URL + "rnamigos_pipeline", headers=headers, data=data, files=files)
    return response