# uncompyle6 version 3.7.4
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.8.6 (default, Dec 16 2020, 17:27:54)
# [GCC 9.3.0]
# Embedded file name: /home/vpraveen/.cache/dazel/_dazel_vpraveen/216c8b41e526c3295d3b802489ac2034/execroot/ai_infra/bazel-out/k8-fastbuild/bin/magnet/packages/iva/build_wheel.runfiles/ai_infra/iva/detectnet_v2/proto/experiment_pb2.py
# Compiled at: 2021-02-05 20:37:47
# Size of source mod 2**32: 11938 bytes
import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from proto import augmentation_config_pb2 as iva_dot_detectnet__v2_dot_proto_dot_augmentation__config__pb2
from proto import bbox_rasterizer_config_pb2 as iva_dot_detectnet__v2_dot_proto_dot_bbox__rasterizer__config__pb2
from proto import cost_function_config_pb2 as iva_dot_detectnet__v2_dot_proto_dot_cost__function__config__pb2
from proto import dataset_config_pb2 as iva_dot_detectnet__v2_dot_proto_dot_dataset__config__pb2
from proto import evaluation_config_pb2 as iva_dot_detectnet__v2_dot_proto_dot_evaluation__config__pb2
from proto import model_config_pb2 as iva_dot_detectnet__v2_dot_proto_dot_model__config__pb2
from proto import objective_label_filter_pb2 as iva_dot_detectnet__v2_dot_proto_dot_objective__label__filter__pb2
from proto import postprocessing_config_pb2 as iva_dot_detectnet__v2_dot_proto_dot_postprocessing__config__pb2
from proto import training_config_pb2 as iva_dot_detectnet__v2_dot_proto_dot_training__config__pb2
from proto import visualizer_config_pb2 as iva_dot_detectnet__v2_dot_proto_dot_visualizer__config__pb2
from proto import dataset_export_config_pb2 as iva_dot_detectnet__v2_dot_proto_dot_dataset__export__config__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='iva/detectnet_v2/proto/experiment.proto',
    package='',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=(_b(
        '\n\'iva/detectnet_v2/proto/experiment.proto\x1a0iva/detectnet_v2/proto/augmentation_config.proto\x1a3iva/detectnet_v2/proto/bbox_rasterizer_config.proto\x1a1iva/detectnet_v2/proto/cost_function_config.proto\x1a+iva/detectnet_v2/proto/dataset_config.proto\x1a.iva/detectnet_v2/proto/evaluation_config.proto\x1a)iva/detectnet_v2/proto/model_config.proto\x1a3iva/detectnet_v2/proto/objective_label_filter.proto\x1a2iva/detectnet_v2/proto/postprocessing_config.proto\x1a,iva/detectnet_v2/proto/training_config.proto\x1a.iva/detectnet_v2/proto/visualizer_config.proto\x1a2iva/detectnet_v2/proto/dataset_export_config.proto"\x8b\x06\n\nExperiment\x12\x1f\n\x0brandom_seed\x18\x01 \x01(\rR\nrandomSeed\x125\n\x0edataset_config\x18\x02 \x01(\x0b2\x0e.DatasetConfigR\rdatasetConfig\x12D\n\x13augmentation_config\x18\x03 \x01(\x0b2\x13.AugmentationConfigR\x12augmentationConfig\x12J\n\x15postprocessing_config\x18\x04 \x01(\x0b2\x15.PostProcessingConfigR\x14postprocessingConfig\x12/\n\x0cmodel_config\x18\x05 \x01(\x0b2\x0c.ModelConfigR\x0bmodelConfig\x12>\n\x11evaluation_config\x18\x06 \x01(\x0b2\x11.EvaluationConfigR\x10evaluationConfig\x12>\n\x11visualizer_config\x18\x07 \x01(\x0b2\x11.VisualizerConfigR\x10visualizerConfig\x12E\n\x14cost_function_config\x18\x08 \x01(\x0b2\x13.CostFunctionConfigR\x12costFunctionConfig\x128\n\x0ftraining_config\x18\t \x01(\x0b2\x0f.TrainingConfigR\x0etrainingConfig\x12K\n\x16bbox_rasterizer_config\x18\n \x01(\x0b2\x15.BboxRasterizerConfigR\x14bboxRasterizerConfig\x12J\n\x16loss_mask_label_filter\x18\x0b \x01(\x0b2\x15.ObjectiveLabelFilterR\x13lossMaskLabelFilter\x12H\n\x15dataset_export_config\x18\x0c \x03(\x0b2\x14.DatasetExportConfigR\x13datasetExportConfigb\x06proto3'
    )),
    dependencies=[
        iva_dot_detectnet__v2_dot_proto_dot_augmentation__config__pb2.
        DESCRIPTOR,
        iva_dot_detectnet__v2_dot_proto_dot_bbox__rasterizer__config__pb2.
        DESCRIPTOR,
        iva_dot_detectnet__v2_dot_proto_dot_cost__function__config__pb2.
        DESCRIPTOR,
        iva_dot_detectnet__v2_dot_proto_dot_dataset__config__pb2.DESCRIPTOR,
        iva_dot_detectnet__v2_dot_proto_dot_evaluation__config__pb2.DESCRIPTOR,
        iva_dot_detectnet__v2_dot_proto_dot_model__config__pb2.DESCRIPTOR,
        iva_dot_detectnet__v2_dot_proto_dot_objective__label__filter__pb2.
        DESCRIPTOR,
        iva_dot_detectnet__v2_dot_proto_dot_postprocessing__config__pb2.
        DESCRIPTOR,
        iva_dot_detectnet__v2_dot_proto_dot_training__config__pb2.DESCRIPTOR,
        iva_dot_detectnet__v2_dot_proto_dot_visualizer__config__pb2.DESCRIPTOR,
        iva_dot_detectnet__v2_dot_proto_dot_dataset__export__config__pb2.
        DESCRIPTOR
    ])
