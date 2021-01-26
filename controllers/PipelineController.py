# This is where the "business logic" of the pipeline will live for the TwoAdder service
# basically whatever data manipulation, or combination of service calls we need to do will happen here
# the routing functions will basically call the controller functions to do what needs to be done
from services.OneAdder import adder as oneAdder
from services.TwoAdder import adder as twoAdder
from services.ThreeAdder import adder as threeAdder

class Pipeline:

    @staticmethod
    def additionChain(input):
        try:
            OneResult = str(oneAdder(input)["result"])
            TwoResult = str(twoAdder(OneResult)["result"])
            ThreeResult = threeAdder(TwoResult) #Do not extract, send as JSON
            return ThreeResult
            
        except:
            return 'Invalid Input'

        