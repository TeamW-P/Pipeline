import requests

# api-endpoint
URL = "http://0.0.0.0:5001/"


def bayespairing_string(payload):
    '''
    Makes a call to the BayesPairing endpoint

    :param payload: the payload to send
    :return: the raw response from BayesPairing
    '''
    files = []
    headers = {}
    response = requests.request(
        "POST", URL + "string", headers=headers, data=payload, files=files)
    return response


def bayespairing_file(payload, input):
    '''
    Makes a call to the BayesPairing endpoint

    :param payload: the payload to send
    :param input: a path to a fasta or stockholm file
    :return: the raw response from BayesPairing
    '''
    files = [("bp_input", open(input, "rb"))]
    headers = {}
    response = requests.request(
        "POST", URL + "file", headers=headers, data=payload, files=files)
    return response


def get_graphs_per_module(modules, dataset):
    '''
    Makes a call to the BayesPairing endpoint to retrieve representative graphs

    :param module: a stringified list of modules
    :param dataset: the dataset to retrieve from
    :return: the raw response from BayesPairing
    '''
    files = []
    headers = {}
    payload = {}
    url = f"{URL}graphs?dataset={dataset}&modules={modules}"

    response = requests.request(
        "GET", url, headers=headers, data=payload, files=files)
    return response


def get_module_info(modules, dataset):
    '''
    Makes a call to the BayesPairing endpoint to retrieve module information

    :param module: a stringified list of modules
    :param dataset: the dataset to retrieve from
    :return: the raw response from BayesPairing
    '''
    files = []
    headers = {}
    payload = {}
    url = f"{URL}module-info?dataset={dataset}&modules={modules}"

    response = requests.request(
        "GET", url, headers=headers, data=payload, files=files)
    return response
