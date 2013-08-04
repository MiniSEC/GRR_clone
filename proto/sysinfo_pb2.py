# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grr/proto/sysinfo.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import grr.proto.semantic_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='grr/proto/sysinfo.proto',
  package='',
  serialized_pb='\n\x17grr/proto/sysinfo.proto\x1a\x18grr/proto/semantic.proto\"\xf9\x03\n\x07Process\x12\x0b\n\x03pid\x18\x01 \x01(\r\x12\x0c\n\x04ppid\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0b\n\x03\x65xe\x18\x04 \x01(\t\x12\x0f\n\x07\x63mdline\x18\x05 \x03(\t\x12\r\n\x05\x63time\x18\x06 \x01(\x04\x12\x10\n\x08real_uid\x18\x07 \x01(\r\x12\x15\n\reffective_uid\x18\x08 \x01(\r\x12\x11\n\tsaved_uid\x18\t \x01(\r\x12\x10\n\x08real_gid\x18\n \x01(\r\x12\x15\n\reffective_gid\x18\x0b \x01(\r\x12\x11\n\tsaved_gid\x18\x0c \x01(\r\x12\x10\n\x08username\x18\r \x01(\t\x12\x10\n\x08terminal\x18\x0e \x01(\t\x12\x0e\n\x06status\x18\x0f \x01(\t\x12\x0c\n\x04nice\x18\x10 \x01(\x05\x12\x0b\n\x03\x63wd\x18\x11 \x01(\t\x12\x13\n\x0bnum_threads\x18\x12 \x01(\r\x12\x15\n\ruser_cpu_time\x18\x13 \x01(\x02\x12\x17\n\x0fsystem_cpu_time\x18\x14 \x01(\x02\x12\x13\n\x0b\x63pu_percent\x18\x15 \x01(\x02\x12\x10\n\x08RSS_size\x18\x16 \x01(\x04\x12\x10\n\x08VMS_size\x18\x17 \x01(\x04\x12\x16\n\x0ememory_percent\x18\x18 \x01(\x02\x12\x12\n\nopen_files\x18\x19 \x03(\t\x12\'\n\x0b\x63onnections\x18\x1a \x03(\x0b\x32\x12.NetworkConnection\"+\n\x0fNetworkEndpoint\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\"\xce\x04\n\x11NetworkConnection\x12)\n\x06\x66\x61mily\x18\x01 \x01(\x0e\x32\x19.NetworkConnection.Family\x12\x35\n\x04type\x18\x02 \x01(\x0e\x32\x17.NetworkConnection.Type:\x0eUNKNOWN_SOCKET\x12\'\n\rlocal_address\x18\x03 \x01(\x0b\x32\x10.NetworkEndpoint\x12(\n\x0eremote_address\x18\x04 \x01(\x0b\x32\x10.NetworkEndpoint\x12\x30\n\x05state\x18\x05 \x01(\x0e\x32\x18.NetworkConnection.State:\x07UNKNOWN\x12\x0b\n\x03pid\x18\x06 \x01(\r\x12\r\n\x05\x63time\x18\x07 \x01(\x04\";\n\x06\x46\x61mily\x12\x08\n\x04INET\x10\x02\x12\t\n\x05INET6\x10\n\x12\r\n\tINET6_WIN\x10\x17\x12\r\n\tINET6_OSX\x10\x1e\";\n\x04Type\x12\x12\n\x0eUNKNOWN_SOCKET\x10\x00\x12\x0f\n\x0bSOCK_STREAM\x10\x01\x12\x0e\n\nSOCK_DGRAM\x10\x02\"\xbb\x01\n\x05State\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x43LOSED\x10\x01\x12\n\n\x06LISTEN\x10\x02\x12\x0c\n\x08SYN_SENT\x10\x03\x12\x0c\n\x08SYN_RCVD\x10\x04\x12\t\n\x05\x45STAB\x10\x05\x12\r\n\tFIN_WAIT1\x10\x06\x12\r\n\tFIN_WAIT2\x10\x07\x12\x0e\n\nCLOSE_WAIT\x10\x08\x12\x0b\n\x07\x43LOSING\x10\t\x12\x0c\n\x08LAST_ACK\x10\n\x12\r\n\tTIME_WAIT\x10\x0b\x12\x0e\n\nDELETE_TCB\x10\x0c\"N\n\nFilesystem\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\t\x12\x13\n\x0bmount_point\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\r\n\x05label\x18\x04 \x01(\t\"1\n\x07MRUFile\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x14\n\ttimestamp\x18\x02 \x01(\x04:\x01\x30\"C\n\x06RunKey\x12\x0f\n\x07keyname\x18\x01 \x01(\t\x12\x10\n\x08\x66ilepath\x18\x02 \x01(\t\x12\x16\n\x0blastwritten\x18\x03 \x01(\x04:\x01\x30\"\x9c\x01\n\nLaunchdJob\x12\x13\n\x0bsessiontype\x18\x01 \x01(\t\x12\x16\n\x0elastexitstatus\x18\x02 \x01(\x04\x12\x0f\n\x07timeout\x18\x03 \x01(\x04\x12\x10\n\x08ondemand\x18\x04 \x01(\x08\x12\x13\n\x0bmachservice\x18\x05 \x03(\t\x12\x19\n\x11perjobmachservice\x18\x06 \x03(\t\x12\x0e\n\x06socket\x18\x07 \x03(\t\"f\n\x07Service\x12\r\n\x05label\x18\x01 \x01(\t\x12\x0f\n\x07program\x18\x02 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x03 \x01(\t\x12\x0b\n\x03pid\x18\x04 \x01(\x04\x12 \n\x0bosx_launchd\x18\x05 \x01(\x0b\x32\x0b.LaunchdJob\"\xf7\x01\n\x0fSoftwarePackage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x14\n\x0c\x61rchitecture\x18\x03 \x01(\t\x12\x11\n\tpublisher\x18\x04 \x01(\t\x12=\n\rinstall_state\x18\x05 \x01(\x0e\x32\x1d.SoftwarePackage.InstallState:\x07UNKNOWN\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\"H\n\x0cInstallState\x12\r\n\tINSTALLED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0f\n\x0bUNINSTALLED\x10\x02\x12\x0b\n\x07UNKNOWN\x10\x03')



