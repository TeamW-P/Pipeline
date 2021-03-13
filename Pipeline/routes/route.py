from flask import jsonify, abort, Blueprint, request, make_response
from controllers.BayesPairingController import BayesPairing
from controllers.RnaMigosController import RnaMigos
from controllers.VernalController import Vernal
from controllers.PipelineController import Pipeline
from . import routes


@routes.route('/pipeline_file', methods=['POST'])
def pipeline_file():
    '''
    Represents the pipeline endpoint for file input.

    :returns: jsonified pipeline output consisting of BayesPairing, VeRNal and RNAMigos output
    '''
    try:
        if ("bp_input" not in request.files):
            abort("Did not receive an input file for BayesPairing")

        code, result = Pipeline.pipeline_file(request.form, request.files)
        if (code == 200):
            return jsonify(result)

        abort(code, result.get("error"))
    except Exception as e:
        abort(400, "Pipeline failed to process data. Please check your inputs. Error: " + str(e))


@routes.route('/pipeline_string', methods=['POST'])
def pipeline_string():
    '''
    Represents the pipeline endpoint for string input.

    :returns: jsonified pipeline output consisting of BayesPairing, VeRNal and RNAMigos output
    '''
    # TODO: add potential file input for VeRNAl & RNAMigos
    try:
        if ("sequence" not in request.form):
            abort("Did not receive arguments for BayesPairing.")

        code, result = Pipeline.pipeline_string(request.form, request.files)
        if (code == 200):
            return jsonify(result)


        abort(code, result.get("error"))
    except Exception as e:
        abort(400, "Pipeline failed to process data. Please check your inputs. Error: " + str(e))


@routes.route('/bayespairing_file', methods=['POST'])
def bayespairing_file():
    '''
    Represents the BayesPairing endpoint for file input.

    :returns: jsonified BayesPairing output
    '''
    try:
        if "bp_input" not in request.files:
            abort(400, description="Did not receive an input file.")
        if not request.form:
            abort(400, description="Did not receive any arguments.")
        result = BayesPairing.bayespairing_file(
            request.form.to_dict(), request.files.get("bp_input"))
        if (result):
            return result.json()

        abort(result.status_code, result.json().get("error"))
    except Exception as e:
        abort(400, "BayesPairing failed to process data. Please check your inputs. Error: " + str(e))


@routes.route('/bayespairing_string', methods=['POST'])
def bayespairing_string():
    '''
    Represents the BayesPairing endpoint for string input.

    :returns: jsonified BayesPairing output
    '''
    try:
        if not request.form or "sequence" not in request.form:
            abort(400, description="Did not receive any arguments.")
        result = BayesPairing.bayespairing_string(request.form.to_dict())
        if (result):
            return result.json()

        abort(result.status_code, result.json().get("error"))
    except Exception as e:
        abort(400, "BayesPairing failed to process data. Please check your inputs. Error: " + str(e))


@routes.route('/graphs', methods=['POST'])
def get_graphs_per_module():
    '''
    Retrievies representative graphs given a list of modules.

    :returns: jsonified output containing a graph for each module
    '''
    try:
        if "modules" not in request.form:
            abort(400, description="Did not receive any modules.")
        result = BayesPairing.get_graphs_per_module(
            request.form.get("modules"))
        if (result):
            return result.json()

        print(result.json().get("error"))
        abort(result.status_code, result.json().get("error"))
    except Exception as e:
        abort(400, "Failed to retrieve representative graphs. Please check your inputs. Error: " + str(e))


@routes.route('/rnamigos', methods=['GET'])
def greeting_rna_migos():
    return RnaMigos.greeting()

@routes.route('/vernal', methods=['POST'])
def vernal_execution():
    output = ""
    try: 
        output = Vernal.vernalSimilarityFunction(representative_graphs=request.form.get("graphs"), dataset=request.form.get("dataset"))
        print(output.json())
        return str(output.json())
        
        
    except Exception as e:
        abort(400, "Vernal encountered an error while processing data: " + str(e))




