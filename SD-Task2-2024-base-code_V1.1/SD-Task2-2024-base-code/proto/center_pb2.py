# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: center.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63\x65nter.proto\";\n\x13notifyMasterRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\"#\n\x14notifyMasterResponse\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\x08\"\x12\n\x10\x63\x61nCommitRequest\" \n\x11\x63\x61nCommitResponse\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\x08\"-\n\x0f\x64oCommitRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x1f\n\x10\x64oCommitResponse\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\x08\"\x10\n\x0e\x64oAbortRequest\"\x1e\n\x0f\x64oAbortResponse\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\x08\"\r\n\x0bPingRequest\"\x0e\n\x0cPingResponse2\x87\x02\n\x10InternalProtocol\x12;\n\x0cnotifyMaster\x12\x14.notifyMasterRequest\x1a\x15.notifyMasterResponse\x12\x32\n\tcanCommit\x12\x11.canCommitRequest\x1a\x12.canCommitResponse\x12/\n\x08\x64oCommit\x12\x10.doCommitRequest\x1a\x11.doCommitResponse\x12,\n\x07\x64oAbort\x12\x0f.doAbortRequest\x1a\x10.doAbortResponse\x12#\n\x04ping\x12\x0c.PingRequest\x1a\r.PingResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'center_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_NOTIFYMASTERREQUEST']._serialized_start=16
  _globals['_NOTIFYMASTERREQUEST']._serialized_end=75
  _globals['_NOTIFYMASTERRESPONSE']._serialized_start=77
  _globals['_NOTIFYMASTERRESPONSE']._serialized_end=112
  _globals['_CANCOMMITREQUEST']._serialized_start=114
  _globals['_CANCOMMITREQUEST']._serialized_end=132
  _globals['_CANCOMMITRESPONSE']._serialized_start=134
  _globals['_CANCOMMITRESPONSE']._serialized_end=166
  _globals['_DOCOMMITREQUEST']._serialized_start=168
  _globals['_DOCOMMITREQUEST']._serialized_end=213
  _globals['_DOCOMMITRESPONSE']._serialized_start=215
  _globals['_DOCOMMITRESPONSE']._serialized_end=246
  _globals['_DOABORTREQUEST']._serialized_start=248
  _globals['_DOABORTREQUEST']._serialized_end=264
  _globals['_DOABORTRESPONSE']._serialized_start=266
  _globals['_DOABORTRESPONSE']._serialized_end=296
  _globals['_PINGREQUEST']._serialized_start=298
  _globals['_PINGREQUEST']._serialized_end=311
  _globals['_PINGRESPONSE']._serialized_start=313
  _globals['_PINGRESPONSE']._serialized_end=327
  _globals['_INTERNALPROTOCOL']._serialized_start=330
  _globals['_INTERNALPROTOCOL']._serialized_end=593
# @@protoc_insertion_point(module_scope)