_NETWORKCONNECTION_FAMILY = _descriptor.EnumDescriptor(
  name='Family',
  full_name='NetworkConnection.Family',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INET', index=0, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INET6', index=1, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INET6_WIN', index=2, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INET6_OSX', index=3, number=30,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=887,
  serialized_end=946,
)

_NETWORKCONNECTION_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='NetworkConnection.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_SOCKET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOCK_STREAM', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOCK_DGRAM', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=948,
  serialized_end=1007,
)

_NETWORKCONNECTION_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='NetworkConnection.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOSED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LISTEN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYN_SENT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYN_RCVD', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ESTAB', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIN_WAIT1', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIN_WAIT2', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOSE_WAIT', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOSING', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAST_ACK', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIME_WAIT', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE_TCB', index=12, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1010,
  serialized_end=1197,
)

_SOFTWAREPACKAGE_INSTALLSTATE = _descriptor.EnumDescriptor(
  name='InstallState',
  full_name='SoftwarePackage.InstallState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INSTALLED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNINSTALLED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1838,
  serialized_end=1910,
)


_PROCESS = _descriptor.Descriptor(
  name='Process',
  full_name='Process',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='Process.pid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ppid', full_name='Process.ppid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Process.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exe', full_name='Process.exe', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cmdline', full_name='Process.cmdline', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='Process.ctime', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='real_uid', full_name='Process.real_uid', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='effective_uid', full_name='Process.effective_uid', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='saved_uid', full_name='Process.saved_uid', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='real_gid', full_name='Process.real_gid', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='effective_gid', full_name='Process.effective_gid', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='saved_gid', full_name='Process.saved_gid', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='username', full_name='Process.username', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='terminal', full_name='Process.terminal', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='Process.status', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nice', full_name='Process.nice', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cwd', full_name='Process.cwd', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_threads', full_name='Process.num_threads', index=17,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_cpu_time', full_name='Process.user_cpu_time', index=18,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='system_cpu_time', full_name='Process.system_cpu_time', index=19,
      number=20, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpu_percent', full_name='Process.cpu_percent', index=20,
      number=21, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RSS_size', full_name='Process.RSS_size', index=21,
      number=22, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='VMS_size', full_name='Process.VMS_size', index=22,
      number=23, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='memory_percent', full_name='Process.memory_percent', index=23,
      number=24, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open_files', full_name='Process.open_files', index=24,
      number=25, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='connections', full_name='Process.connections', index=25,
      number=26, type=11, cpp_type=10, label=3,
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
  serialized_start=54,
  serialized_end=559,
)


_NETWORKENDPOINT = _descriptor.Descriptor(
  name='NetworkEndpoint',
  full_name='NetworkEndpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='NetworkEndpoint.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='NetworkEndpoint.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=561,
  serialized_end=604,
)


_NETWORKCONNECTION = _descriptor.Descriptor(
  name='NetworkConnection',
  full_name='NetworkConnection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='family', full_name='NetworkConnection.family', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='NetworkConnection.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='local_address', full_name='NetworkConnection.local_address', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remote_address', full_name='NetworkConnection.remote_address', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='NetworkConnection.state', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pid', full_name='NetworkConnection.pid', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='NetworkConnection.ctime', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NETWORKCONNECTION_FAMILY,
    _NETWORKCONNECTION_TYPE,
    _NETWORKCONNECTION_STATE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=607,
  serialized_end=1197,
)


_FILESYSTEM = _descriptor.Descriptor(
  name='Filesystem',
  full_name='Filesystem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='Filesystem.device', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mount_point', full_name='Filesystem.mount_point', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Filesystem.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='Filesystem.label', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=1199,
  serialized_end=1277,
)


