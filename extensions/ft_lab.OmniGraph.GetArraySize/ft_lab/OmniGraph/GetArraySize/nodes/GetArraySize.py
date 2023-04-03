"""
Get array size.
"""
import numpy as np
import omni.graph.core as og
import omni.ext
import math

class GetArraySize:
    # ---------------------------------------------------.
    # Compute the outputs from the current input.
    # ---------------------------------------------------.
    @staticmethod
    def compute(db) -> bool:
        try:
            db.outputs.type = db.inputs.array.type.get_type_name()
            db.outputs.size = db.inputs.array.size

        except TypeError as error:
            db.log_error(f"Processing failed : {error}")
            return False

        return True

