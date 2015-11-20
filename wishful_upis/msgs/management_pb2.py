# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: management.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='management.proto',
  package='wishful_upis.mgmt',
  serialized_pb=_b('\n\x10management.proto\x12\x11wishful_upis.mgmt\"e\n\x07MsgDesc\x12\x10\n\x08msg_type\x18\x01 \x02(\t\x12\x11\n\texec_time\x18\x02 \x01(\t\x12\x16\n\x0etransaction_id\x18\x03 \x01(\t\x12\x0c\n\x04uuid\x18\x04 \x01(\t\x12\x0f\n\x07msg_set\x18\x05 \x01(\x08\"\xb4\x01\n\nNewNodeMsg\x12\x12\n\nagent_uuid\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04info\x18\x03 \x01(\t\x12\x0f\n\x07modules\x18\x04 \x03(\t\x12;\n\nattributes\x18\x05 \x03(\x0b\x32\'.wishful_upis.mgmt.NewNodeMsg.Attribute\x1a(\n\tAttribute\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"Y\n\nNewNodeAck\x12\x0e\n\x06status\x18\x01 \x02(\x08\x12\x17\n\x0f\x63ontroller_uuid\x18\x02 \x01(\t\x12\x12\n\nagent_uuid\x18\x03 \x01(\t\x12\x0e\n\x06topics\x18\x04 \x03(\t\"1\n\x0bNodeExitMsg\x12\x12\n\nagent_uuid\x18\x01 \x02(\t\x12\x0e\n\x06reason\x18\x02 \x01(\t\"K\n\x17\x43ontrollerDiscoveredMsg\x12\x11\n\tdown_link\x18\x01 \x01(\t\x12\x0f\n\x07up_link\x18\x02 \x01(\t\x12\x0c\n\x04pair\x18\x03 \x01(\t\"%\n\x13\x44iscoverySuccessMsg\x12\x0e\n\x06status\x18\x01 \x02(\x08\"!\n\x10\x45xampleModuleReq\x12\r\n\x05hello\x18\x01 \x01(\t\"!\n\x10\x45xampleModuleAck\x12\r\n\x05hello\x18\x01 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MSGDESC = _descriptor.Descriptor(
  name='MsgDesc',
  full_name='wishful_upis.mgmt.MsgDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_type', full_name='wishful_upis.mgmt.MsgDesc.msg_type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exec_time', full_name='wishful_upis.mgmt.MsgDesc.exec_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='wishful_upis.mgmt.MsgDesc.transaction_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='wishful_upis.mgmt.MsgDesc.uuid', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg_set', full_name='wishful_upis.mgmt.MsgDesc.msg_set', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=140,
)


_NEWNODEMSG_ATTRIBUTE = _descriptor.Descriptor(
  name='Attribute',
  full_name='wishful_upis.mgmt.NewNodeMsg.Attribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='wishful_upis.mgmt.NewNodeMsg.Attribute.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='wishful_upis.mgmt.NewNodeMsg.Attribute.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=283,
  serialized_end=323,
)

_NEWNODEMSG = _descriptor.Descriptor(
  name='NewNodeMsg',
  full_name='wishful_upis.mgmt.NewNodeMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_uuid', full_name='wishful_upis.mgmt.NewNodeMsg.agent_uuid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='wishful_upis.mgmt.NewNodeMsg.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='wishful_upis.mgmt.NewNodeMsg.info', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modules', full_name='wishful_upis.mgmt.NewNodeMsg.modules', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='wishful_upis.mgmt.NewNodeMsg.attributes', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_NEWNODEMSG_ATTRIBUTE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=323,
)


_NEWNODEACK = _descriptor.Descriptor(
  name='NewNodeAck',
  full_name='wishful_upis.mgmt.NewNodeAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='wishful_upis.mgmt.NewNodeAck.status', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='controller_uuid', full_name='wishful_upis.mgmt.NewNodeAck.controller_uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='agent_uuid', full_name='wishful_upis.mgmt.NewNodeAck.agent_uuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='topics', full_name='wishful_upis.mgmt.NewNodeAck.topics', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=325,
  serialized_end=414,
)


_NODEEXITMSG = _descriptor.Descriptor(
  name='NodeExitMsg',
  full_name='wishful_upis.mgmt.NodeExitMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_uuid', full_name='wishful_upis.mgmt.NodeExitMsg.agent_uuid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='wishful_upis.mgmt.NodeExitMsg.reason', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=416,
  serialized_end=465,
)


_CONTROLLERDISCOVEREDMSG = _descriptor.Descriptor(
  name='ControllerDiscoveredMsg',
  full_name='wishful_upis.mgmt.ControllerDiscoveredMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='down_link', full_name='wishful_upis.mgmt.ControllerDiscoveredMsg.down_link', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='up_link', full_name='wishful_upis.mgmt.ControllerDiscoveredMsg.up_link', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pair', full_name='wishful_upis.mgmt.ControllerDiscoveredMsg.pair', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=467,
  serialized_end=542,
)


