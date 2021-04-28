# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from zed_interfaces/Skeleton2D.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import zed_interfaces.msg

class Skeleton2D(genpy.Message):
  _md5sum = "1754703e1a6ce338ad28b9ee81fb712a"
  _type = "zed_interfaces/Skeleton2D"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Skeleton joints indices
#        16-14   15-17
#             \ /
#              0
#              |
#       2------1------5
#       |    |   |    |
#	    |    |   |    |
#       3    |   |    6
#       |    |   |    |
#       |    |   |    |
#       4    8   11   7
#            |   |
#            |   |
#            |   |
#            9   12
#            |   |
#            |   |
#            |   |
#           10   13
zed_interfaces/Keypoint2Df[18] keypoints

================================================================================
MSG: zed_interfaces/Keypoint2Df
float32[2] kp
"""
  __slots__ = ['keypoints']
  _slot_types = ['zed_interfaces/Keypoint2Df[18]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       keypoints

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Skeleton2D, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.keypoints is None:
        self.keypoints = [zed_interfaces.msg.Keypoint2Df() for _ in range(18)]
    else:
      self.keypoints = [zed_interfaces.msg.Keypoint2Df() for _ in range(18)]

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      if len(self.keypoints) != 18:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (18, len(self.keypoints), 'self.keypoints')))
      for val1 in self.keypoints:
        buff.write(_get_struct_2f().pack(*val1.kp))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.keypoints is None:
        self.keypoints = None
      end = 0
      self.keypoints = []
      for i in range(0, 18):
        val1 = zed_interfaces.msg.Keypoint2Df()
        start = end
        end += 8
        val1.kp = _get_struct_2f().unpack(str[start:end])
        self.keypoints.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      if len(self.keypoints) != 18:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (18, len(self.keypoints), 'self.keypoints')))
      for val1 in self.keypoints:
        buff.write(val1.kp.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.keypoints is None:
        self.keypoints = None
      end = 0
      self.keypoints = []
      for i in range(0, 18):
        val1 = zed_interfaces.msg.Keypoint2Df()
        start = end
        end += 8
        val1.kp = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=2)
        self.keypoints.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2f = None
def _get_struct_2f():
    global _struct_2f
    if _struct_2f is None:
        _struct_2f = struct.Struct("<2f")
    return _struct_2f
