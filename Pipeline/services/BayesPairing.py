import requests 

# api-endpoint 
URL = 'http://bayespairing:5001/'

def bayespairing(query_params):
    r = requests.get(url = URL, params = query_params) 
    data = r.json() 
    return data    

