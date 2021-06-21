# uncompyle6 version 3.7.4
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.8.6 (default, Dec 16 2020, 17:27:54)
# [GCC 9.3.0]
# Embedded file name: /home/vpraveen/.cache/dazel/_dazel_vpraveen/216c8b41e526c3295d3b802489ac2034/execroot/ai_infra/bazel-out/k8-fastbuild/bin/magnet/packages/iva/build_wheel.runfiles/ai_infra/iva/detectnet_v2/proto/dataset_config_pb2.py
# Compiled at: 2021-02-05 20:37:47
# Size of source mod 2**32: 10740 bytes
import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name='iva/detectnet_v2/proto/dataset_config.proto',
    package='',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=(_b(
        '\n+iva/detectnet_v2/proto/dataset_config.proto"\x8a\x01\n\nDataSource\x12%\n\x0etfrecords_path\x18\x01 \x01(\tR\rtfrecordsPath\x120\n\x14image_directory_path\x18\x02 \x01(\tR\x12imageDirectoryPath\x12#\n\rsource_weight\x18\x03 \x01(\x02R\x0csourceWeight"\x95\x04\n\rDatasetConfig\x12.\n\x0cdata_sources\x18\x01 \x03(\x0b2\x0b.DataSourceR\x0bdataSources\x12\'\n\x0fimage_extension\x18\x02 \x01(\tR\x0eimageExtension\x12X\n\x14target_class_mapping\x18\x03 \x03(\x0b2&.DatasetConfig.TargetClassMappingEntryR\x12targetClassMapping\x12)\n\x0fvalidation_fold\x18\x04 \x01(\rH\x00R\x0evalidationFold\x12C\n\x16validation_data_source\x18\x05 \x01(\x0b2\x0b.DataSourceH\x00R\x14validationDataSource\x12G\n\x0fdataloader_mode\x18\x06 \x01(\x0e2\x1e.DatasetConfig.DATALOADER_MODER\x0edataloaderMode\x1aE\n\x17TargetClassMappingEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01";\n\x0fDATALOADER_MODE\x12\x0f\n\x0bMULTISOURCE\x10\x00\x12\n\n\x06LEGACY\x10\x01\x12\x0b\n\x07DEFAULT\x10\x02B\x14\n\x12dataset_split_typeb\x06proto3'
    )))
_DATASETCONFIG_DATALOADER_MODE = _descriptor.EnumDescriptor(
    name='DATALOADER_MODE',
    full_name='DatasetConfig.DATALOADER_MODE',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(name='MULTISOURCE',
                                        index=0,
                                        number=0,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='LEGACY',
                                        index=1,
                                        number=1,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='DEFAULT',
                                        index=2,
                                        number=2,
                                        serialized_options=None,
                                        type=None)
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=641,
    serialized_end=700)
