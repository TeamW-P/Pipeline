# This is where the "business logic" of the pipeline will live for the TwoAdder service
# basically whatever data manipulation, or combination of service calls we need to do will happen here
# the routing functions will basically call the controller functions to do what needs to be done
from services.RnaMigos import *
import tempfile

class RnaMigos:

    @staticmethod
    def rnamigos_pipeline(representative_graphs, ligand_library):
        ligand_Library.seek(0)
        # store the file temporarily
        temp = tempfile.NamedTemporaryFile(
            suffix="." + ligand_Library.filename.rsplit(".", 1)[1])
        temp.write(ligand_Library.read())
        temp.seek(0)
        result = rnamigos_pipeline(representative_graphs, temp.name)
        temp.close()
        return result