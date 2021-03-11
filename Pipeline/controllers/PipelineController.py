from .BayesPairingController import BayesPairing
from .RnaMigosController import RnaMigos
import json

class Pipeline:

    @staticmethod
    def pipeline_file(arguments, files):
        '''
        Processes data for a call to the pipeline and makes calls to the relevant services

        :param arguments: a dictionary containing all arguments for any service
        :param files: a dictionary containing any relevant files including BayesPairing input
        :returns: a response containing all relevant output
        '''
        bp_input = files.get("bp_input")
        vernal = arguments.get("vernal", default=1, type=int)
        rnamigos = arguments.get("rnamigos", default=1, type=int)

        arguments = arguments.to_dict()
        arguments['get_graphs'] = 1
        bp_result = BayesPairing.bayespairing_file(arguments, bp_input)

        # if we have an error, just return the error response
        if not (bp_result):
            return bp_result.status_code, bp_result.json()

        bp_data = bp_result.json()
        motifs = bp_data.get("motif_graphs")
        bp_data.pop("motif_graphs", None)


        if rnamigos == 1:
            rnamigos_result = RnaMigos.rnamigos_string(str(motifs))
            rnamigos_data = rnamigos_result.json()
            bp_data["rnamigos_result"] = rnamigos_data
            return rnamigos_result.status_code, bp_data
        
        return bp_result.status_code, bp_data

    @staticmethod
    def pipeline_string(arguments, files):
        '''
        Processes data for a call to the pipeline and makes calls to the relevant services

        :param arguments: a dictionary containing all arguments for any service
        :param files: a dictionary containing any relevant files (RNAMigos ligand library)
        :returns: a response containing all relevant output
        '''
        vernal = arguments.get("vernal", default=1, type=int)
        rnamigos = arguments.get("rnamigos", default=1, type=int)

        arguments = arguments.to_dict()
        arguments['get_graphs'] = 1
        bp_result = BayesPairing.bayespairing_string(arguments)

        # if we have an error, just return the error response
        if not (bp_result):
            return bp_result.status_code, bp_result.json()

        bp_data = bp_result.json()
        motifs = bp_data.get("motif_graphs")
        bp_data.pop("motif_graphs", None)

        if rnamigos == 1:
            rnamigos_result = RnaMigos.rnamigos_string(str(motifs))
            rnamigos_data = rnamigos_result.json()
            bp_data["rnamigos_result"] = rnamigos_data
            return rnamigos_result.status_code, bp_data
        
        return bp_result.status_code, bp_data
