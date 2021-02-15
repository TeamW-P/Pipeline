from .BayesPairingController import BayesPairing

class Pipeline:

    @staticmethod
    def pipeline(arguments):
        try:
            valid, output = BayesPairing.bayespairing(arguments)
            if not (valid):
                return (False, "Failed to complete BayesPairing: %s." % (output))
            # imaginary pipelining
            return (True, output)
        except Exception as e:
            return (False, "Pipeline failed due to an unexpected error: %s." % (str(e)))

        