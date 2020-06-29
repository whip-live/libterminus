# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: terminus/proto/recordings_matches.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from terminus.proto import recording_pb2 as terminus_dot_proto_dot_recording__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='terminus/proto/recordings_matches.proto',
  package='terminus.recordings_matches',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'terminus/proto/recordings_matches.proto\x12\x1bterminus.recordings_matches\x1a\x1eterminus/proto/recording.proto\"\xc3\x05\n\x11RecordingsMatches\x12\x30\n\trecording\x18\x01 \x01(\x0b\x32\x1d.terminus.recording.Recording\x12_\n\x11matching_segments\x18\x02 \x03(\x0b\x32\x44.terminus.recordings_matches.RecordingsMatches.MatchingSegmentsEntry\x12O\n\x0cmatching_ids\x18\x03 \x03(\x0b\x32\x39.terminus.recordings_matches.RecordingsMatches.MatchingId\x1a\x8d\x01\n\x0fMatchingSegment\x12U\n\x07indexes\x18\x01 \x03(\x0b\x32\x44.terminus.recordings_matches.RecordingsMatches.MatchingSegment.Index\x1a#\n\x05Index\x12\r\n\x05start\x18\x01 \x01(\r\x12\x0b\n\x03\x65nd\x18\x02 \x01(\r\x1a\xc0\x01\n\nMatchingId\x12\x12\n\nsegment_id\x18\x01 \x01(\x0c\x12U\n\tmatchings\x18\x02 \x03(\x0b\x32\x42.terminus.recordings_matches.RecordingsMatches.MatchingId.Matching\x1aG\n\x08Matching\x12\x13\n\x0bmatching_id\x18\x01 \x01(\x0c\x12\x13\n\x0bstart_index\x18\x02 \x01(\r\x12\x11\n\tend_index\x18\x03 \x01(\r\x1aw\n\x15MatchingSegmentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12M\n\x05value\x18\x02 \x01(\x0b\x32>.terminus.recordings_matches.RecordingsMatches.MatchingSegment:\x02\x38\x01\x62\x06proto3'
  ,
  dependencies=[terminus_dot_proto_dot_recording__pb2.DESCRIPTOR,])




_RECORDINGSMATCHES_MATCHINGSEGMENT_INDEX = _descriptor.Descriptor(
  name='Index',
  full_name='terminus.recordings_matches.RecordingsMatches.MatchingSegment.Index',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='terminus.recordings_matches.RecordingsMatches.MatchingSegment.Index.start', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='terminus.recordings_matches.RecordingsMatches.MatchingSegment.Index.end', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=461,
  serialized_end=496,
)

_RECORDINGSMATCHES_MATCHINGSEGMENT = _descriptor.Descriptor(
  name='MatchingSegment',
  full_name='terminus.recordings_matches.RecordingsMatches.MatchingSegment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='indexes', full_name='terminus.recordings_matches.RecordingsMatches.MatchingSegment.indexes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RECORDINGSMATCHES_MATCHINGSEGMENT_INDEX, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=355,
  serialized_end=496,
)

_RECORDINGSMATCHES_MATCHINGID_MATCHING = _descriptor.Descriptor(
  name='Matching',
  full_name='terminus.recordings_matches.RecordingsMatches.MatchingId.Matching',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='matching_id', full_name='terminus.recordings_matches.RecordingsMatches.MatchingId.Matching.matching_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_index', full_name='terminus.recordings_matches.RecordingsMatches.MatchingId.Matching.start_index', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_index', full_name='terminus.recordings_matches.RecordingsMatches.MatchingId.Matching.end_index', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=620,
  serialized_end=691,
)

_RECORDINGSMATCHES_MATCHINGID = _descriptor.Descriptor(
  name='MatchingId',
  full_name='terminus.recordings_matches.RecordingsMatches.MatchingId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='segment_id', full_name='terminus.recordings_matches.RecordingsMatches.MatchingId.segment_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='matchings', full_name='terminus.recordings_matches.RecordingsMatches.MatchingId.matchings', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RECORDINGSMATCHES_MATCHINGID_MATCHING, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=499,
  serialized_end=691,
)

_RECORDINGSMATCHES_MATCHINGSEGMENTSENTRY = _descriptor.Descriptor(
  name='MatchingSegmentsEntry',
  full_name='terminus.recordings_matches.RecordingsMatches.MatchingSegmentsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='terminus.recordings_matches.RecordingsMatches.MatchingSegmentsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='terminus.recordings_matches.RecordingsMatches.MatchingSegmentsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=693,
  serialized_end=812,
)

_RECORDINGSMATCHES = _descriptor.Descriptor(
  name='RecordingsMatches',
  full_name='terminus.recordings_matches.RecordingsMatches',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='recording', full_name='terminus.recordings_matches.RecordingsMatches.recording', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='matching_segments', full_name='terminus.recordings_matches.RecordingsMatches.matching_segments', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='matching_ids', full_name='terminus.recordings_matches.RecordingsMatches.matching_ids', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RECORDINGSMATCHES_MATCHINGSEGMENT, _RECORDINGSMATCHES_MATCHINGID, _RECORDINGSMATCHES_MATCHINGSEGMENTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=812,
)

