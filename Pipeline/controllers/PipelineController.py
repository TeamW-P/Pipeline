from .BayesPairingController import BayesPairing


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
        rnamigos_library = files.get("rnamigos_library")
        vernal = arguments.get("vernal", default=1, type=int)
        rnamigos = arguments.get("rnamigos", default=1, type=int)

        # TODO, stockholm handling
        if (rnamigos and not rnamigos_library):
            raise Exception(
                "RNAMigos flag is set to true but received no ligand library for RNAMigos.")

        arguments = arguments.to_dict()
        arguments['get_graphs'] = 1
        bp_result = BayesPairing.bayespairing_file(arguments, bp_input)

        # if we have an error, just return the error response
        if not (bp_result):
            return bp_result.status_code, bp_result.json()

        bp_data = bp_result.json()
        motifs = bp_data.get("motif_graphs")

        # TODO, pipelining

        bp_data.pop("motif_graphs", None)
        return bp_result.status_code, bp_data

    @staticmethod
    def pipeline_string(arguments, files):
        '''
        Processes data for a call to the pipeline and makes calls to the relevant services

        :param arguments: a dictionary containing all arguments for any service
        :param files: a dictionary containing any relevant files (RNAMigos ligand library)
        :returns: a response containing all relevant output
        '''
        rnamigos_library = files.get("rnamigos_library")
        vernal = arguments.get("vernal", default=1, type=int)
        rnamigos = arguments.get("rnamigos", default=1, type=int)

        if (rnamigos and not rnamigos_library):
            raise Exception(
                "RNAMigos flag is set to true but received no ligand library for RNAMigos.")

        arguments = arguments.to_dict()
        arguments['get_graphs'] = 1
        bp_result = BayesPairing.bayespairing_string(arguments)

        # if we have an error, just return the error response
        if not (bp_result):
            return bp_result.status_code, bp_result.json()

        bp_data = bp_result.json()
        motifs = bp_data.get("motif_graphs")

        # TODO, pipelining

        bp_data.pop("motif_graphs", None)
        return bp_result.status_code, bp_data
