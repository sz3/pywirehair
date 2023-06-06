import ctypes

from .constants import Wirehair_Success
from .wirehair import wirehair


class encoder:
    def __init__(self, msg, packet_size):
        self.msg = (ctypes.c_uint8 * len(msg)).from_buffer_copy(msg)
        self.packet_size = packet_size
        # WirehairCodec is a pointer, and we need to make that explicit
        wirehair().wirehair_encoder_create.restype = ctypes.c_void_p
        self._eid = wirehair().wirehair_encoder_create(
            None, ctypes.byref(self.msg), ctypes.c_uint64(len(self.msg)), ctypes.c_uint32(packet_size)
        )
        self._buff = (ctypes.c_uint8 * packet_size)()

    def encode(self, block_id):
        writelen = ctypes.c_uint32(0)
        res = wirehair().wirehair_encode(
            ctypes.c_void_p(self._eid), ctypes.c_uint(block_id), ctypes.byref(self._buff), ctypes.c_uint32(self.packet_size),
            ctypes.byref(writelen)
        )
        if res != Wirehair_Success:
            return None
        return bytes(bytearray(self._buff)[:writelen.value])
