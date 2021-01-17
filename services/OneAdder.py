# this is where we will make HTTP calls to the OneAdder container
# it'll only be pure http call, as in send the inputs and receive the outputs
# manipulation of that data should be done elsewhere

# SAMPLE

import requests 
  
# api-endpoint 
URL = 'http://127.0.0.1:5001/'
  
# defining a params dictionary for the parameters to be sent to the API 
# PARAMS = {'address':location} 
  
# sending get request and saving the response as response object 
# r = requests.get(url = URL, params = PARAMS) 

# extracting data in json format 
# data = r.json() 
  
  
# extracting data from response
# result = data['result']
def greeting():
    r = requests.get(url = URL) 
    data = r.json() 
    return data

def adder(input):
    r = requests.get(url = URL + input) 
    data = r.json() 
    return data