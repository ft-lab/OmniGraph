import omni.graph.core as og
import omni.graph.core._omni_graph_core as _og
import omni.graph.tools.ogn as ogn
import numpy
import sys
import traceback
import carb
from typing import Any

class GetArraySizeDatabase(og.Database):
    """Helper class providing simplified access to data on nodes of type ft_lab.OmniGraph.GetArraySize.GetArraySize

    Class Members:
        node: Node being evaluated

    Attribute Value Properties:
        Inputs:
            inputs.array
        Outputs:
            outputs.type
            outputs.size
    """

    # This is an internal object that provides per-class storage of a per-node data dictionary
    PER_NODE_DATA = {}

    INTERFACE = og.Database._get_interface([
        ('inputs:array', 'bool[],colord[3][],colord[4][],colorf[3][],colorf[4][],colorh[3][],colorh[4][],double[2][],double[3][],double[4][],double[],float[2][],float[3][],float[4][],float[],frame[4][],half[2][],half[3][],half[4][],half[],int64[],int[2][],int[3][],int[4][],int[],matrixd[3][],matrixd[4][],normald[3][],normalf[3][],normalh[3][],pointd[3][],pointf[3][],pointh[3][],quatd[4][],quatf[4][],quath[4][],texcoordd[2][],texcoordd[3][],texcoordf[2][],texcoordf[3][],texcoordh[2][],texcoordh[3][],timecode[],token[],transform[4][],uchar[],uint64[],uint[],vectord[3][],vectorf[3][],vectorh[3][]', 1, 'Array', 'The array', {}, True, None, False, ''),
        ('outputs:type', 'string', 0, 'Type', 'Array Type', {}, True, None, False, ''),
        ('outputs:size', 'int', 0, 'Size', 'Array Size', {}, True, None, False, ''),
    ])

    # ----------------------------------------------------.
    # Processing Input Parameters.
    # ----------------------------------------------------.
    class ValuesForInputs(og.DynamicAttributeAccess):
        LOCAL_PROPERTY_NAMES = {}
        """Helper class that creates natural hierarchical access to input attributes"""
        def __init__(self, node: og.Node, attributes, dynamic_attributes: og.DynamicAttributeInterface):
            """Initialize simplified access for the attribute data"""
            context = node.get_graph().get_default_graph_context()
            super().__init__(context, node, attributes, dynamic_attributes)
            self._batchedReadAttributes = []
            self._batchedReadValues = []

        @property
        def array(self) -> og.RuntimeAttribute:
            return og.RuntimeAttribute(self._attributes.array.get_attribute_data(), self._context, True)

        @array.setter
        def array(self, value_to_set: Any):
            """Assign another attribute's value to outputs.array"""
            if isinstance(value_to_set, og.RuntimeAttribute):
                self.array.value = value_to_set.value
            else:
                self.array.value = value_to_set

        def _prefetch(self):
            readAttributes = self._batchedReadAttributes
            newValues = _og._prefetch_input_attributes_data(readAttributes)
            if len(readAttributes) == len(newValues):
                self._batchedReadValues = newValues

    # ----------------------------------------------------.
    # Processing Output Parameter.
    # ----------------------------------------------------.
    class ValuesForOutputs(og.DynamicAttributeAccess):
        LOCAL_PROPERTY_NAMES = { "type", "size" }
        """Helper class that creates natural hierarchical access to output attributes"""
        def __init__(self, node: og.Node, attributes, dynamic_attributes: og.DynamicAttributeInterface):
            """Initialize simplified access for the attribute data"""
            context = node.get_graph().get_default_graph_context()
            super().__init__(context, node, attributes, dynamic_attributes)
            self._batchedWriteValues = { }

        @property
        def type(self):
            value = self._batchedWriteValues.get(self._attributes.type)
            if value:
                return value
            else:
                data_view = og.AttributeValueHelper(self._attributes.type)
                return data_view.get()

        @type.setter
        def type(self, value):
            self._batchedWriteValues[self._attributes.type] = value

        @property
        def size(self):
            value = self._batchedWriteValues.get(self._attributes.size)
            if value:
                return value
            else:
                data_view = og.AttributeValueHelper(self._attributes.size)
                return data_view.get()

        @size.setter
        def size(self, value):
            self._batchedWriteValues[self._attributes.size] = value

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

        def _commit(self):
            _og._commit_output_attributes_data(self._batchedWriteValues)
            self._batchedWriteValues = { }

    class ValuesForState(og.DynamicAttributeAccess):
        """Helper class that creates natural hierarchical access to state attributes"""
        def __init__(self, node: og.Node, attributes, dynamic_attributes: og.DynamicAttributeInterface):
            """Initialize simplified access for the attribute data"""
            context = node.get_graph().get_default_graph_context()
            super().__init__(context, node, attributes, dynamic_attributes)

    def __init__(self, node):
        super().__init__(node)

        dynamic_attributes = self.dynamic_attribute_data(node, og.AttributePortType.ATTRIBUTE_PORT_TYPE_INPUT)
        self.inputs = GetArraySizeDatabase.ValuesForInputs(node, self.attributes.inputs, dynamic_attributes)

        dynamic_attributes = self.dynamic_attribute_data(node, og.AttributePortType.ATTRIBUTE_PORT_TYPE_OUTPUT)
        self.outputs = GetArraySizeDatabase.ValuesForOutputs(node, self.attributes.outputs, dynamic_attributes)

        dynamic_attributes = self.dynamic_attribute_data(node, og.AttributePortType.ATTRIBUTE_PORT_TYPE_STATE)
        self.state = GetArraySizeDatabase.ValuesForState(node, self.attributes.state, dynamic_attributes)

    # ----------------------------------------------------.
    # Class defining the ABI interface for the node type.
    # ----------------------------------------------------.
    class abi:
        @staticmethod
        def get_node_type():
            get_node_type_function = getattr(GetArraySizeDatabase.NODE_TYPE_CLASS, 'get_node_type', None)
            if callable(get_node_type_function):
                return get_node_type_function()
            return 'ft_lab.OmniGraph.GetArraySize.GetArraySize'
        
        @staticmethod
        def compute(context, node):
            try:
                per_node_data = GetArraySizeDatabase.PER_NODE_DATA[node.node_id()]
                db = per_node_data.get('_db')
                if db is None:
                    db = GetArraySizeDatabase(node)
                    per_node_data['_db'] = db
            except:
                db = GetArraySizeDatabase(node)

            try:
                compute_function = getattr(GetArraySizeDatabase.NODE_TYPE_CLASS, 'compute', None)
                if callable(compute_function) and compute_function.__code__.co_argcount > 1:
                    return compute_function(context, node)

                db.inputs._prefetch()
                db.inputs._setting_locked = True
                with og.in_compute():
                    return GetArraySizeDatabase.NODE_TYPE_CLASS.compute(db)
            except Exception as error:
                stack_trace = "".join(traceback.format_tb(sys.exc_info()[2].tb_next))
                db.log_error(f'Assertion raised in compute - {error}\n{stack_trace}', add_context=False)
            finally:
                db.inputs._setting_locked = False
                db.outputs._commit()
            return False
        @staticmethod
        def initialize(context, node):
            GetArraySizeDatabase._initialize_per_node_data(node)
            initialize_function = getattr(GetArraySizeDatabase.NODE_TYPE_CLASS, 'initialize', None)
            if callable(initialize_function):
                initialize_function(context, node)
        @staticmethod
        def release(node):
            release_function = getattr(GetArraySizeDatabase.NODE_TYPE_CLASS, 'release', None)
            if callable(release_function):
                release_function(node)
            GetArraySizeDatabase._release_per_node_data(node)
        @staticmethod
        def update_node_version(context, node, old_version, new_version):
            update_node_version_function = getattr(GetArraySizeDatabase.NODE_TYPE_CLASS, 'update_node_version', None)
            if callable(update_node_version_function):
                return update_node_version_function(context, node, old_version, new_version)
            return False
        @staticmethod
        def initialize_type(node_type):
            initialize_type_function = getattr(GetArraySizeDatabase.NODE_TYPE_CLASS, 'initialize_type', None)
            needs_initializing = True
            if callable(initialize_type_function):
                needs_initializing = initialize_type_function(node_type)
            if needs_initializing:
                node_type.set_metadata(ogn.MetadataKeys.EXTENSION, "ft_lab.OmniGraph.GetArraySize")
                node_type.set_metadata(ogn.MetadataKeys.UI_NAME, "Get array size")
                node_type.set_metadata(ogn.MetadataKeys.CATEGORIES, "examples")
                node_type.set_metadata(ogn.MetadataKeys.DESCRIPTION, "Get array size")
                node_type.set_metadata(ogn.MetadataKeys.LANGUAGE, "Python")

                # Set Icon(svg).
                icon_path = carb.tokens.get_tokens_interface().resolve("${ft_lab.OmniGraph.GetArraySize}")
                icon_path = icon_path + '/' + "data/icons/icon.svg"
                node_type.set_metadata(ogn.MetadataKeys.ICON_PATH, icon_path)

                GetArraySizeDatabase.INTERFACE.add_to_node_type(node_type)
        @staticmethod
        def on_connection_type_resolve(node):
            on_connection_type_resolve_function = getattr(GetArraySizeDatabase.NODE_TYPE_CLASS, 'on_connection_type_resolve', None)
            if callable(on_connection_type_resolve_function):
                on_connection_type_resolve_function(node)
    NODE_TYPE_CLASS = None
    GENERATOR_VERSION = (1, 17, 2)
    TARGET_VERSION = (2, 65, 4)

    @staticmethod
    def register(node_type_class):
        GetArraySizeDatabase.NODE_TYPE_CLASS = node_type_class
        og.register_node_type(GetArraySizeDatabase.abi, 1)

    @staticmethod
    def deregister():
        og.deregister_node_type("ft_lab.OmniGraph.GetArraySize.GetArraySize")
