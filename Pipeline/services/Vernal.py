# this is where we will make HTTP calls to the ThreeAdder container
# it'll only be pure http call, as in send the inputs and receive the outputs
# manipulation of that data should be done elsewhere
import requests 
URL = 'http://vernal:5003/'

def greeting():
    r = requests.get(url = URL) 
    data = r.json() 
    return data