_MRUFILE = _descriptor.Descriptor(
  name='MRUFile',
  full_name='MRUFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='MRUFile.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='MRUFile.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
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
  serialized_start=1279,
  serialized_end=1328,
)


_RUNKEY = _descriptor.Descriptor(
  name='RunKey',
  full_name='RunKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyname', full_name='RunKey.keyname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filepath', full_name='RunKey.filepath', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastwritten', full_name='RunKey.lastwritten', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
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
  serialized_start=1330,
  serialized_end=1397,
)


_LAUNCHDJOB = _descriptor.Descriptor(
  name='LaunchdJob',
  full_name='LaunchdJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sessiontype', full_name='LaunchdJob.sessiontype', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastexitstatus', full_name='LaunchdJob.lastexitstatus', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='LaunchdJob.timeout', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ondemand', full_name='LaunchdJob.ondemand', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='machservice', full_name='LaunchdJob.machservice', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='perjobmachservice', full_name='LaunchdJob.perjobmachservice', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='socket', full_name='LaunchdJob.socket', index=6,
      number=7, type=9, cpp_type=9, label=3,
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
  serialized_start=1400,
  serialized_end=1556,
)


_SERVICE = _descriptor.Descriptor(
  name='Service',
  full_name='Service',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='Service.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='program', full_name='Service.program', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='args', full_name='Service.args', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pid', full_name='Service.pid', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='osx_launchd', full_name='Service.osx_launchd', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1558,
  serialized_end=1660,
)


_SOFTWAREPACKAGE = _descriptor.Descriptor(
  name='SoftwarePackage',
  full_name='SoftwarePackage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='SoftwarePackage.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='SoftwarePackage.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='architecture', full_name='SoftwarePackage.architecture', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='publisher', full_name='SoftwarePackage.publisher', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='install_state', full_name='SoftwarePackage.install_state', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='SoftwarePackage.description', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SOFTWAREPACKAGE_INSTALLSTATE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1663,
  serialized_end=1910,
)

_PROCESS.fields_by_name['connections'].message_type = _NETWORKCONNECTION
_NETWORKCONNECTION.fields_by_name['family'].enum_type = _NETWORKCONNECTION_FAMILY
_NETWORKCONNECTION.fields_by_name['type'].enum_type = _NETWORKCONNECTION_TYPE
_NETWORKCONNECTION.fields_by_name['local_address'].message_type = _NETWORKENDPOINT
_NETWORKCONNECTION.fields_by_name['remote_address'].message_type = _NETWORKENDPOINT
_NETWORKCONNECTION.fields_by_name['state'].enum_type = _NETWORKCONNECTION_STATE
_NETWORKCONNECTION_FAMILY.containing_type = _NETWORKCONNECTION;
_NETWORKCONNECTION_TYPE.containing_type = _NETWORKCONNECTION;
_NETWORKCONNECTION_STATE.containing_type = _NETWORKCONNECTION;
_SERVICE.fields_by_name['osx_launchd'].message_type = _LAUNCHDJOB
_SOFTWAREPACKAGE.fields_by_name['install_state'].enum_type = _SOFTWAREPACKAGE_INSTALLSTATE
_SOFTWAREPACKAGE_INSTALLSTATE.containing_type = _SOFTWAREPACKAGE;
DESCRIPTOR.message_types_by_name['Process'] = _PROCESS
DESCRIPTOR.message_types_by_name['NetworkEndpoint'] = _NETWORKENDPOINT
DESCRIPTOR.message_types_by_name['NetworkConnection'] = _NETWORKCONNECTION
DESCRIPTOR.message_types_by_name['Filesystem'] = _FILESYSTEM
DESCRIPTOR.message_types_by_name['MRUFile'] = _MRUFILE
DESCRIPTOR.message_types_by_name['RunKey'] = _RUNKEY
DESCRIPTOR.message_types_by_name['LaunchdJob'] = _LAUNCHDJOB
DESCRIPTOR.message_types_by_name['Service'] = _SERVICE
DESCRIPTOR.message_types_by_name['SoftwarePackage'] = _SOFTWAREPACKAGE

class Process(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PROCESS

  # @@protoc_insertion_point(class_scope:Process)

class NetworkEndpoint(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NETWORKENDPOINT

  # @@protoc_insertion_point(class_scope:NetworkEndpoint)

class NetworkConnection(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NETWORKCONNECTION

  # @@protoc_insertion_point(class_scope:NetworkConnection)

class Filesystem(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FILESYSTEM

  # @@protoc_insertion_point(class_scope:Filesystem)

class MRUFile(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MRUFILE

  # @@protoc_insertion_point(class_scope:MRUFile)

class RunKey(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RUNKEY

  # @@protoc_insertion_point(class_scope:RunKey)

class LaunchdJob(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LAUNCHDJOB

  # @@protoc_insertion_point(class_scope:LaunchdJob)

class Service(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SERVICE

  # @@protoc_insertion_point(class_scope:Service)

class SoftwarePackage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SOFTWAREPACKAGE

  # @@protoc_insertion_point(class_scope:SoftwarePackage)


# @@protoc_insertion_point(module_scope)