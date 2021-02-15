from flask import jsonify, abort, Blueprint, request
from controllers.BayesPairingController import BayesPairing
from controllers.RnaMigosController import RnaMigos
from controllers.VernalController import Vernal
from controllers.PipelineController import Pipeline
from . import routes

@routes.route('/pipeline', methods=['GET'])
def pipeline():
    # output is either the json output or an error string depending on the status of valid
    valid, output = Pipeline.pipeline(request.args)
    if not (valid):
        abort(400, description=output)

    return output

@routes.route('/bayespairing', methods=['GET'])
def bayespairing():
    # output is either the json output or an error string depending on the status of valid
    valid, output = BayesPairing.bayespairing(request.args)
    if not (valid):
        abort(400, description=output)

    return output

@routes.route('/rnamigos', methods=['GET'])
def greeting_rna_migos():
    return RnaMigos.greeting()

@routes.route('/vernal', methods=['GET'])
def greeting_vernal():
    return BayesPairing.greeting()
