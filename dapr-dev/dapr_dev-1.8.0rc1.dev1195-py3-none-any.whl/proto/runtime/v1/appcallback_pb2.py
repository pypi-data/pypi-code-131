# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dapr/proto/runtime/v1/appcallback.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from dapr.proto.common.v1 import common_pb2 as dapr_dot_proto_dot_common_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'dapr/proto/runtime/v1/appcallback.proto\x12\x15\x64\x61pr.proto.runtime.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a!dapr/proto/common/v1/common.proto\"\xae\x01\n\x11TopicEventRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x14\n\x0cspec_version\x18\x04 \x01(\t\x12\x19\n\x11\x64\x61ta_content_type\x18\x05 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x07 \x01(\x0c\x12\r\n\x05topic\x18\x06 \x01(\t\x12\x13\n\x0bpubsub_name\x18\x08 \x01(\t\x12\x0c\n\x04path\x18\t \x01(\t\"\xa6\x01\n\x12TopicEventResponse\x12R\n\x06status\x18\x01 \x01(\x0e\x32\x42.dapr.proto.runtime.v1.TopicEventResponse.TopicEventResponseStatus\"<\n\x18TopicEventResponseStatus\x12\x0b\n\x07SUCCESS\x10\x00\x12\t\n\x05RETRY\x10\x01\x12\x08\n\x04\x44ROP\x10\x02\"\xae\x01\n\x13\x42indingEventRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12J\n\x08metadata\x18\x03 \x03(\x0b\x32\x38.dapr.proto.runtime.v1.BindingEventRequest.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x88\x02\n\x14\x42indingEventResponse\x12\x12\n\nstore_name\x18\x01 \x01(\t\x12/\n\x06states\x18\x02 \x03(\x0b\x32\x1f.dapr.proto.common.v1.StateItem\x12\n\n\x02to\x18\x03 \x03(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\x12X\n\x0b\x63oncurrency\x18\x05 \x01(\x0e\x32\x43.dapr.proto.runtime.v1.BindingEventResponse.BindingEventConcurrency\"7\n\x17\x42indingEventConcurrency\x12\x0e\n\nSEQUENTIAL\x10\x00\x12\x0c\n\x08PARALLEL\x10\x01\"a\n\x1eListTopicSubscriptionsResponse\x12?\n\rsubscriptions\x18\x01 \x03(\x0b\x32(.dapr.proto.runtime.v1.TopicSubscription\"\x81\x02\n\x11TopicSubscription\x12\x13\n\x0bpubsub_name\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12H\n\x08metadata\x18\x03 \x03(\x0b\x32\x36.dapr.proto.runtime.v1.TopicSubscription.MetadataEntry\x12\x32\n\x06routes\x18\x05 \x01(\x0b\x32\".dapr.proto.runtime.v1.TopicRoutes\x12\x19\n\x11\x64\x65\x61\x64_letter_topic\x18\x06 \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"O\n\x0bTopicRoutes\x12/\n\x05rules\x18\x01 \x03(\x0b\x32 .dapr.proto.runtime.v1.TopicRule\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x02 \x01(\t\"(\n\tTopicRule\x12\r\n\x05match\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\"-\n\x19ListInputBindingsResponse\x12\x10\n\x08\x62indings\x18\x01 \x03(\t2\x86\x04\n\x0b\x41ppCallback\x12W\n\x08OnInvoke\x12#.dapr.proto.common.v1.InvokeRequest\x1a$.dapr.proto.common.v1.InvokeResponse\"\x00\x12i\n\x16ListTopicSubscriptions\x12\x16.google.protobuf.Empty\x1a\x35.dapr.proto.runtime.v1.ListTopicSubscriptionsResponse\"\x00\x12\x65\n\x0cOnTopicEvent\x12(.dapr.proto.runtime.v1.TopicEventRequest\x1a).dapr.proto.runtime.v1.TopicEventResponse\"\x00\x12_\n\x11ListInputBindings\x12\x16.google.protobuf.Empty\x1a\x30.dapr.proto.runtime.v1.ListInputBindingsResponse\"\x00\x12k\n\x0eOnBindingEvent\x12*.dapr.proto.runtime.v1.BindingEventRequest\x1a+.dapr.proto.runtime.v1.BindingEventResponse\"\x00\x42y\n\nio.dapr.v1B\x15\x44\x61prAppCallbackProtosZ1github.com/dapr/dapr/pkg/proto/runtime/v1;runtime\xaa\x02 Dapr.AppCallback.Autogen.Grpc.v1b\x06proto3')



