from services.RnaMigos import rnamigos_string
import tempfile
import json


class RnaMigos:
 
    @staticmethod
    def rnamigos_string(arguments):
        '''
        Processes RnaMigos input before calling its service.

        :param arguments: a stringified version of the arguments for RnaMigos
        :returns: the response from the RnaMigos service
        '''
        return rnamigos_string(arguments)