_sym_db.RegisterEnumDescriptor(_DATASETCONFIG_DATALOADER_MODE)
_DATASOURCE = _descriptor.Descriptor(
    name='DataSource',
    full_name='DataSource',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(name='tfrecords_path',
                                    full_name='DataSource.tfrecords_path',
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
                                    json_name='tfrecordsPath',
                                    file=DESCRIPTOR),
        _descriptor.FieldDescriptor(name='image_directory_path',
                                    full_name='DataSource.image_directory_path',
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
                                    json_name='imageDirectoryPath',
                                    file=DESCRIPTOR),
        _descriptor.FieldDescriptor(name='source_weight',
                                    full_name='DataSource.source_weight',
                                    index=2,
                                    number=3,
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
                                    json_name='sourceWeight',
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
    serialized_start=48,
    serialized_end=186)
_DATASETCONFIG_TARGETCLASSMAPPINGENTRY = _descriptor.Descriptor(
    name='TargetClassMappingEntry',
    full_name='DatasetConfig.TargetClassMappingEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key',
            full_name='DatasetConfig.TargetClassMappingEntry.key',
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
            full_name='DatasetConfig.TargetClassMappingEntry.value',
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
    serialized_start=570,
    serialized_end=639)
_DATASETCONFIG = _descriptor.Descriptor(
    name='DatasetConfig',
    full_name='DatasetConfig',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(name='data_sources',
                                    full_name='DatasetConfig.data_sources',
                                    index=0,
                                    number=1,
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
                                    json_name='dataSources',
                                    file=DESCRIPTOR),
        _descriptor.FieldDescriptor(name='image_extension',
                                    full_name='DatasetConfig.image_extension',
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
                                    json_name='imageExtension',
                                    file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='target_class_mapping',
            full_name='DatasetConfig.target_class_mapping',
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
            json_name='targetClassMapping',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(name='validation_fold',
                                    full_name='DatasetConfig.validation_fold',
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
                                    json_name='validationFold',
                                    file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='validation_data_source',
            full_name='DatasetConfig.validation_data_source',
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
            json_name='validationDataSource',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(name='dataloader_mode',
                                    full_name='DatasetConfig.dataloader_mode',
                                    index=5,
                                    number=6,
                                    type=14,
                                    cpp_type=8,
                                    label=1,
                                    has_default_value=False,
                                    default_value=0,
                                    message_type=None,
                                    enum_type=None,
                                    containing_type=None,
                                    is_extension=False,
                                    extension_scope=None,
                                    serialized_options=None,
                                    json_name='dataloaderMode',
                                    file=DESCRIPTOR)
    ],
    extensions=[],
    nested_types=[_DATASETCONFIG_TARGETCLASSMAPPINGENTRY],
    enum_types=[_DATASETCONFIG_DATALOADER_MODE],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name='dataset_split_type',
            full_name='DatasetConfig.dataset_split_type',
            index=0,
            containing_type=None,
            fields=[])
    ],
    serialized_start=189,
    serialized_end=722)
_DATASETCONFIG_TARGETCLASSMAPPINGENTRY.containing_type = _DATASETCONFIG
_DATASETCONFIG.fields_by_name['data_sources'].message_type = _DATASOURCE
_DATASETCONFIG.fields_by_name[
    'target_class_mapping'].message_type = _DATASETCONFIG_TARGETCLASSMAPPINGENTRY
_DATASETCONFIG.fields_by_name[
    'validation_data_source'].message_type = _DATASOURCE
_DATASETCONFIG.fields_by_name[
    'dataloader_mode'].enum_type = _DATASETCONFIG_DATALOADER_MODE
_DATASETCONFIG_DATALOADER_MODE.containing_type = _DATASETCONFIG
_DATASETCONFIG.oneofs_by_name['dataset_split_type'].fields.append(
    _DATASETCONFIG.fields_by_name['validation_fold'])
_DATASETCONFIG.fields_by_name[
    'validation_fold'].containing_oneof = _DATASETCONFIG.oneofs_by_name[
        'dataset_split_type']
_DATASETCONFIG.oneofs_by_name['dataset_split_type'].fields.append(
    _DATASETCONFIG.fields_by_name['validation_data_source'])
_DATASETCONFIG.fields_by_name[
    'validation_data_source'].containing_oneof = _DATASETCONFIG.oneofs_by_name[
        'dataset_split_type']
DESCRIPTOR.message_types_by_name['DataSource'] = _DATASOURCE
DESCRIPTOR.message_types_by_name['DatasetConfig'] = _DATASETCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
DataSource = _reflection.GeneratedProtocolMessageType(
    'DataSource', (_message.Message,),
    dict(DESCRIPTOR=_DATASOURCE,
         __module__='iva.detectnet_v2.proto.dataset_config_pb2'))
_sym_db.RegisterMessage(DataSource)
DatasetConfig = _reflection.GeneratedProtocolMessageType(
    'DatasetConfig', (_message.Message,),
    dict(TargetClassMappingEntry=(_reflection.GeneratedProtocolMessageType(
        'TargetClassMappingEntry', (_message.Message,),
        dict(DESCRIPTOR=_DATASETCONFIG_TARGETCLASSMAPPINGENTRY,
             __module__='iva.detectnet_v2.proto.dataset_config_pb2'))),
         DESCRIPTOR=_DATASETCONFIG,
         __module__='iva.detectnet_v2.proto.dataset_config_pb2'))
_sym_db.RegisterMessage(DatasetConfig)
_sym_db.RegisterMessage(DatasetConfig.TargetClassMappingEntry)
_DATASETCONFIG_TARGETCLASSMAPPINGENTRY._options = None
# okay decompiling dataset_config_pb2.pyc
