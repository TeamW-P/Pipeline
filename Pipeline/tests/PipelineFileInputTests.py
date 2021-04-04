import unittest
import json
import os
from .constants.TestPayloads import *
from .constants.TestEnvironment import *
# relative paths refuse to work because Python is terrible!
from app import app
import io
from mock import patch, Mock
import json

CURRENT_DIRECTORY = os.path.dirname(__file__)

# IMPORTANT NOTE: BP Results are not deterministic. To that effect, these tests validate the existence of keys and whether responses are successful or a failure
# NOTE: For boolean based comparisons, we still use assertEquals so there is no need to update code in the case of a new response (i.e. you only need to change the expected response JSONs)

class PipelineFileInputTests(unittest.TestCase):
    '''
    Implements unit testing for the file input endpoint.
    '''

    def setUp(self):
        self.app = app.test_client()

    @patch('requests.request')
    def test_success_file_all(self, mock_post):
        '''
        Tests for a successful pipeline run where all 3 tools are run (file input)
        '''
        with open(os.path.join(CURRENT_DIRECTORY, "responses/mock_responses/RESPONSE_BP_FILE.json")) as f:
            bp_response = json.load(f)
        f.close()
        with open(os.path.join(CURRENT_DIRECTORY, "responses/mock_responses/RESPONSE_PIPELINE_FILE_RNAMIGOS.json")) as f:
            rnamigos_response = json.load(f)
        f.close()
        with open(os.path.join(CURRENT_DIRECTORY, "responses/mock_responses/RESPONSE_PIPELINE_FILE_VERNAL.json")) as f:
            vernal_response = json.load(f)
        f.close()

        # use side effect when you need to mock multiple calls
        # in-order of calls
        mock_post.side_effect = [self.MockResponse(bp_response, 200), self.MockResponse(
            rnamigos_response, 200), self.MockResponse(vernal_response, 200)]

        payload = FILE_INPUT_FULL
        headers = {}

        with open(os.path.join(CURRENT_DIRECTORY, "data/INPUT_SEQUENCE.fa"), mode="rb") as f:
            payload["bp_input"] = f
            response = self.app.post(
                PL_FILE_URL, content_type='multipart/form-data', headers=headers, data=payload)
        f.close()

        with open(os.path.join(CURRENT_DIRECTORY, "responses/responses/PIPELINE_FILE_SUCCESS.json")) as f:
            expected_response = json.load(f)
        f.close()

        self.assertEqual(200, response.status_code)
        self.compare_core(expected_response, response.json)
        self.assertTrue("similar_motifs" in response.json)
        self.assertTrue("rnamigos_result" in response.json)

    @patch('requests.request')
    def test_success_file_bp_only(self, mock_post):
        '''
        Tests for a successful pipeline run where only BP is run (file input)
        '''
        with open(os.path.join(CURRENT_DIRECTORY, "responses/mock_responses/RESPONSE_BP_FILE.json")) as f:
            bp_response = json.load(f)
        f.close()

        mock_post.return_value = self.MockResponse(bp_response, 200)

        payload = FILE_INPUT_BP_ONLY
        headers = {}

        with open(os.path.join(CURRENT_DIRECTORY, "data/INPUT_SEQUENCE.fa"), mode="rb") as f:
            payload["bp_input"] = f
            response = self.app.post(
                PL_FILE_URL, content_type='multipart/form-data', headers=headers, data=payload)
        f.close()

        with open(os.path.join(CURRENT_DIRECTORY, "responses/responses/PIPELINE_FILE_BP_ONLY.json")) as f:
            expected_response = json.load(f)
        f.close()

        self.assertEqual(200, response.status_code)
        self.compare_core(expected_response, response.json)
        self.assertTrue("similar_motifs" not in response.json)
        self.assertTrue("rnamigos_result" not in response.json)

    @patch('requests.request')
    def test_success_file_no_vernal(self, mock_post):
        '''
        Tests for a successful pipeline run where VeRNAl is not run (file input)
        '''
        with open(os.path.join(CURRENT_DIRECTORY, "responses/mock_responses/RESPONSE_BP_FILE.json")) as f:
            bp_response = json.load(f)
        f.close()

        with open(os.path.join(CURRENT_DIRECTORY, "responses/mock_responses/RESPONSE_PIPELINE_FILE_RNAMIGOS.json")) as f:
            rnamigos_response = json.load(f)
        f.close()

        mock_post.side_effect = [self.MockResponse(bp_response, 200), self.MockResponse(
            rnamigos_response, 200)]

        payload = FILE_INPUT_NO_VERNAL
        headers = {}

        with open(os.path.join(CURRENT_DIRECTORY, "data/INPUT_SEQUENCE.fa"), mode="rb") as f:
            payload["bp_input"] = f
            response = self.app.post(
                PL_FILE_URL, content_type='multipart/form-data', headers=headers, data=payload)
        f.close()

        with open(os.path.join(CURRENT_DIRECTORY, "responses/responses/PIPELINE_FILE_NO_VERNAL.json")) as f:
            expected_response = json.load(f)
        f.close()

        self.assertEqual(200, response.status_code)
        self.compare_core(expected_response, response.json)
        self.assertTrue("rnamigos_result" in response.json)
        self.assertTrue("similar_motifs" not in response.json)

    @patch('requests.request')
    def test_success_file_no_rnamigos(self, mock_post):
        '''
        Tests for a successful pipeline run where RNAmigos is not run (file input)
        '''
        with open(os.path.join(CURRENT_DIRECTORY, "responses/mock_responses/RESPONSE_BP_FILE.json")) as f:
            bp_response = json.load(f)
        f.close()
        with open(os.path.join(CURRENT_DIRECTORY, "responses/mock_responses/RESPONSE_PIPELINE_FILE_VERNAL.json")) as f:
            vernal_response = json.load(f)
        f.close()

        mock_post.side_effect = [self.MockResponse(bp_response, 200), self.MockResponse(
            vernal_response, 200)]

        payload = FILE_INPUT_NO_RNAMIGOS
        headers = {}

        with open(os.path.join(CURRENT_DIRECTORY, "data/INPUT_SEQUENCE.fa"), mode="rb") as f:
            payload["bp_input"] = f
            response = self.app.post(
                PL_FILE_URL, content_type='multipart/form-data', headers=headers, data=payload)
        f.close()

        with open(os.path.join(CURRENT_DIRECTORY, "responses/responses/PIPELINE_FILE_NO_RNAMIGOS.json")) as f:
            expected_response = json.load(f)
        f.close()

        self.assertEqual(200, response.status_code)
        self.compare_core(expected_response, response.json)
        self.assertTrue("rnamigos_result" not in response.json)
        self.assertTrue("similar_motifs" in response.json)

    @patch('requests.request')
    def test_failure_bp(self, mock_post):
        '''
        Tests for a failure case where a failure occurred in BayesPairing
        '''
        with open(os.path.join(CURRENT_DIRECTORY, "responses/mock_responses/RESPONSE_BP_ERROR.json")) as f:
            bp_response = json.load(f)
        f.close()

        mock_post.return_value = self.MockResponse(bp_response, 400)

        payload = FILE_INPUT_FULL
        headers = {}

        with open(os.path.join(CURRENT_DIRECTORY, "data/INVALID_FASTA.fa"), mode="rb") as f:
            payload["bp_input"] = f
            response = self.app.post(
                PL_FILE_URL, content_type='multipart/form-data', headers=headers, data=payload)
        f.close()
        
        self.assertEqual(400, response.status_code)

    @patch('requests.request')
    def test_failure_vernal(self, mock_post):
        '''
        Tests for a failure case where a failure occurred in VeRNAl
        '''
        with open(os.path.join(CURRENT_DIRECTORY, "responses/mock_responses/RESPONSE_VERNAL_ERROR.json")) as f:
            vernal_response = json.load(f)
        f.close()

        mock_post.return_value = self.MockResponse(vernal_response, 400)

        payload = FILE_INPUT_FULL
        headers = {}

        with open(os.path.join(CURRENT_DIRECTORY, "data/INPUT_SEQUENCE.fa"), mode="rb") as f:
            payload["bp_input"] = f
            response = self.app.post(
                PL_FILE_URL, content_type='multipart/form-data', headers=headers, data=payload)
        f.close()
        
        self.assertEqual(400, response.status_code)

    @patch('requests.request')
    def test_failure_rnamigos(self, mock_post):
        '''
        Tests for a failure case where a failure occurred in RNAmigos
        '''
        with open(os.path.join(CURRENT_DIRECTORY, "responses/mock_responses/RESPONSE_RNAMIGOS_ERROR.json")) as f:
            rnamigos_response = json.load(f)
        f.close()

        mock_post.return_value = self.MockResponse(rnamigos_response, 400)

        payload = FILE_INPUT_FULL
        headers = {}

        with open(os.path.join(CURRENT_DIRECTORY, "data/INPUT_SEQUENCE.fa"), mode="rb") as f:
            payload["bp_input"] = f
            response = self.app.post(
                PL_FILE_URL, content_type='multipart/form-data', headers=headers, data=payload)
        f.close()
        
        self.assertEqual(400, response.status_code)

    @patch('requests.request')
    def test_failure_no_arguments(self, mock_post):
        '''
        Tests for a failure case where an no arguments are provided
        '''
        with open(os.path.join(CURRENT_DIRECTORY, "responses/mock_responses/RESPONSE_PIPELINE_EMPTY_ARGS_ERROR.json")) as f:
            pipeline_empty_args_response = json.load(f)
        f.close()

        mock_post.return_file = self.MockResponse(pipeline_empty_args_response, 400)
        
        payload = {}
        headers = {}

        response = self.app.post(
            PL_FILE_URL, content_type='multipart/form-data', headers=headers, data=payload)
        
        self.assertEqual(400, response.status_code)

    def compare_core(self, expected, received):
        self.assertEqual("all_hits" in expected, "all_hits" in received)
        self.assertEqual("chefs_choice_struct" in expected,
                         "chefs_choice_struct" in received)

        self.assertEqual("params" in expected, "params" in received)
        self.assertEqual("motif_graphs" not in expected,
                         "motif_graphs" not in received)

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

        def json(self):
            return self.json_data

