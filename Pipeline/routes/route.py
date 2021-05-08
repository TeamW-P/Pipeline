from flask import jsonify, abort, Blueprint, request, make_response
from controllers.BayesPairingController import BayesPairing
from controllers.RnaMigosController import RnaMigos
from controllers.VernalController import Vernal
from controllers.PipelineController import Pipeline
import json
from . import routes


@routes.route('/pipeline-file', methods=['POST'])
def pipeline_file():
    '''
    Represents the pipeline endpoint for file input.

    :returns: jsonified pipeline output consisting of BayesPairing, VeRNal and RNAMigos output
    '''
    try:
        if ("bp_input" not in request.files):
            raise Exception("Did not receive an input file for BayesPairing")

        code, result = Pipeline.pipeline_file(request.form, request.files)
        if (code == 200):
            return jsonify(result)

    except Exception as e:
        abort(400, "Pipeline failed to process data. Please check your inputs. Error: " + str(e))

    abort(code, result.get("error"))


@routes.route('/pipeline-string', methods=['POST'])
def pipeline_string():
    '''
    Represents the pipeline endpoint for string input.

    :returns: jsonified pipeline output consisting of BayesPairing, VeRNal and RNAMigos output
    '''
    try:
        if ("sequence" not in request.form):
            raise Exception("Did not receive arguments for BayesPairing.")

        code, result = Pipeline.pipeline_string(request.form, request.files)
        if (code == 200):
            return jsonify(result)

    except Exception as e:
        abort(400, "Pipeline failed to process data. Please check your inputs. Error: " + str(e))

    abort(code, result.get("error"))


@routes.route('/graphs', methods=['GET'])
def get_graphs_per_module():
    '''
    Retrievies representative graphs given a list of modules.

    :returns: jsonified output containing a graph for each module
    '''
    try:
        if "modules" not in request.args:
            raise Exception("Did not receive any modules.")

        modules = request.args.get("modules", type = str)
        dataset = request.args.get("dataset", default = "ALL", type = str)

        result = BayesPairing.get_graphs_per_module(modules, dataset)

        if (result):
            return result.json()

    except Exception as e:
        abort(400, "Failed to retrieve representative graphs. Please check your inputs. Error: " + str(e))

    abort(result.status_code, result.json().get("error"))


@routes.route('/module-info', methods=['GET'])
def get_module_info():
    '''
    Retrievies module info for a given list of modules.

    :returns: jsonified output containing module information per module.
    '''
    try:
        if "modules" not in request.args:
            raise Exception("Did not receive any modules.")
        
        modules = request.args.get("modules", type = str)
        dataset = request.args.get("dataset", default = "ALL", type = str)

        result = BayesPairing.get_module_info(modules, dataset)
        if (result):
            return result.json()

    except Exception as e:
        abort(400, "Failed to retrieve representative graphs. Please check your inputs. Error: " + str(e))

    abort(result.status_code, result.json().get("error"))

@routes.route('/rnamigos-string', methods=['POST'])
def rnamigos_string():
    '''
    For future use cases: Represents the RnaMigos endpoint for string input.

    :returns: RnaMigos output
    '''
    try:
        if not "graphs" not in request.form:
            raise Exception("Did not receive any arguments.")

        result = RnaMigos.rnamigos_string(request.form["graphs"])
        if (result):
            return result.json()

    except Exception as e:
        abort(400, "RnaMigos failed to process data. Error: " + str(e))

    abort(result.status_code, result.json().get("error"))


@routes.route('/vernal', methods=['POST'])
def vernal_similarity_function():
    '''
    For future use cases: Given graphs, retrieve similar motifs.

    :returns: similar motifs
    '''
    try:
        if ("graphs" not in request.form):
            raise Exception("Did not receive any arguments.")

        result = Vernal.vernal_similarity_function(request.form.to_dict())

        if (result):
            return result.json()

    except Exception as e:
        abort(400, "Vernal encountered an error while processing data: " + str(e))

    abort(result.status_code, result.json().get("error"))
