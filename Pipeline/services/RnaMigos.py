# this is where we will make HTTP calls to the TwoAdder container
# it'll only be pure http call, as in send the inputs and receive the outputs
# manipulation of that data should be done elsewhere
import requests 
URL = "http://rnamigos:5002/" 

def greeting():
    r = requests.get(url = URL) 
    data = r.json() 
    return data