_TOPICEVENTREQUEST = DESCRIPTOR.message_types_by_name['TopicEventRequest']
_TOPICEVENTRESPONSE = DESCRIPTOR.message_types_by_name['TopicEventResponse']
_BINDINGEVENTREQUEST = DESCRIPTOR.message_types_by_name['BindingEventRequest']
_BINDINGEVENTREQUEST_METADATAENTRY = _BINDINGEVENTREQUEST.nested_types_by_name['MetadataEntry']
_BINDINGEVENTRESPONSE = DESCRIPTOR.message_types_by_name['BindingEventResponse']
_LISTTOPICSUBSCRIPTIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListTopicSubscriptionsResponse']
_TOPICSUBSCRIPTION = DESCRIPTOR.message_types_by_name['TopicSubscription']
_TOPICSUBSCRIPTION_METADATAENTRY = _TOPICSUBSCRIPTION.nested_types_by_name['MetadataEntry']
_TOPICROUTES = DESCRIPTOR.message_types_by_name['TopicRoutes']
_TOPICRULE = DESCRIPTOR.message_types_by_name['TopicRule']
_LISTINPUTBINDINGSRESPONSE = DESCRIPTOR.message_types_by_name['ListInputBindingsResponse']
_TOPICEVENTRESPONSE_TOPICEVENTRESPONSESTATUS = _TOPICEVENTRESPONSE.enum_types_by_name['TopicEventResponseStatus']
_BINDINGEVENTRESPONSE_BINDINGEVENTCONCURRENCY = _BINDINGEVENTRESPONSE.enum_types_by_name['BindingEventConcurrency']
TopicEventRequest = _reflection.GeneratedProtocolMessageType('TopicEventRequest', (_message.Message,), {
  'DESCRIPTOR' : _TOPICEVENTREQUEST,
  '__module__' : 'dapr.proto.runtime.v1.appcallback_pb2'
  # @@protoc_insertion_point(class_scope:dapr.proto.runtime.v1.TopicEventRequest)
  })
_sym_db.RegisterMessage(TopicEventRequest)

TopicEventResponse = _reflection.GeneratedProtocolMessageType('TopicEventResponse', (_message.Message,), {
  'DESCRIPTOR' : _TOPICEVENTRESPONSE,
  '__module__' : 'dapr.proto.runtime.v1.appcallback_pb2'
  # @@protoc_insertion_point(class_scope:dapr.proto.runtime.v1.TopicEventResponse)
  })
_sym_db.RegisterMessage(TopicEventResponse)

BindingEventRequest = _reflection.GeneratedProtocolMessageType('BindingEventRequest', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _BINDINGEVENTREQUEST_METADATAENTRY,
    '__module__' : 'dapr.proto.runtime.v1.appcallback_pb2'
    # @@protoc_insertion_point(class_scope:dapr.proto.runtime.v1.BindingEventRequest.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _BINDINGEVENTREQUEST,
  '__module__' : 'dapr.proto.runtime.v1.appcallback_pb2'
  # @@protoc_insertion_point(class_scope:dapr.proto.runtime.v1.BindingEventRequest)
  })
_sym_db.RegisterMessage(BindingEventRequest)
_sym_db.RegisterMessage(BindingEventRequest.MetadataEntry)

BindingEventResponse = _reflection.GeneratedProtocolMessageType('BindingEventResponse', (_message.Message,), {
  'DESCRIPTOR' : _BINDINGEVENTRESPONSE,
  '__module__' : 'dapr.proto.runtime.v1.appcallback_pb2'
  # @@protoc_insertion_point(class_scope:dapr.proto.runtime.v1.BindingEventResponse)
  })
_sym_db.RegisterMessage(BindingEventResponse)

ListTopicSubscriptionsResponse = _reflection.GeneratedProtocolMessageType('ListTopicSubscriptionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTOPICSUBSCRIPTIONSRESPONSE,
  '__module__' : 'dapr.proto.runtime.v1.appcallback_pb2'
  # @@protoc_insertion_point(class_scope:dapr.proto.runtime.v1.ListTopicSubscriptionsResponse)
  })
_sym_db.RegisterMessage(ListTopicSubscriptionsResponse)

