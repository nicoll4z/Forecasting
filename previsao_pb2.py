# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: previsao.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'previsao.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eprevisao.proto\x12\x08previsao\"$\n\x0fPrevisaoRequest\x12\x11\n\tcity_name\x18\x01 \x01(\t\"\x8e\x01\n\rDailyForecast\x12\x0f\n\x07\x63ountry\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x64\x41rea\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\x12\x14\n\x0cweather_text\x18\x04 \x01(\t\x12\x13\n\x0btemperature\x18\x05 \x01(\x02\x12\x11\n\treal_feel\x18\x06 \x01(\x02\x12\x10\n\x08humidity\x18\x07 \x01(\x02\">\n\x10PrevisaoResponse\x12*\n\tforecasts\x18\x01 \x03(\x0b\x32\x17.previsao.DailyForecast2\xe9\x01\n\x0fPrevisaoService\x12\x46\n\rGetPrevisao5d\x12\x19.previsao.PrevisaoRequest\x1a\x1a.previsao.PrevisaoResponse\x12\x46\n\rGetPrevisao1d\x12\x19.previsao.PrevisaoRequest\x1a\x1a.previsao.PrevisaoResponse\x12\x46\n\rGetPrevisao1h\x12\x19.previsao.PrevisaoRequest\x1a\x1a.previsao.PrevisaoResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'previsao_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PREVISAOREQUEST']._serialized_start=28
  _globals['_PREVISAOREQUEST']._serialized_end=64
  _globals['_DAILYFORECAST']._serialized_start=67
  _globals['_DAILYFORECAST']._serialized_end=209
  _globals['_PREVISAORESPONSE']._serialized_start=211
  _globals['_PREVISAORESPONSE']._serialized_end=273
  _globals['_PREVISAOSERVICE']._serialized_start=276
  _globals['_PREVISAOSERVICE']._serialized_end=509
# @@protoc_insertion_point(module_scope)
