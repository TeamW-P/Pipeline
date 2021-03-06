# this is where we will make HTTP calls to the TwoAdder container
# it'll only be pure http call, as in send the inputs and receive the outputs
# manipulation of that data should be done elsewhere
import requests 
URL = "http://0.0.0.0:5002/" 

def rnamigos(representative_graphs, ligand_Library):
    '''
    Makes a call to the BayesPairing endpoint to retrieve representative graphs

    :param payload: the payload to send
    :return: the raw response from BayesPairing
    '''
    files = [("library", open(ligand_Library, "rb"))]
    data = {"graphs": str(representative_graphs)}
    headers = {}
    response = requests.request(
        "POST", URL + "rnamigos_pipeline", headers=headers, data=data, files=files)
    return response
