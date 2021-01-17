# This is where the "business logic" of the pipeline will live for the OneAdder service
# basically whatever data manipulation, or combination of service calls we need to do will happen here
# the routing functions will basically call the controller functions to do what needs to be done
from services.OneAdder import *
class OneAdder:

    @staticmethod
    def greeting():
        return greeting()

    @staticmethod
    def adder(input):
        return adder(input)