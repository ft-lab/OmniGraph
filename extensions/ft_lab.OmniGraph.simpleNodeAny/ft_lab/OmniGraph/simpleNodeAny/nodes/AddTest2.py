"""
Add Test2.
"""
import numpy as np
import omni.graph.core as og
import omni.ext
import math

class AddTest2:

    # ---------------------------------------------------.
    # Compute the outputs from the current input.
    # ---------------------------------------------------.
    @staticmethod
    def compute(db) -> bool:
        try:
            # Attribute Type for ["numerics"].
            # "aType.base_type" is the following value.
            # og.BaseDataType.INT, og.BaseDataType.INT64, og.BaseDataType.FLOAT, og.BaseDataType.DOUBLE, etc.
            aType = db.inputs.a.type
            bType = db.inputs.b.type
            sumType = db.outputs.sum.type

            # The actual value is "a.value".
            a = db.inputs.a
            b = db.inputs.b

            db.outputs.sum.value = a.value + b.value

        except TypeError as error:
            db.log_error(f"Processing failed : {error}")
            return False

        return True

    # ---------------------------------------------------.
    # Resolves the type of the output based on the types of inputs.
    # This is called after the inputs connection is finalized.
    # ---------------------------------------------------.
    @staticmethod
    def on_connection_type_resolve(node) -> None:
        # Attribute Type for ["numerics"].
        # "aType.base_type" is the following value.
        # og.BaseDataType.INT, og.BaseDataType.INT64, og.BaseDataType.FLOAT, og.BaseDataType.DOUBLE, etc.
        aType = node.get_attribute("inputs:a").get_resolved_type()
        bType = node.get_attribute("inputs:b").get_resolved_type()
        sumType = node.get_attribute("outputs:sum").get_resolved_type()

        # If the type of "outputs:sum" is not specified.
        if (
            aType.base_type != og.BaseDataType.UNKNOWN
            and bType.base_type != og.BaseDataType.UNKNOWN
            and sumType.base_type == og.BaseDataType.UNKNOWN
        ):
            
            # Set the type of "outputs:sum" to the same as "inputs:a".
            og.resolve_fully_coupled(
                [node.get_attribute("inputs:a"), node.get_attribute("outputs:sum")]
            )
