# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/gr/v1/run.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15proto/gr/v1/run.proto\x12\x0bproto.gr.v1\"`\n\rSubmitRequest\x12\x16\n\x06\x62locks\x18\x01 \x01(\tR\x06\x62locks\x12!\n\x0c\x66ull_refresh\x18\x02 \x01(\x08R\x0b\x66ullRefresh\x12\x14\n\x05\x66orce\x18\x03 \x01(\x08R\x05\x66orce\"6\n\x0eSubmitResponse\x12$\n\x04jobs\x18\x02 \x03(\x0b\x32\x10.proto.gr.v1.JobR\x04jobs\"B\n\x03Job\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\x12\x15\n\x06job_id\x18\x02 \x01(\tR\x05jobId\x12\x14\n\x05state\x18\x03 \x01(\tR\x05state2Q\n\nRunService\x12\x43\n\x06Submit\x12\x1a.proto.gr.v1.SubmitRequest\x1a\x1b.proto.gr.v1.SubmitResponse\"\x00\x42i\n\x0f\x63om.proto.gr.v1B\x08RunProtoP\x01\xa2\x02\x03PGX\xaa\x02\x0bProto.Gr.V1\xca\x02\x0bProto\\Gr\\V1\xe2\x02\x17Proto\\Gr\\V1\\GPBMetadata\xea\x02\rProto::Gr::V1b\x06proto3')



_SUBMITREQUEST = DESCRIPTOR.message_types_by_name['SubmitRequest']
_SUBMITRESPONSE = DESCRIPTOR.message_types_by_name['SubmitResponse']
_JOB = DESCRIPTOR.message_types_by_name['Job']
SubmitRequest = _reflection.GeneratedProtocolMessageType('SubmitRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITREQUEST,
  '__module__' : 'proto.gr.v1.run_pb2'
  # @@protoc_insertion_point(class_scope:proto.gr.v1.SubmitRequest)
  })
_sym_db.RegisterMessage(SubmitRequest)

SubmitResponse = _reflection.GeneratedProtocolMessageType('SubmitResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITRESPONSE,
  '__module__' : 'proto.gr.v1.run_pb2'
  # @@protoc_insertion_point(class_scope:proto.gr.v1.SubmitResponse)
  })
_sym_db.RegisterMessage(SubmitResponse)

Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), {
  'DESCRIPTOR' : _JOB,
  '__module__' : 'proto.gr.v1.run_pb2'
  # @@protoc_insertion_point(class_scope:proto.gr.v1.Job)
  })
_sym_db.RegisterMessage(Job)

_RUNSERVICE = DESCRIPTOR.services_by_name['RunService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017com.proto.gr.v1B\010RunProtoP\001\242\002\003PGX\252\002\013Proto.Gr.V1\312\002\013Proto\\Gr\\V1\342\002\027Proto\\Gr\\V1\\GPBMetadata\352\002\rProto::Gr::V1'
  _SUBMITREQUEST._serialized_start=38
  _SUBMITREQUEST._serialized_end=134
  _SUBMITRESPONSE._serialized_start=136
  _SUBMITRESPONSE._serialized_end=190
  _JOB._serialized_start=192
  _JOB._serialized_end=258
  _RUNSERVICE._serialized_start=260
  _RUNSERVICE._serialized_end=341
# @@protoc_insertion_point(module_scope)