_EXPERIMENT = _descriptor.Descriptor(
    name='Experiment',
    full_name='Experiment',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(name='random_seed',
                                    full_name='Experiment.random_seed',
                                    index=0,
                                    number=1,
                                    type=13,
                                    cpp_type=3,
                                    label=1,
                                    has_default_value=False,
                                    default_value=0,
                                    message_type=None,
                                    enum_type=None,
                                    containing_type=None,
                                    is_extension=False,
                                    extension_scope=None,
                                    serialized_options=None,
                                    json_name='randomSeed',
                                    file=DESCRIPTOR),
        _descriptor.FieldDescriptor(name='dataset_config',
                                    full_name='Experiment.dataset_config',
                                    index=1,
                                    number=2,
                                    type=11,
                                    cpp_type=10,
                                    label=1,
                                    has_default_value=False,
                                    default_value=None,
                                    message_type=None,
                                    enum_type=None,
                                    containing_type=None,
                                    is_extension=False,
                                    extension_scope=None,
                                    serialized_options=None,
                                    json_name='datasetConfig',
                                    file=DESCRIPTOR),
        _descriptor.FieldDescriptor(name='augmentation_config',
                                    full_name='Experiment.augmentation_config',
                                    index=2,
                                    number=3,
                                    type=11,
                                    cpp_type=10,
                                    label=1,
                                    has_default_value=False,
                                    default_value=None,
                                    message_type=None,
                                    enum_type=None,
                                    containing_type=None,
                                    is_extension=False,
                                    extension_scope=None,
                                    serialized_options=None,
                                    json_name='augmentationConfig',
                                    file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='postprocessing_config',
            full_name='Experiment.postprocessing_config',
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='postprocessingConfig',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(name='model_config',
                                    full_name='Experiment.model_config',
                                    index=4,
                                    number=5,
                                    type=11,
                                    cpp_type=10,
                                    label=1,
                                    has_default_value=False,
                                    default_value=None,
                                    message_type=None,
                                    enum_type=None,
                                    containing_type=None,
                                    is_extension=False,
                                    extension_scope=None,
                                    serialized_options=None,
                                    json_name='modelConfig',
                                    file=DESCRIPTOR),
        _descriptor.FieldDescriptor(name='evaluation_config',
                                    full_name='Experiment.evaluation_config',
                                    index=5,
                                    number=6,
                                    type=11,
                                    cpp_type=10,
                                    label=1,
                                    has_default_value=False,
                                    default_value=None,
                                    message_type=None,
                                    enum_type=None,
                                    containing_type=None,
                                    is_extension=False,
                                    extension_scope=None,
                                    serialized_options=None,
                                    json_name='evaluationConfig',
                                    file=DESCRIPTOR),
        _descriptor.FieldDescriptor(name='visualizer_config',
                                    full_name='Experiment.visualizer_config',
                                    index=6,
                                    number=7,
                                    type=11,
                                    cpp_type=10,
                                    label=1,
                                    has_default_value=False,
                                    default_value=None,
                                    message_type=None,
                                    enum_type=None,
                                    containing_type=None,
                                    is_extension=False,
                                    extension_scope=None,
                                    serialized_options=None,
                                    json_name='visualizerConfig',
                                    file=DESCRIPTOR),
        _descriptor.FieldDescriptor(name='cost_function_config',
                                    full_name='Experiment.cost_function_config',
                                    index=7,
                                    number=8,
                                    type=11,
                                    cpp_type=10,
                                    label=1,
                                    has_default_value=False,
                                    default_value=None,
                                    message_type=None,
                                    enum_type=None,
                                    containing_type=None,
                                    is_extension=False,
                                    extension_scope=None,
                                    serialized_options=None,
                                    json_name='costFunctionConfig',
                                    file=DESCRIPTOR),
        _descriptor.FieldDescriptor(name='training_config',
                                    full_name='Experiment.training_config',
                                    index=8,
                                    number=9,
                                    type=11,
                                    cpp_type=10,
                                    label=1,
                                    has_default_value=False,
                                    default_value=None,
                                    message_type=None,
                                    enum_type=None,
                                    containing_type=None,
                                    is_extension=False,
                                    extension_scope=None,
                                    serialized_options=None,
                                    json_name='trainingConfig',
                                    file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='bbox_rasterizer_config',
            full_name='Experiment.bbox_rasterizer_config',
            index=9,
            number=10,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='bboxRasterizerConfig',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='loss_mask_label_filter',
            full_name='Experiment.loss_mask_label_filter',
            index=10,
            number=11,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='lossMaskLabelFilter',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='dataset_export_config',
            full_name='Experiment.dataset_export_config',
            index=11,
            number=12,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='datasetExportConfig',
            file=DESCRIPTOR)
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=585,
    serialized_end=1364)
_EXPERIMENT.fields_by_name[
    'dataset_config'].message_type = iva_dot_detectnet__v2_dot_proto_dot_dataset__config__pb2._DATASETCONFIG
_EXPERIMENT.fields_by_name[
    'augmentation_config'].message_type = iva_dot_detectnet__v2_dot_proto_dot_augmentation__config__pb2._AUGMENTATIONCONFIG
_EXPERIMENT.fields_by_name[
    'postprocessing_config'].message_type = iva_dot_detectnet__v2_dot_proto_dot_postprocessing__config__pb2._POSTPROCESSINGCONFIG
_EXPERIMENT.fields_by_name[
    'model_config'].message_type = iva_dot_detectnet__v2_dot_proto_dot_model__config__pb2._MODELCONFIG
_EXPERIMENT.fields_by_name[
    'evaluation_config'].message_type = iva_dot_detectnet__v2_dot_proto_dot_evaluation__config__pb2._EVALUATIONCONFIG
_EXPERIMENT.fields_by_name[
    'visualizer_config'].message_type = iva_dot_detectnet__v2_dot_proto_dot_visualizer__config__pb2._VISUALIZERCONFIG
_EXPERIMENT.fields_by_name[
    'cost_function_config'].message_type = iva_dot_detectnet__v2_dot_proto_dot_cost__function__config__pb2._COSTFUNCTIONCONFIG
_EXPERIMENT.fields_by_name[
    'training_config'].message_type = iva_dot_detectnet__v2_dot_proto_dot_training__config__pb2._TRAININGCONFIG
_EXPERIMENT.fields_by_name[
    'bbox_rasterizer_config'].message_type = iva_dot_detectnet__v2_dot_proto_dot_bbox__rasterizer__config__pb2._BBOXRASTERIZERCONFIG
_EXPERIMENT.fields_by_name[
    'loss_mask_label_filter'].message_type = iva_dot_detectnet__v2_dot_proto_dot_objective__label__filter__pb2._OBJECTIVELABELFILTER
_EXPERIMENT.fields_by_name[
    'dataset_export_config'].message_type = iva_dot_detectnet__v2_dot_proto_dot_dataset__export__config__pb2._DATASETEXPORTCONFIG
DESCRIPTOR.message_types_by_name['Experiment'] = _EXPERIMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
Experiment = _reflection.GeneratedProtocolMessageType(
    'Experiment', (_message.Message,),
    dict(DESCRIPTOR=_EXPERIMENT,
         __module__='iva.detectnet_v2.proto.experiment_pb2'))
_sym_db.RegisterMessage(Experiment)
# okay decompiling experiment_pb2.pyc
