# routing for the pipeline service will be done here, 
# aka whenever there's a call to the backend, this is where it will be received

# we'll have whatever endpoints we made available in the API here
# the endpoints here will call whichever service needed to get the required info
# then call helper functions to manipulate the data as needed

from flask import jsonify, abort, Blueprint
from controllers.OneAdderController import OneAdder
from controllers.TwoAdderController import TwoAdder
from controllers.ThreeAdderController import ThreeAdder
from . import routes

@routes.route('/oneadder', methods=['GET'])
def greeting_one():
    return OneAdder.greeting()

@routes.route('/oneadder/<num>', methods=['GET'])
def one_adder(num):
    return OneAdder.adder(num)

@routes.route('/twoadder', methods=['GET'])
def greeting_two():
    return TwoAdder.greeting()

@routes.route('/twoadder/<num>', methods=['GET'])
def two_adder(num):
    return TwoAdder.adder(num)

@routes.route('/threeadder', methods=['GET'])
def greeting_three():
    return ThreeAdder.greeting()

@routes.route('/threeadder/<num>', methods=['GET'])
def three_adder(num):
    return ThreeAdder.adder(num)