from services.BayesPairing import *
import tempfile


class BayesPairing:

    @staticmethod
    def bayespairing_string(arguments):
        '''
        Processes BayesPairing input before calling its service.

        :param arguments: a dictionary containing all arguments to BayesPairing
        :returns: the response from the BayesPairing service
        '''
        return bayespairing_string(arguments)

    @staticmethod
    def bayespairing_file(arguments, input):
        '''
        Processes BayesPairing input before calling its service.

        :param arguments: a dictionary containing all arguments to BayesPairing
        :param input: a fasta or stockholm file
        :returns: the response from the BayesPairing service
        '''
        input.seek(0)
        with (tempfile.NamedTemporaryFile(
                suffix="." + input.filename.rsplit(".", 1)[1])) as temp:
            temp.write(input.read())
            temp.seek(0)
            result = bayespairing_file(arguments, temp.name)
        return result

    @staticmethod
    def get_graphs_per_module(modules, dataset):
        '''
        Retrieves representative graphs given a list of modules.

        :param module: a stringified list of modules
        :param dataset: the dataset to retrieve from
        :returns: the response from the BayesPairing service
        '''
        return get_graphs_per_module(modules, dataset)

    @staticmethod
    def get_module_info(modules, dataset):
        '''
        Retrieves module info for a given list of modules.

        :param module: a stringified list of modules
        :param dataset: the dataset to retrieve from
        :returns: the response from the BayesPairing service
        '''
        return get_module_info(modules, dataset)
