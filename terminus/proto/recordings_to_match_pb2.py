# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: terminus/proto/recordings_to_match.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from terminus.proto import core_pb2 as terminus_dot_proto_dot_core__pb2
from terminus.proto import recording_pb2 as terminus_dot_proto_dot_recording__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='terminus/proto/recordings_to_match.proto',
  package='terminus.recordings_to_match',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(terminus/proto/recordings_to_match.proto\x12\x1cterminus.recordings_to_match\x1a\x19terminus/proto/core.proto\x1a\x1eterminus/proto/recording.proto\"\xa8\x02\n\x11RecordingsToMatch\x12\x31\n\nrecordings\x18\x01 \x03(\x0b\x32\x1d.terminus.recording.Recording\x12I\n\x08segments\x18\x02 \x03(\x0b\x32\x37.terminus.recordings_to_match.RecordingsToMatch.Segment\x1a\x94\x01\n\x07Segment\x12\n\n\x02id\x18\x01 \x01(\x0c\x12%\n\x04path\x18\x02 \x03(\x0b\x32\x17.terminus.core.GeoPoint\x12+\n\nstart_line\x18\x03 \x03(\x0b\x32\x17.terminus.core.GeoPoint\x12)\n\x08\x65nd_line\x18\x04 \x03(\x0b\x32\x17.terminus.core.GeoPointb\x06proto3'
  ,
  dependencies=[terminus_dot_proto_dot_core__pb2.DESCRIPTOR,terminus_dot_proto_dot_recording__pb2.DESCRIPTOR,])




_RECORDINGSTOMATCH_SEGMENT = _descriptor.Descriptor(
  name='Segment',
  full_name='terminus.recordings_to_match.RecordingsToMatch.Segment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='terminus.recordings_to_match.RecordingsToMatch.Segment.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='terminus.recordings_to_match.RecordingsToMatch.Segment.path', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_line', full_name='terminus.recordings_to_match.RecordingsToMatch.Segment.start_line', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_line', full_name='terminus.recordings_to_match.RecordingsToMatch.Segment.end_line', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=282,
  serialized_end=430,
)

_RECORDINGSTOMATCH = _descriptor.Descriptor(
  name='RecordingsToMatch',
  full_name='terminus.recordings_to_match.RecordingsToMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='recordings', full_name='terminus.recordings_to_match.RecordingsToMatch.recordings', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='segments', full_name='terminus.recordings_to_match.RecordingsToMatch.segments', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RECORDINGSTOMATCH_SEGMENT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=430,
)

_RECORDINGSTOMATCH_SEGMENT.fields_by_name['path'].message_type = terminus_dot_proto_dot_core__pb2._GEOPOINT
_RECORDINGSTOMATCH_SEGMENT.fields_by_name['start_line'].message_type = terminus_dot_proto_dot_core__pb2._GEOPOINT
_RECORDINGSTOMATCH_SEGMENT.fields_by_name['end_line'].message_type = terminus_dot_proto_dot_core__pb2._GEOPOINT
_RECORDINGSTOMATCH_SEGMENT.containing_type = _RECORDINGSTOMATCH
_RECORDINGSTOMATCH.fields_by_name['recordings'].message_type = terminus_dot_proto_dot_recording__pb2._RECORDING
_RECORDINGSTOMATCH.fields_by_name['segments'].message_type = _RECORDINGSTOMATCH_SEGMENT
DESCRIPTOR.message_types_by_name['RecordingsToMatch'] = _RECORDINGSTOMATCH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RecordingsToMatch = _reflection.GeneratedProtocolMessageType('RecordingsToMatch', (_message.Message,), {

  'Segment' : _reflection.GeneratedProtocolMessageType('Segment', (_message.Message,), {
    'DESCRIPTOR' : _RECORDINGSTOMATCH_SEGMENT,
    '__module__' : 'terminus.proto.recordings_to_match_pb2'
    # @@protoc_insertion_point(class_scope:terminus.recordings_to_match.RecordingsToMatch.Segment)
    })
  ,
  'DESCRIPTOR' : _RECORDINGSTOMATCH,
  '__module__' : 'terminus.proto.recordings_to_match_pb2'
  # @@protoc_insertion_point(class_scope:terminus.recordings_to_match.RecordingsToMatch)
  })
_sym_db.RegisterMessage(RecordingsToMatch)
_sym_db.RegisterMessage(RecordingsToMatch.Segment)


# @@protoc_insertion_point(module_scope)
