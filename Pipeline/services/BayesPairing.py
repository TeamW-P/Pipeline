import requests 

# api-endpoint 
URL = "http://bayespairing:5001/"

def bayespairing_string(arguments):
    payload = {"arguments": arguments}
    files = []
    headers= {}
    response = requests.request("POST", URL + "string", headers=headers, data = payload, files = files)
    return response

def bayespairing_file(arguments, input):
    payload = {"arguments": arguments}
    files = [("input", open(input, "rb"))]    
    headers= {}
    response = requests.request("POST", URL + "file", headers=headers, data = payload, files = files)
    return response
