# this is where we will make HTTP calls to the ThreeAdder container
# it'll only be pure http call, as in send the inputs and receive the outputs
# manipulation of that data should be done elsewhere
import requests 
URL = "http://0.0.0.0:5003/"

def vernalSimilarityFunction(representative_graphs, dataset):

    data = {"graphs": str(representative_graphs), "dataset": dataset}
    headers = {}
    files = []
    response = requests.request(
        "POST", URL + "compare-sequence/", headers=headers, data=data, files=files)

    return response
