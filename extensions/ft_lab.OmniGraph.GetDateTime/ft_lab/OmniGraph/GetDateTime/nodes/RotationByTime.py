"""
Rotation by time.
"""
import numpy as np
import omni.ext

class RotationByTime:
    @staticmethod
    def compute(db) -> bool:
        try:
            # Calculate clock rotation from seconds.
            if db.inputs.rotationAxis >= 0 and db.inputs.rotationAxis <= 2:
                v = db.outputs.secondRotateXYZ
                v[0] = db.inputs.defaultRotateXYZ[0]
                v[1] = db.inputs.defaultRotateXYZ[1]
                v[2] = db.inputs.defaultRotateXYZ[2]
                v[db.inputs.rotationAxis] = ((float)(db.inputs.second) / 60.0) * 360.0

            # Calculate clock rotation from minutes.
            if db.inputs.rotationAxis >= 0 and db.inputs.rotationAxis <= 2:
                v = db.outputs.minuteRotateXYZ
                v[0] = db.inputs.defaultRotateXYZ[0]
                v[1] = db.inputs.defaultRotateXYZ[1]
                v[2] = db.inputs.defaultRotateXYZ[2]
                v[db.inputs.rotationAxis] = ((float)(db.inputs.minute * 60.0 + db.inputs.second) / (60.0 * 60.0)) * 360.0

            # Calculate clock rotation from hours.
            if db.inputs.rotationAxis >= 0 and db.inputs.rotationAxis <= 2:
                v = db.outputs.hourRotateXYZ
                v[0] = db.inputs.defaultRotateXYZ[0]
                v[1] = db.inputs.defaultRotateXYZ[1]
                v[2] = db.inputs.defaultRotateXYZ[2]
                v[db.inputs.rotationAxis] = ((float)(db.inputs.hour * 60.0 + db.inputs.minute) / (60.0 * 24.0)) * 360.0 * 2.0

        except TypeError as error:
            db.log_error(f"Processing failed : {error}")
            return False
    
        return True