_RECORDINGSMATCHES_MATCHINGSEGMENT_INDEX.containing_type = _RECORDINGSMATCHES_MATCHINGSEGMENT
_RECORDINGSMATCHES_MATCHINGSEGMENT.fields_by_name['indexes'].message_type = _RECORDINGSMATCHES_MATCHINGSEGMENT_INDEX
_RECORDINGSMATCHES_MATCHINGSEGMENT.containing_type = _RECORDINGSMATCHES
_RECORDINGSMATCHES_MATCHINGID_MATCHING.containing_type = _RECORDINGSMATCHES_MATCHINGID
_RECORDINGSMATCHES_MATCHINGID.fields_by_name['matchings'].message_type = _RECORDINGSMATCHES_MATCHINGID_MATCHING
_RECORDINGSMATCHES_MATCHINGID.containing_type = _RECORDINGSMATCHES
_RECORDINGSMATCHES_MATCHINGSEGMENTSENTRY.fields_by_name['value'].message_type = _RECORDINGSMATCHES_MATCHINGSEGMENT
_RECORDINGSMATCHES_MATCHINGSEGMENTSENTRY.containing_type = _RECORDINGSMATCHES
_RECORDINGSMATCHES.fields_by_name['recording'].message_type = terminus_dot_proto_dot_recording__pb2._RECORDING
_RECORDINGSMATCHES.fields_by_name['matching_segments'].message_type = _RECORDINGSMATCHES_MATCHINGSEGMENTSENTRY
_RECORDINGSMATCHES.fields_by_name['matching_ids'].message_type = _RECORDINGSMATCHES_MATCHINGID
DESCRIPTOR.message_types_by_name['RecordingsMatches'] = _RECORDINGSMATCHES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RecordingsMatches = _reflection.GeneratedProtocolMessageType('RecordingsMatches', (_message.Message,), {

  'MatchingSegment' : _reflection.GeneratedProtocolMessageType('MatchingSegment', (_message.Message,), {

    'Index' : _reflection.GeneratedProtocolMessageType('Index', (_message.Message,), {
      'DESCRIPTOR' : _RECORDINGSMATCHES_MATCHINGSEGMENT_INDEX,
      '__module__' : 'terminus.proto.recordings_matches_pb2'
      # @@protoc_insertion_point(class_scope:terminus.recordings_matches.RecordingsMatches.MatchingSegment.Index)
      })
    ,
    'DESCRIPTOR' : _RECORDINGSMATCHES_MATCHINGSEGMENT,
    '__module__' : 'terminus.proto.recordings_matches_pb2'
    # @@protoc_insertion_point(class_scope:terminus.recordings_matches.RecordingsMatches.MatchingSegment)
    })
  ,

  'MatchingId' : _reflection.GeneratedProtocolMessageType('MatchingId', (_message.Message,), {

    'Matching' : _reflection.GeneratedProtocolMessageType('Matching', (_message.Message,), {
      'DESCRIPTOR' : _RECORDINGSMATCHES_MATCHINGID_MATCHING,
      '__module__' : 'terminus.proto.recordings_matches_pb2'
      # @@protoc_insertion_point(class_scope:terminus.recordings_matches.RecordingsMatches.MatchingId.Matching)
      })
    ,
    'DESCRIPTOR' : _RECORDINGSMATCHES_MATCHINGID,
    '__module__' : 'terminus.proto.recordings_matches_pb2'
    # @@protoc_insertion_point(class_scope:terminus.recordings_matches.RecordingsMatches.MatchingId)
    })
  ,

  'MatchingSegmentsEntry' : _reflection.GeneratedProtocolMessageType('MatchingSegmentsEntry', (_message.Message,), {
    'DESCRIPTOR' : _RECORDINGSMATCHES_MATCHINGSEGMENTSENTRY,
    '__module__' : 'terminus.proto.recordings_matches_pb2'
    # @@protoc_insertion_point(class_scope:terminus.recordings_matches.RecordingsMatches.MatchingSegmentsEntry)
    })
  ,
  'DESCRIPTOR' : _RECORDINGSMATCHES,
  '__module__' : 'terminus.proto.recordings_matches_pb2'
  # @@protoc_insertion_point(class_scope:terminus.recordings_matches.RecordingsMatches)
  })
_sym_db.RegisterMessage(RecordingsMatches)
_sym_db.RegisterMessage(RecordingsMatches.MatchingSegment)
_sym_db.RegisterMessage(RecordingsMatches.MatchingSegment.Index)
_sym_db.RegisterMessage(RecordingsMatches.MatchingId)
_sym_db.RegisterMessage(RecordingsMatches.MatchingId.Matching)
_sym_db.RegisterMessage(RecordingsMatches.MatchingSegmentsEntry)


_RECORDINGSMATCHES_MATCHINGSEGMENTSENTRY._options = None
# @@protoc_insertion_point(module_scope)