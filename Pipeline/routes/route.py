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

@routes.route('/bayespairing_file', methods=['POST'])
def bayespairing_file():
    if "input" not in request.files:
        abort(400, description="Did not receive an input file.")
    if "arguments" not in request.form:
        abort(400, description="Did not receive any arguments.")
    result = BayesPairing.bayespairing_file(request.form.get("arguments"), request.files.get("input"))
    if (result):
        return result.json()
    
    abort(result.status_code, result.json().get("error"))


@routes.route('/bayespairing_string', methods=['POST'])
def bayespairing_string():
    if "arguments" not in request.form:
        abort(400, description="Did not receive any arguments.")
    result = BayesPairing.bayespairing_string(request.form.get("arguments"))
    if (result):
        return result.json()
    
    abort(result.status_code, result.json().get("error"))

@routes.route('/rnamigos', methods=['GET'])
def greeting_rna_migos():
    return RnaMigos.greeting()

@routes.route('/vernal', methods=['GET'])
def greeting_vernal():
    return Vernal.greeting()
