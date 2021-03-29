from services.RnaMigos import rnamigos_string
import tempfile
import json


class RnaMigos:

    @staticmethod
    def rnamigos_string(arguments):
        '''
        Processes RnaMigos input before calling its service.

        :param arguments: a dictionary containing RnaMigos arguments
        :returns: the response from the RnaMigos service
        '''
        payload = {"graphs": arguments}
        return rnamigos_string(payload)
