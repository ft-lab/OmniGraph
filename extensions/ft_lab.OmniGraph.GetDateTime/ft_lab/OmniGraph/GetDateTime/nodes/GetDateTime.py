"""
Get date time.
"""
import numpy as np
import omni.ext
import datetime

class GetDateTime:
    @staticmethod
    def compute(db) -> bool:
        try:
            # Get current date and time.
            now = datetime.datetime.now()
            db.outputs.year   = now.year
            db.outputs.month  = now.month
            db.outputs.day    = now.day
            db.outputs.hour   = now.hour
            db.outputs.minute = now.minute
            db.outputs.second = now.second

        except TypeError as error:
            db.log_error(f"Processing failed : {error}")
            return False
    
        return True


