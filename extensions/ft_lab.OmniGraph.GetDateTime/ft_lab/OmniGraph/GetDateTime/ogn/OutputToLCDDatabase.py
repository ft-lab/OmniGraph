import omni.graph.core as og
import omni.graph.core._omni_graph_core as _og
import omni.graph.tools.ogn as ogn
import numpy
import sys
import traceback
import carb
from typing import Any

class OutputToLCDDatabase(og.Database):
    """Helper class providing simplified access to data on nodes of type ft_lab.OmniGraph.GetDateTime.OutputToDatabaseDatabase

    Class Members:
        node: Node being evaluated

    Attribute Value Properties:
        Inputs:
            inputs.hourNum10Prim
            inputs.hourNum1Prim
            inputs.minuteNum10Prim
            inputs.minuteNum1Prim
            inputs.amPrim
            inputs.pmPrim
            inputs.maskList
            inputs.hour
            inputs.minute
            inputs.second
        Outputs:
    """

    # This is an internal object that provides per-class storage of a per-node data dictionary
    PER_NODE_DATA = {}

    INTERFACE = og.Database._get_interface([
        ('inputs:hourNum10Prim', 'token', 0, 'HourNum10 Prim', 'HourNum10 Prim', {}, True, None, False, ''),
        ('inputs:hourNum1Prim', 'token', 0, 'HourNum1 Prim', 'HourNum1 Prim', {}, True, None, False, ''),
        ('inputs:minuteNum10Prim', 'token', 0, 'MinuteNum10 Prim', 'MinuteNum10 Prim', {}, True, None, False, ''),
        ('inputs:minuteNum1Prim', 'token', 0, 'MinuteNum1 Prim', 'MinuteNum1 Prim', {}, True, None, False, ''),
        ('inputs:amPrim', 'token', 0, 'AM Prim', 'AM Prim', {}, True, None, False, ''),
        ('inputs:pmPrim', 'token', 0, 'PM Prim', 'PM Prim', {}, True, None, False, ''),
        ('inputs:hour', 'int', 0, 'Hour', 'Hour', {}, True, 0, False, ''),
        ('inputs:minute', 'int', 0, 'Minute', 'Minute', {}, True, 0, False, ''),
        ('inputs:second', 'int', 0, 'Second', 'Second', {}, True, 0, False, ''),
    ])

    # ----------------------------------------------------.
    # Processing Input Parameters.
    # ----------------------------------------------------.
    class ValuesForInputs(og.DynamicAttributeAccess):
        LOCAL_PROPERTY_NAMES = {"hourNum10Prim", "hourNum1Prim", "minuteNum10Prim", "minuteNum1Prim", "amPrim", "pmPrim", "hour", "minute", "second"}
        """Helper class that creates natural hierarchical access to input attributes"""
        def __init__(self, node: og.Node, attributes, dynamic_attributes: og.DynamicAttributeInterface):
            """Initialize simplified access for the attribute data"""
            context = node.get_graph().get_default_graph_context()
            super().__init__(context, node, attributes, dynamic_attributes)
            self._batchedReadAttributes = [self._attributes.hourNum10Prim, self._attributes.hourNum1Prim, self._attributes.minuteNum10Prim, self._attributes.minuteNum1Prim, self._attributes.amPrim, self._attributes.pmPrim, self._attributes.hour, self._attributes.minute, self._attributes.second]
            self._batchedReadValues = ["", "", "", "", "", "", 0, 0, 0]

        @property
        def hourNum10Prim(self):
            return self._batchedReadValues[0]

        @hourNum10Prim.setter
        def hourNum10Prim(self, value):
            self._batchedReadValues[0] = value

        @property
        def hourNum1Prim(self):
            return self._batchedReadValues[1]

        @hourNum1Prim.setter
        def hourNum1Prim(self, value):
            self._batchedReadValues[1] = value

        @property
        def minuteNum10Prim(self):
            return self._batchedReadValues[2]

        @minuteNum10Prim.setter
        def minuteNum10Prim(self, value):
            self._batchedReadValues[2] = value

        @property
        def minuteNum1Prim(self):
            return self._batchedReadValues[3]

        @minuteNum1Prim.setter
        def minuteNum1Prim(self, value):
            self._batchedReadValues[3] = value

        @property
        def amPrim(self):
            return self._batchedReadValues[4]

        @amPrim.setter
        def amPrim(self, value):
            self._batchedReadValues[4] = value

        @property
        def pmPrim(self):
            return self._batchedReadValues[5]

        @pmPrim.setter
        def pmPrim(self, value):
            self._batchedReadValues[5] = value

        @property
        def hour(self):
            return self._batchedReadValues[6]

        @hour.setter
        def hour(self, value):
            self._batchedReadValues[6] = value

        @property
        def minute(self):
            return self._batchedReadValues[7]

        @minute.setter
        def minute(self, value):
            self._batchedReadValues[7] = value

        @property
        def second(self):
            return self._batchedReadValues[8]

        @second.setter
        def second(self, value):
            self._batchedReadValues[8] = value

        def __getattr__(self, item: str):
            if item in self.LOCAL_PROPERTY_NAMES:
                return object.__getattribute__(self, item)
            else:
                return super().__getattr__(item)

        def __setattr__(self, item: str, new_value):
            if item in self.LOCAL_PROPERTY_NAMES:
                object.__setattr__(self, item, new_value)
            else:
                super().__setattr__(item, new_value)

        def _prefetch(self):
            readAttributes = self._batchedReadAttributes
            newValues = _og._prefetch_input_attributes_data(readAttributes)
            if len(readAttributes) == len(newValues):
                self._batchedReadValues = newValues

    class ValuesForState(og.DynamicAttributeAccess):
        """Helper class that creates natural hierarchical access to state attributes"""
        def __init__(self, node: og.Node, attributes, dynamic_attributes: og.DynamicAttributeInterface):
            """Initialize simplified access for the attribute data"""
            context = node.get_graph().get_default_graph_context()
            super().__init__(context, node, attributes, dynamic_attributes)

    def __init__(self, node):
        super().__init__(node)

        dynamic_attributes = self.dynamic_attribute_data(node, og.AttributePortType.ATTRIBUTE_PORT_TYPE_INPUT)
        self.inputs = OutputToLCDDatabase.ValuesForInputs(node, self.attributes.inputs, dynamic_attributes)

        dynamic_attributes = self.dynamic_attribute_data(node, og.AttributePortType.ATTRIBUTE_PORT_TYPE_STATE)
        self.state = OutputToLCDDatabase.ValuesForState(node, self.attributes.state, dynamic_attributes)

    # ----------------------------------------------------.
    # Class defining the ABI interface for the node type.
    # ----------------------------------------------------.
    class abi:
        @staticmethod
        def get_node_type():
            get_node_type_function = getattr(OutputToLCDDatabase.NODE_TYPE_CLASS, 'get_node_type', None)
            if callable(get_node_type_function):
                return get_node_type_function()
            return 'ft_lab.OmniGraph.GetDateTime.OutputToLCD'
        
        @staticmethod
        def compute(context, node):
            try:
                per_node_data = OutputToLCDDatabase.PER_NODE_DATA[node.node_id()]
                db = per_node_data.get('_db')
                if db is None:
                    db = OutputToLCDDatabase(node)
                    per_node_data['_db'] = db
            except:
                db = OutputToLCDDatabase(node)

            try:
                compute_function = getattr(OutputToLCDDatabase.NODE_TYPE_CLASS, 'compute', None)
                if callable(compute_function) and compute_function.__code__.co_argcount > 1:
                    return compute_function(context, node)

                db.inputs._prefetch()
                db.inputs._setting_locked = True
                with og.in_compute():
                    return OutputToLCDDatabase.NODE_TYPE_CLASS.compute(db)
            except Exception as error:
                stack_trace = "".join(traceback.format_tb(sys.exc_info()[2].tb_next))
                db.log_error(f'Assertion raised in compute - {error}\n{stack_trace}', add_context=False)
            finally:
                db.inputs._setting_locked = False
                #db.outputs._commit()
            return False

        @staticmethod
        def initialize(context, node):
            OutputToLCDDatabase._initialize_per_node_data(node)
            initialize_function = getattr(OutputToLCDDatabase.NODE_TYPE_CLASS, 'initialize', None)
            if callable(initialize_function):
                initialize_function(context, node)
        @staticmethod
        def release(node):
            release_function = getattr(OutputToLCDDatabase.NODE_TYPE_CLASS, 'release', None)
            if callable(release_function):
                release_function(node)
            OutputToLCDDatabase._release_per_node_data(node)
        @staticmethod
        def update_node_version(context, node, old_version, new_version):
            update_node_version_function = getattr(OutputToLCDDatabase.NODE_TYPE_CLASS, 'update_node_version', None)
            if callable(update_node_version_function):
                return update_node_version_function(context, node, old_version, new_version)
            return False
        @staticmethod
        def initialize_type(node_type):
            initialize_type_function = getattr(OutputToLCDDatabase.NODE_TYPE_CLASS, 'initialize_type', None)
            needs_initializing = True
            if callable(initialize_type_function):
                needs_initializing = initialize_type_function(node_type)
            if needs_initializing:
                node_type.set_metadata(ogn.MetadataKeys.EXTENSION, "ft_lab.OmniGraph.GetDateTime")
                node_type.set_metadata(ogn.MetadataKeys.UI_NAME, "Time output to LCD")
                node_type.set_metadata(ogn.MetadataKeys.CATEGORIES, "examples")
                node_type.set_metadata(ogn.MetadataKeys.DESCRIPTION, "Time output to LCD")
                node_type.set_metadata(ogn.MetadataKeys.LANGUAGE, "Python")

                # Set Icon(svg).
                icon_path = carb.tokens.get_tokens_interface().resolve("${ft_lab.OmniGraph.GetDateTime}")
                icon_path = icon_path + '/' + "data/icons/outputToLCD.svg"
                node_type.set_metadata(ogn.MetadataKeys.ICON_PATH, icon_path)

                OutputToLCDDatabase.INTERFACE.add_to_node_type(node_type)
        @staticmethod
        def on_connection_type_resolve(node):
            on_connection_type_resolve_function = getattr(OutputToLCDDatabase.NODE_TYPE_CLASS, 'on_connection_type_resolve', None)
            if callable(on_connection_type_resolve_function):
                on_connection_type_resolve_function(node)
    NODE_TYPE_CLASS = None
    GENERATOR_VERSION = (1, 17, 2)
    TARGET_VERSION = (2, 65, 4)

    @staticmethod
    def register(node_type_class):
        OutputToLCDDatabase.NODE_TYPE_CLASS = node_type_class
        og.register_node_type(OutputToLCDDatabase.abi, 1)

    @staticmethod
    def deregister():
        og.deregister_node_type("ft_lab.OmniGraph.GetDateTime.OutputToLCD")
