# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meltapi/v1/run.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14meltapi/v1/run.proto\x12\nmeltapi.v1\"`\n\rSubmitRequest\x12\x16\n\x06\x62locks\x18\x01 \x01(\tR\x06\x62locks\x12!\n\x0c\x66ull_refresh\x18\x02 \x01(\x08R\x0b\x66ullRefresh\x12\x14\n\x05\x66orce\x18\x03 \x01(\x08R\x05\x66orce\"5\n\x0eSubmitResponse\x12#\n\x04jobs\x18\x02 \x03(\x0b\x32\x0f.meltapi.v1.JobR\x04jobs\"B\n\x03Job\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\x12\x15\n\x06job_id\x18\x02 \x01(\tR\x05jobId\x12\x14\n\x05state\x18\x03 \x01(\tR\x05state2O\n\nRunService\x12\x41\n\x06Submit\x12\x19.meltapi.v1.SubmitRequest\x1a\x1a.meltapi.v1.SubmitResponse\"\x00\x42\x63\n\x0e\x63om.meltapi.v1B\x08RunProtoP\x01\xa2\x02\x03MXX\xaa\x02\nMeltapi.V1\xca\x02\nMeltapi\\V1\xe2\x02\x16Meltapi\\V1\\GPBMetadata\xea\x02\x0bMeltapi::V1b\x06proto3')



_SUBMITREQUEST = DESCRIPTOR.message_types_by_name['SubmitRequest']
_SUBMITRESPONSE = DESCRIPTOR.message_types_by_name['SubmitResponse']
_JOB = DESCRIPTOR.message_types_by_name['Job']
SubmitRequest = _reflection.GeneratedProtocolMessageType('SubmitRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITREQUEST,
  '__module__' : 'meltapi.v1.run_pb2'
  # @@protoc_insertion_point(class_scope:meltapi.v1.SubmitRequest)
  })
_sym_db.RegisterMessage(SubmitRequest)

SubmitResponse = _reflection.GeneratedProtocolMessageType('SubmitResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITRESPONSE,
  '__module__' : 'meltapi.v1.run_pb2'
  # @@protoc_insertion_point(class_scope:meltapi.v1.SubmitResponse)
  })
_sym_db.RegisterMessage(SubmitResponse)

Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), {
  'DESCRIPTOR' : _JOB,
  '__module__' : 'meltapi.v1.run_pb2'
  # @@protoc_insertion_point(class_scope:meltapi.v1.Job)
  })
_sym_db.RegisterMessage(Job)

_RUNSERVICE = DESCRIPTOR.services_by_name['RunService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\016com.meltapi.v1B\010RunProtoP\001\242\002\003MXX\252\002\nMeltapi.V1\312\002\nMeltapi\\V1\342\002\026Meltapi\\V1\\GPBMetadata\352\002\013Meltapi::V1'
  _SUBMITREQUEST._serialized_start=36
  _SUBMITREQUEST._serialized_end=132
  _SUBMITRESPONSE._serialized_start=134
  _SUBMITRESPONSE._serialized_end=187
  _JOB._serialized_start=189
  _JOB._serialized_end=255
  _RUNSERVICE._serialized_start=257
  _RUNSERVICE._serialized_end=336
# @@protoc_insertion_point(module_scope)
