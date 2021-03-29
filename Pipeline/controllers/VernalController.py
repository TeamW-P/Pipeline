# This is where the "business logic" of the pipeline will live for the ThreeAdder service
# basically whatever data manipulation, or combination of service calls we need to do will happen here
# the routing functions will basically call the controller functions to do what needs to be done
from services.Vernal import *


class Vernal:

    @staticmethod
    def vernal_similarity_function(arguments):
        '''
        Calls the VeRNAl service (for use by individual endpoint)

        :param arguments: a dictionary containing vernal arguments
        :returns: the output of the VeRNAl service
        '''
        return vernal_similarity_function(arguments)

    @staticmethod
    def vernal_similarity_function(representative_graphs, dataset):
        '''
        Calls the VeRNAl service (for use by pipeline)

        :param representative_graphs: graphs to process
        :param dataset: the dataset to use
        :returns: the output of the VeRNAl service
        '''
        payload = {"graphs": str(representative_graphs), "dataset": dataset}
        return vernal_similarity_function(payload)