TopicSubscription = _reflection.GeneratedProtocolMessageType('TopicSubscription', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _TOPICSUBSCRIPTION_METADATAENTRY,
    '__module__' : 'dapr.proto.runtime.v1.appcallback_pb2'
    # @@protoc_insertion_point(class_scope:dapr.proto.runtime.v1.TopicSubscription.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _TOPICSUBSCRIPTION,
  '__module__' : 'dapr.proto.runtime.v1.appcallback_pb2'
  # @@protoc_insertion_point(class_scope:dapr.proto.runtime.v1.TopicSubscription)
  })
_sym_db.RegisterMessage(TopicSubscription)
_sym_db.RegisterMessage(TopicSubscription.MetadataEntry)

TopicRoutes = _reflection.GeneratedProtocolMessageType('TopicRoutes', (_message.Message,), {
  'DESCRIPTOR' : _TOPICROUTES,
  '__module__' : 'dapr.proto.runtime.v1.appcallback_pb2'
  # @@protoc_insertion_point(class_scope:dapr.proto.runtime.v1.TopicRoutes)
  })
_sym_db.RegisterMessage(TopicRoutes)

TopicRule = _reflection.GeneratedProtocolMessageType('TopicRule', (_message.Message,), {
  'DESCRIPTOR' : _TOPICRULE,
  '__module__' : 'dapr.proto.runtime.v1.appcallback_pb2'
  # @@protoc_insertion_point(class_scope:dapr.proto.runtime.v1.TopicRule)
  })
_sym_db.RegisterMessage(TopicRule)

ListInputBindingsResponse = _reflection.GeneratedProtocolMessageType('ListInputBindingsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTINPUTBINDINGSRESPONSE,
  '__module__' : 'dapr.proto.runtime.v1.appcallback_pb2'
  # @@protoc_insertion_point(class_scope:dapr.proto.runtime.v1.ListInputBindingsResponse)
  })
_sym_db.RegisterMessage(ListInputBindingsResponse)

_APPCALLBACK = DESCRIPTOR.services_by_name['AppCallback']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\nio.dapr.v1B\025DaprAppCallbackProtosZ1github.com/dapr/dapr/pkg/proto/runtime/v1;runtime\252\002 Dapr.AppCallback.Autogen.Grpc.v1'
  _BINDINGEVENTREQUEST_METADATAENTRY._options = None
  _BINDINGEVENTREQUEST_METADATAENTRY._serialized_options = b'8\001'
  _TOPICSUBSCRIPTION_METADATAENTRY._options = None
  _TOPICSUBSCRIPTION_METADATAENTRY._serialized_options = b'8\001'
  _TOPICEVENTREQUEST._serialized_start=131
  _TOPICEVENTREQUEST._serialized_end=305
  _TOPICEVENTRESPONSE._serialized_start=308
  _TOPICEVENTRESPONSE._serialized_end=474
  _TOPICEVENTRESPONSE_TOPICEVENTRESPONSESTATUS._serialized_start=414
  _TOPICEVENTRESPONSE_TOPICEVENTRESPONSESTATUS._serialized_end=474
  _BINDINGEVENTREQUEST._serialized_start=477
  _BINDINGEVENTREQUEST._serialized_end=651
  _BINDINGEVENTREQUEST_METADATAENTRY._serialized_start=604
  _BINDINGEVENTREQUEST_METADATAENTRY._serialized_end=651
  _BINDINGEVENTRESPONSE._serialized_start=654
  _BINDINGEVENTRESPONSE._serialized_end=918
  _BINDINGEVENTRESPONSE_BINDINGEVENTCONCURRENCY._serialized_start=863
  _BINDINGEVENTRESPONSE_BINDINGEVENTCONCURRENCY._serialized_end=918
  _LISTTOPICSUBSCRIPTIONSRESPONSE._serialized_start=920
  _LISTTOPICSUBSCRIPTIONSRESPONSE._serialized_end=1017
  _TOPICSUBSCRIPTION._serialized_start=1020
  _TOPICSUBSCRIPTION._serialized_end=1277
  _TOPICSUBSCRIPTION_METADATAENTRY._serialized_start=604
  _TOPICSUBSCRIPTION_METADATAENTRY._serialized_end=651
  _TOPICROUTES._serialized_start=1279
  _TOPICROUTES._serialized_end=1358
  _TOPICRULE._serialized_start=1360
  _TOPICRULE._serialized_end=1400
  _LISTINPUTBINDINGSRESPONSE._serialized_start=1402
  _LISTINPUTBINDINGSRESPONSE._serialized_end=1447
  _APPCALLBACK._serialized_start=1450
  _APPCALLBACK._serialized_end=1968
# @@protoc_insertion_point(module_scope)
