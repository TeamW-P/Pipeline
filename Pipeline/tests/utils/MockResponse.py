class MockResponse:
    '''
    A response object similar to Requests Response

    This is mocked instead of setting the values individually or the original Response class because .json() 
    will fail if you simply do mock.return_value = json or use the Response class. As a result, we mock
    the entire object
    '''

    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def __bool__(self):
        # mimics the response object by returning true when a request is successful
        return self.status_code == 200

    def json(self):
        return self.json_data
