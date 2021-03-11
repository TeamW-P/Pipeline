# This is where the "business logic" of the pipeline will live for the TwoAdder service
# basically whatever data manipulation, or combination of service calls we need to do will happen here
# the routing functions will basically call the controller functions to do what needs to be done
from services.RnaMigos import rnamigos_string
import tempfile
import json


class RnaMigos:
 
    @staticmethod
    def rnamigos_string(arguments):
        return rnamigos_string(arguments)
