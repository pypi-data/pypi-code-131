# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: featureform/proto/serving.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x66\x65\x61tureform/proto/serving.proto\x12\x19\x66\x65\x61tureform.serving.proto\"L\n\x13TrainingDataRequest\x12\x35\n\x02id\x18\x01 \x01(\x0b\x32).featureform.serving.proto.TrainingDataID\"/\n\x0eTrainingDataID\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"v\n\x0fTrainingDataRow\x12\x32\n\x08\x66\x65\x61tures\x18\x01 \x03(\x0b\x32 .featureform.serving.proto.Value\x12/\n\x05label\x18\x02 \x01(\x0b\x32 .featureform.serving.proto.Value\"\x82\x01\n\x13\x46\x65\x61tureServeRequest\x12\x36\n\x08\x66\x65\x61tures\x18\x01 \x03(\x0b\x32$.featureform.serving.proto.FeatureID\x12\x33\n\x08\x65ntities\x18\x02 \x03(\x0b\x32!.featureform.serving.proto.Entity\">\n\nFeatureRow\x12\x30\n\x06values\x18\x01 \x03(\x0b\x32 .featureform.serving.proto.Value\"*\n\tFeatureID\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"%\n\x06\x45ntity\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xad\x01\n\x05Value\x12\x13\n\tstr_value\x18\x01 \x01(\tH\x00\x12\x13\n\tint_value\x18\x02 \x01(\x05H\x00\x12\x15\n\x0b\x66loat_value\x18\x03 \x01(\x02H\x00\x12\x16\n\x0c\x64ouble_value\x18\x04 \x01(\x01H\x00\x12\x15\n\x0bint64_value\x18\x05 \x01(\x03H\x00\x12\x15\n\x0bint32_value\x18\x06 \x01(\x05H\x00\x12\x14\n\nbool_value\x18\x07 \x01(\x08H\x00\x42\x07\n\x05value2\xe2\x01\n\x07\x46\x65\x61ture\x12n\n\x0cTrainingData\x12..featureform.serving.proto.TrainingDataRequest\x1a*.featureform.serving.proto.TrainingDataRow\"\x00\x30\x01\x12g\n\x0c\x46\x65\x61tureServe\x12..featureform.serving.proto.FeatureServeRequest\x1a%.featureform.serving.proto.FeatureRow\"\x00\x42\x1eZ\x1cgithub.com/featureform/protob\x06proto3')



_TRAININGDATAREQUEST = DESCRIPTOR.message_types_by_name['TrainingDataRequest']
_TRAININGDATAID = DESCRIPTOR.message_types_by_name['TrainingDataID']
_TRAININGDATAROW = DESCRIPTOR.message_types_by_name['TrainingDataRow']
_FEATURESERVEREQUEST = DESCRIPTOR.message_types_by_name['FeatureServeRequest']
_FEATUREROW = DESCRIPTOR.message_types_by_name['FeatureRow']
_FEATUREID = DESCRIPTOR.message_types_by_name['FeatureID']
_ENTITY = DESCRIPTOR.message_types_by_name['Entity']
_VALUE = DESCRIPTOR.message_types_by_name['Value']
TrainingDataRequest = _reflection.GeneratedProtocolMessageType('TrainingDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRAININGDATAREQUEST,
  '__module__' : 'featureform.proto.serving_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.proto.TrainingDataRequest)
  })
_sym_db.RegisterMessage(TrainingDataRequest)

TrainingDataID = _reflection.GeneratedProtocolMessageType('TrainingDataID', (_message.Message,), {
  'DESCRIPTOR' : _TRAININGDATAID,
  '__module__' : 'featureform.proto.serving_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.proto.TrainingDataID)
  })
_sym_db.RegisterMessage(TrainingDataID)

TrainingDataRow = _reflection.GeneratedProtocolMessageType('TrainingDataRow', (_message.Message,), {
  'DESCRIPTOR' : _TRAININGDATAROW,
  '__module__' : 'featureform.proto.serving_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.proto.TrainingDataRow)
  })
_sym_db.RegisterMessage(TrainingDataRow)

FeatureServeRequest = _reflection.GeneratedProtocolMessageType('FeatureServeRequest', (_message.Message,), {
  'DESCRIPTOR' : _FEATURESERVEREQUEST,
  '__module__' : 'featureform.proto.serving_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.proto.FeatureServeRequest)
  })
_sym_db.RegisterMessage(FeatureServeRequest)

FeatureRow = _reflection.GeneratedProtocolMessageType('FeatureRow', (_message.Message,), {
  'DESCRIPTOR' : _FEATUREROW,
  '__module__' : 'featureform.proto.serving_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.proto.FeatureRow)
  })
_sym_db.RegisterMessage(FeatureRow)

FeatureID = _reflection.GeneratedProtocolMessageType('FeatureID', (_message.Message,), {
  'DESCRIPTOR' : _FEATUREID,
  '__module__' : 'featureform.proto.serving_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.proto.FeatureID)
  })
_sym_db.RegisterMessage(FeatureID)

Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), {
  'DESCRIPTOR' : _ENTITY,
  '__module__' : 'featureform.proto.serving_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.proto.Entity)
  })
_sym_db.RegisterMessage(Entity)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'featureform.proto.serving_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.proto.Value)
  })
_sym_db.RegisterMessage(Value)

_FEATURE = DESCRIPTOR.services_by_name['Feature']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\034github.com/featureform/proto'
  _TRAININGDATAREQUEST._serialized_start=62
  _TRAININGDATAREQUEST._serialized_end=138
  _TRAININGDATAID._serialized_start=140
  _TRAININGDATAID._serialized_end=187
  _TRAININGDATAROW._serialized_start=189
  _TRAININGDATAROW._serialized_end=307
  _FEATURESERVEREQUEST._serialized_start=310
  _FEATURESERVEREQUEST._serialized_end=440
  _FEATUREROW._serialized_start=442
  _FEATUREROW._serialized_end=504
  _FEATUREID._serialized_start=506
  _FEATUREID._serialized_end=548
  _ENTITY._serialized_start=550
  _ENTITY._serialized_end=587
  _VALUE._serialized_start=590
  _VALUE._serialized_end=763
  _FEATURE._serialized_start=766
  _FEATURE._serialized_end=992
# @@protoc_insertion_point(module_scope)
