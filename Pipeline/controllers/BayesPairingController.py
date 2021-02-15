from services.BayesPairing import bayespairing as run_bayespairing

class BayesPairing:

    @staticmethod
    def bayespairing(arguments):
        try:
            # handle some early checking in-order to avoid making a call to the BayesPairing container
            sequence = arguments.get("sequence", default="", type = str)
            if (sequence == ""):
                return (False, "Did not receive a sequence as an argument.")
                
            secondary_structure = arguments.get("secondary_structure", default="", type = str)
            secondary_structure_infile = arguments.get("secondary_structure_infile", default = 0, type=int)

            # a secondary structure can be provided via a fasta file. This means a string cannot be provided, so verify that only one was received
            if (secondary_structure_infile and secondary_structure != ""):
                return (False, "Indicated that the secondary structure is provided in the fasta file, but also provided a separate structure.")

            return (True, run_bayespairing(arguments))
        except ValueError as e:
            return (False, 'ValueError: Received an invalid argument, log:' + str(e))
