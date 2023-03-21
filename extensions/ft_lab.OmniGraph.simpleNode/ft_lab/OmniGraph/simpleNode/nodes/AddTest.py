"""
Add Test.
"""
import numpy as np
import omni.ext
import math

class AddTest:
    @staticmethod
    def compute(db) -> bool:
        """Compute the outputs from the current input"""
        try:
            a = db.inputs.a
            b = db.inputs.b
            db.outputs.sum = a + b

        except TypeError as error:
            db.log_error(f"Processing failed : {error}")
            return False
    
        return True


