# uncompyle6 version 3.7.4
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.8.6 (default, Dec 16 2020, 17:27:54)
# [GCC 9.3.0]
# Embedded file name: /home/vpraveen/.cache/dazel/_dazel_vpraveen/216c8b41e526c3295d3b802489ac2034/execroot/ai_infra/bazel-out/k8-fastbuild/bin/magnet/packages/iva/build_wheel.runfiles/ai_infra/iva/detectnet_v2/proto/dataset_export_config_pb2.py
# Compiled at: 2021-02-05 20:37:47
# Size of source mod 2**32: 13301 bytes
import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from proto import kitti_config_pb2 as iva_dot_detectnet__v2_dot_proto_dot_kitti__config__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='iva/detectnet_v2/proto/dataset_export_config.proto',
    package='',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=(_b(
        '\n2iva/detectnet_v2/proto/dataset_export_config.proto\x1a)iva/detectnet_v2/proto/kitti_config.proto"\x89\x07\n\x13DatasetExportConfig\x12/\n\x0ckitti_config\x18\x02 \x01(\x0b2\x0c.KITTIConfigR\x0bkittiConfig\x12_\n\x16sample_modifier_config\x18\x05 \x01(\x0b2).DatasetExportConfig.SampleModifierConfigR\x14sampleModifierConfig\x120\n\x14image_directory_path\x18\x06 \x01(\tR\x12imageDirectoryPath\x1a\xad\x05\n\x14SampleModifierConfig\x12C\n\x1efilter_samples_containing_only\x18\x01 \x03(\tR\x1bfilterSamplesContainingOnly\x126\n\x17dominant_target_classes\x18\x02 \x03(\tR\x15dominantTargetClasses\x12\x8f\x01\n\x1eminimum_target_class_imbalance\x18\x03 \x03(\x0b2J.DatasetExportConfig.SampleModifierConfig.MinimumTargetClassImbalanceEntryR\x1bminimumTargetClassImbalance\x12%\n\x0enum_duplicates\x18\x04 \x01(\rR\rnumDuplicates\x120\n\x14max_training_samples\x18\x05 \x01(\rR\x12maxTrainingSamples\x12\x8d\x01\n\x1esource_to_target_class_mapping\x18\x06 \x03(\x0b2I.DatasetExportConfig.SampleModifierConfig.SourceToTargetClassMappingEntryR\x1asourceToTargetClassMapping\x1aN\n MinimumTargetClassImbalanceEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x02R\x05value:\x028\x01\x1aM\n\x1fSourceToTargetClassMappingEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01b\x06proto3'
    )),
    dependencies=[
        iva_dot_detectnet__v2_dot_proto_dot_kitti__config__pb2.DESCRIPTOR
    ])
_DATASETEXPORTCONFIG_SAMPLEMODIFIERCONFIG_MINIMUMTARGETCLASSIMBALANCEENTRY = _descriptor.Descriptor(
    name='MinimumTargetClassImbalanceEntry',
    full_name=
    'DatasetExportConfig.SampleModifierConfig.MinimumTargetClassImbalanceEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key',
            full_name=
            'DatasetExportConfig.SampleModifierConfig.MinimumTargetClassImbalanceEntry.key',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=(_b('').decode('utf-8')),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='key',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='value',
            full_name=
            'DatasetExportConfig.SampleModifierConfig.MinimumTargetClassImbalanceEntry.value',
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=(float(0)),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='value',
            file=DESCRIPTOR)
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=(_b('8\x01')),
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=846,
    serialized_end=924)
_DATASETEXPORTCONFIG_SAMPLEMODIFIERCONFIG_SOURCETOTARGETCLASSMAPPINGENTRY = _descriptor.Descriptor(
    name='SourceToTargetClassMappingEntry',
    full_name=
    'DatasetExportConfig.SampleModifierConfig.SourceToTargetClassMappingEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key',
            full_name=
            'DatasetExportConfig.SampleModifierConfig.SourceToTargetClassMappingEntry.key',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=(_b('').decode('utf-8')),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='key',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='value',
            full_name=
            'DatasetExportConfig.SampleModifierConfig.SourceToTargetClassMappingEntry.value',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=(_b('').decode('utf-8')),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='value',
            file=DESCRIPTOR)
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=(_b('8\x01')),
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=926,
    serialized_end=1003)
_DATASETEXPORTCONFIG_SAMPLEMODIFIERCONFIG = _descriptor.Descriptor(
    name='SampleModifierConfig',
    full_name='DatasetExportConfig.SampleModifierConfig',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='filter_samples_containing_only',
            full_name=
            'DatasetExportConfig.SampleModifierConfig.filter_samples_containing_only',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='filterSamplesContainingOnly',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='dominant_target_classes',
            full_name=
            'DatasetExportConfig.SampleModifierConfig.dominant_target_classes',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='dominantTargetClasses',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='minimum_target_class_imbalance',
            full_name=
            'DatasetExportConfig.SampleModifierConfig.minimum_target_class_imbalance',
            index=2,
            number=3,
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
            json_name='minimumTargetClassImbalance',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='num_duplicates',
            full_name='DatasetExportConfig.SampleModifierConfig.num_duplicates',
            index=3,
            number=4,
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
            json_name='numDuplicates',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='max_training_samples',
            full_name=
            'DatasetExportConfig.SampleModifierConfig.max_training_samples',
            index=4,
            number=5,
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
            json_name='maxTrainingSamples',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='source_to_target_class_mapping',
            full_name=
            'DatasetExportConfig.SampleModifierConfig.source_to_target_class_mapping',
            index=5,
            number=6,
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
            json_name='sourceToTargetClassMapping',
            file=DESCRIPTOR)
    ],
    extensions=[],
    nested_types=[
        _DATASETEXPORTCONFIG_SAMPLEMODIFIERCONFIG_MINIMUMTARGETCLASSIMBALANCEENTRY,
        _DATASETEXPORTCONFIG_SAMPLEMODIFIERCONFIG_SOURCETOTARGETCLASSMAPPINGENTRY
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=318,
    serialized_end=1003)
