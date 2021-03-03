from services.BayesPairing import bayespairing_string, bayespairing_file
import tempfile

class BayesPairing:

    @staticmethod
    def bayespairing_string(arguments):
        return bayespairing_string(arguments)

    @staticmethod
    def bayespairing_file(arguments, input):
        input.seek(0)
        temp = tempfile.NamedTemporaryFile(suffix = "." + input.filename.rsplit(".", 1)[1])
        temp.write(input.read())
        temp.seek(0)
        result = bayespairing_file(arguments, temp.name)
        temp.close()
        return result