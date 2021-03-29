# this is where we will make HTTP calls to the ThreeAdder container
# it'll only be pure http call, as in send the inputs and receive the outputs
# manipulation of that data should be done elsewhere
import requests
URL = "http://0.0.0.0:5003/"


def vernal_similarity_function(payload):
    '''
    Calls the VeRNAl service

    :param arguments: a dictionary containing arguments to pass to VeRNAl
    :returns: the response from the VeRNAl service
    '''
    headers = {}
    files = []
    response = requests.request(
        "POST", URL + "compare-sequence/", headers=headers, data=payload, files=files)

    return response