_DISCOVERYSUCCESSMSG = _descriptor.Descriptor(
  name='DiscoverySuccessMsg',
  full_name='wishful_upis.mgmt.DiscoverySuccessMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='wishful_upis.mgmt.DiscoverySuccessMsg.status', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=544,
  serialized_end=581,
)


_EXAMPLEMODULEREQ = _descriptor.Descriptor(
  name='ExampleModuleReq',
  full_name='wishful_upis.mgmt.ExampleModuleReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hello', full_name='wishful_upis.mgmt.ExampleModuleReq.hello', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=583,
  serialized_end=616,
)


_EXAMPLEMODULEACK = _descriptor.Descriptor(
  name='ExampleModuleAck',
  full_name='wishful_upis.mgmt.ExampleModuleAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hello', full_name='wishful_upis.mgmt.ExampleModuleAck.hello', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=618,
  serialized_end=651,
)

_NEWNODEMSG_ATTRIBUTE.containing_type = _NEWNODEMSG
_NEWNODEMSG.fields_by_name['attributes'].message_type = _NEWNODEMSG_ATTRIBUTE
DESCRIPTOR.message_types_by_name['MsgDesc'] = _MSGDESC
DESCRIPTOR.message_types_by_name['NewNodeMsg'] = _NEWNODEMSG
DESCRIPTOR.message_types_by_name['NewNodeAck'] = _NEWNODEACK
DESCRIPTOR.message_types_by_name['NodeExitMsg'] = _NODEEXITMSG
DESCRIPTOR.message_types_by_name['ControllerDiscoveredMsg'] = _CONTROLLERDISCOVEREDMSG
DESCRIPTOR.message_types_by_name['DiscoverySuccessMsg'] = _DISCOVERYSUCCESSMSG
DESCRIPTOR.message_types_by_name['ExampleModuleReq'] = _EXAMPLEMODULEREQ
DESCRIPTOR.message_types_by_name['ExampleModuleAck'] = _EXAMPLEMODULEACK

MsgDesc = _reflection.GeneratedProtocolMessageType('MsgDesc', (_message.Message,), dict(
  DESCRIPTOR = _MSGDESC,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_upis.mgmt.MsgDesc)
  ))
_sym_db.RegisterMessage(MsgDesc)

NewNodeMsg = _reflection.GeneratedProtocolMessageType('NewNodeMsg', (_message.Message,), dict(

  Attribute = _reflection.GeneratedProtocolMessageType('Attribute', (_message.Message,), dict(
    DESCRIPTOR = _NEWNODEMSG_ATTRIBUTE,
    __module__ = 'management_pb2'
    # @@protoc_insertion_point(class_scope:wishful_upis.mgmt.NewNodeMsg.Attribute)
    ))
  ,
  DESCRIPTOR = _NEWNODEMSG,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_upis.mgmt.NewNodeMsg)
  ))
_sym_db.RegisterMessage(NewNodeMsg)
_sym_db.RegisterMessage(NewNodeMsg.Attribute)

NewNodeAck = _reflection.GeneratedProtocolMessageType('NewNodeAck', (_message.Message,), dict(
  DESCRIPTOR = _NEWNODEACK,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_upis.mgmt.NewNodeAck)
  ))
_sym_db.RegisterMessage(NewNodeAck)

NodeExitMsg = _reflection.GeneratedProtocolMessageType('NodeExitMsg', (_message.Message,), dict(
  DESCRIPTOR = _NODEEXITMSG,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_upis.mgmt.NodeExitMsg)
  ))
_sym_db.RegisterMessage(NodeExitMsg)

ControllerDiscoveredMsg = _reflection.GeneratedProtocolMessageType('ControllerDiscoveredMsg', (_message.Message,), dict(
  DESCRIPTOR = _CONTROLLERDISCOVEREDMSG,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_upis.mgmt.ControllerDiscoveredMsg)
  ))
_sym_db.RegisterMessage(ControllerDiscoveredMsg)

DiscoverySuccessMsg = _reflection.GeneratedProtocolMessageType('DiscoverySuccessMsg', (_message.Message,), dict(
  DESCRIPTOR = _DISCOVERYSUCCESSMSG,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_upis.mgmt.DiscoverySuccessMsg)
  ))
_sym_db.RegisterMessage(DiscoverySuccessMsg)

ExampleModuleReq = _reflection.GeneratedProtocolMessageType('ExampleModuleReq', (_message.Message,), dict(
  DESCRIPTOR = _EXAMPLEMODULEREQ,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_upis.mgmt.ExampleModuleReq)
  ))
_sym_db.RegisterMessage(ExampleModuleReq)

ExampleModuleAck = _reflection.GeneratedProtocolMessageType('ExampleModuleAck', (_message.Message,), dict(
  DESCRIPTOR = _EXAMPLEMODULEACK,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_upis.mgmt.ExampleModuleAck)
  ))
_sym_db.RegisterMessage(ExampleModuleAck)


# @@protoc_insertion_point(module_scope)
