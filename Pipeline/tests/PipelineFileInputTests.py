import unittest
import json
import os
from .constants.TestPayloads import *
from .constants.TestEnvironment import *
# relative paths refuse to work because Python is terrible!
from app import app
import io

CURRENT_DIRECTORY = os.path.dirname(__file__)

# IMPORTANT NOTE: BP Results are not deterministic. To that effect, these tests validate the existence of keys and whether responses are successful or a failure
# NOTE: For boolean based comparisons, we still use assertEquals so there is no need to update code in the case of a new response (i.e. you only need to change the expected response JSONs)

class PipelineStringInputTests(unittest.TestCase):
    '''
    Implements unit testing for the string input endpoint.
    '''

    def setUp(self):
        self.app = app.test_client()

    def test_success_string_all(self):
        '''
        Tests for a successful pipeline run where all 3 tools are run (string input)
        '''

    def test_success_string_bp_only(self):
        '''
        Tests for a successful pipeline run where only BP is run (string input)
        '''

    def test_success_string_no_vernal(self):
        '''
        Tests for a successful pipeline run where VeRNAl is not run (file input)
        '''

    def test_success_string_no_rnamigos(self):
        '''
        Tests for a successful pipeline run where RNAmigos is not run (file input)
        '''

    def test_failure_bp(self):
        '''
        Tests for a failure case where a failure occurred in BayesPairing
        '''

    def test_failure_vernal(self):
        '''
        Tests for a failure case where a failure occurred in VeRNAl
        '''

    def test_failure_rnamigos(self):
        '''
        Tests for a failure case where a failure occurred in RNAmigos
        '''

    def test_failure_no_arguments(self):
        '''
        Tests for a failure case where an no arguments are provided
        '''

    def compare_core(self, expected, received):
        self.assertEqual("all_hits" in expected, "all_hits" in received)
        self.assertEqual("chefs_choice_struct" in expected,
                         "chefs_choice_struct" in received)
        self.assertEqual(expected["input"], received["input"])
        self.assertEqual(expected["params"], received["params"])