_DATASETEXPORTCONFIG = _descriptor.Descriptor(
    name='DatasetExportConfig',
    full_name='DatasetExportConfig',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='kitti_config',
            full_name='DatasetExportConfig.kitti_config',
            index=0,
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
            json_name='kittiConfig',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='sample_modifier_config',
            full_name='DatasetExportConfig.sample_modifier_config',
            index=1,
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
            json_name='sampleModifierConfig',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='image_directory_path',
            full_name='DatasetExportConfig.image_directory_path',
            index=2,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=(_b('').decode('utf-8')),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='imageDirectoryPath',
            file=DESCRIPTOR)
    ],
    extensions=[],
    nested_types=[_DATASETEXPORTCONFIG_SAMPLEMODIFIERCONFIG],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=98,
    serialized_end=1003)
_DATASETEXPORTCONFIG_SAMPLEMODIFIERCONFIG_MINIMUMTARGETCLASSIMBALANCEENTRY.containing_type = _DATASETEXPORTCONFIG_SAMPLEMODIFIERCONFIG
_DATASETEXPORTCONFIG_SAMPLEMODIFIERCONFIG_SOURCETOTARGETCLASSMAPPINGENTRY.containing_type = _DATASETEXPORTCONFIG_SAMPLEMODIFIERCONFIG
_DATASETEXPORTCONFIG_SAMPLEMODIFIERCONFIG.fields_by_name[
    'minimum_target_class_imbalance'].message_type = _DATASETEXPORTCONFIG_SAMPLEMODIFIERCONFIG_MINIMUMTARGETCLASSIMBALANCEENTRY
_DATASETEXPORTCONFIG_SAMPLEMODIFIERCONFIG.fields_by_name[
    'source_to_target_class_mapping'].message_type = _DATASETEXPORTCONFIG_SAMPLEMODIFIERCONFIG_SOURCETOTARGETCLASSMAPPINGENTRY
_DATASETEXPORTCONFIG_SAMPLEMODIFIERCONFIG.containing_type = _DATASETEXPORTCONFIG
_DATASETEXPORTCONFIG.fields_by_name[
    'kitti_config'].message_type = iva_dot_detectnet__v2_dot_proto_dot_kitti__config__pb2._KITTICONFIG
_DATASETEXPORTCONFIG.fields_by_name[
    'sample_modifier_config'].message_type = _DATASETEXPORTCONFIG_SAMPLEMODIFIERCONFIG
DESCRIPTOR.message_types_by_name['DatasetExportConfig'] = _DATASETEXPORTCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
DatasetExportConfig = _reflection.GeneratedProtocolMessageType(
    'DatasetExportConfig', (_message.Message,),
    dict(SampleModifierConfig=(_reflection.GeneratedProtocolMessageType(
        'SampleModifierConfig', (_message.Message,),
        dict(MinimumTargetClassImbalanceEntry=(
            _reflection.GeneratedProtocolMessageType(
                'MinimumTargetClassImbalanceEntry', (_message.Message,),
                dict(
                    DESCRIPTOR=
                    _DATASETEXPORTCONFIG_SAMPLEMODIFIERCONFIG_MINIMUMTARGETCLASSIMBALANCEENTRY,
                    __module__='iva.detectnet_v2.proto.dataset_export_config_pb2'
                ))),
             SourceToTargetClassMappingEntry=
             (_reflection.GeneratedProtocolMessageType(
                 'SourceToTargetClassMappingEntry', (_message.Message,),
                 dict(
                     DESCRIPTOR=
                     _DATASETEXPORTCONFIG_SAMPLEMODIFIERCONFIG_SOURCETOTARGETCLASSMAPPINGENTRY,
                     __module__=
                     'iva.detectnet_v2.proto.dataset_export_config_pb2'))),
             DESCRIPTOR=_DATASETEXPORTCONFIG_SAMPLEMODIFIERCONFIG,
             __module__='iva.detectnet_v2.proto.dataset_export_config_pb2'))),
         DESCRIPTOR=_DATASETEXPORTCONFIG,
         __module__='iva.detectnet_v2.proto.dataset_export_config_pb2'))
_sym_db.RegisterMessage(DatasetExportConfig)
_sym_db.RegisterMessage(DatasetExportConfig.SampleModifierConfig)
_sym_db.RegisterMessage(
    DatasetExportConfig.SampleModifierConfig.MinimumTargetClassImbalanceEntry)
_sym_db.RegisterMessage(
    DatasetExportConfig.SampleModifierConfig.SourceToTargetClassMappingEntry)
_DATASETEXPORTCONFIG_SAMPLEMODIFIERCONFIG_MINIMUMTARGETCLASSIMBALANCEENTRY._options = None
_DATASETEXPORTCONFIG_SAMPLEMODIFIERCONFIG_SOURCETOTARGETCLASSMAPPINGENTRY._options = None
# okay decompiling dataset_export_config_pb2.pyc
