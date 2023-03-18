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
        a = db.inputs.a
        b = db.inputs.b
        db.outputs.sum = a + b
    
        return True



