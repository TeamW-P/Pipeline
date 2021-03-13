# This is where the "business logic" of the pipeline will live for the ThreeAdder service
# basically whatever data manipulation, or combination of service calls we need to do will happen here
# the routing functions will basically call the controller functions to do what needs to be done
from services.Vernal import *

class Vernal:

    @staticmethod
    def vernalSimilarityFunction(representative_graphs, dataset):
        return vernalSimilarityFunction(representative_graphs, dataset)
