import unittest
import json
import os
from .constants.TestPayloads import *
from .constants.TestEnvironment import *
from .utils.MockResponse import *
# relative paths refuse to work because Python is terrible!
from app import app
from mock import patch, Mock
import io

CURRENT_DIRECTORY = os.path.dirname(__file__)

# NOTE: Results here can be considered determnistic but note that dataset changes mean that the responses also need to be changed.
# NOTE: For boolean based comparisons, we still use assertEquals so there is no need to update code in the case of a new response (i.e. you only need to change the expected response JSONs)


class GraphRetrievalTests(unittest.TestCase):
    '''
    Implements unit testing for the graph retrieval endpoint.
    '''

    def setUp(self):
        self.app = app.test_client()

    @patch('requests.request')
    def test_succesful_request(self, mock_get):
        '''
        Tests for a successful run of graph retrieval.
        '''
        with open(os.path.join(CURRENT_DIRECTORY, "responses/mock_responses/RESPONSE_GRAPH_RETRIEVAL_SUCCESS.json")) as f:
            mock_response = json.load(f)
        f.close()

        payload = {}
        headers = {}
        url = f"{GRAPH_RETRIEVAL_URL}?{GRAPH_RETRIEVAL_DATASET_KEY}={ALL_DATASET_NAME}&{GRAPH_RETRIEVAL_MODULES_KEY}={GRAPH_RETRIEVAL_VALID_MODULES}"

        mock_get.return_value = MockResponse(mock_response, 200)

        response = self.app.get(
            url, headers=headers, data=payload)

        with open(os.path.join(CURRENT_DIRECTORY, "responses/responses/GRAPH_RETRIEVAL_SUCCESS.json")) as f:
            expected_response = json.load(f)
        f.close()

        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_response, response.json)

    @patch('requests.request')
    def test_service_failure(self, mock_get):
        '''
        Tests for a run of graph retrieval where the service returns a failure.
        '''
        with open(os.path.join(CURRENT_DIRECTORY, "responses/mock_responses/RESPONSE_GRAPH_RETRIEVAL_ERROR.json")) as f:
            mock_response = json.load(f)
        f.close()

        payload = {}
        headers = {}
        # payload is irrelevant since we are mocking a failure anyways
        url = f"{GRAPH_RETRIEVAL_URL}?{GRAPH_RETRIEVAL_DATASET_KEY}={ALL_DATASET_NAME}&{GRAPH_RETRIEVAL_MODULES_KEY}={GRAPH_RETRIEVAL_VALID_MODULES}"

        mock_get.return_value = MockResponse(mock_response, 400)

        response = self.app.get(
            url, headers=headers, data=payload)

        self.assertEqual(400, response.status_code)

    def test_failure_no_arguments(self):
        '''
        Tests for a failure run of graph retrieval where no arguments are provided.
        '''
        payload = {}
        headers = {}

        response = self.app.get(
            GRAPH_RETRIEVAL_URL, headers=headers, data=payload)

        self.assertEqual(400, response.status_code)
