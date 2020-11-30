import ctypes

from .constants import Wirehair_Success
from .wirehair import wirehair


class encoder:
    def __init__(self, msg, packet_size):
        self.msg = (ctypes.c_uint8 * len(msg)).from_buffer_copy(msg)
        self.packet_size = packet_size
        self._eid = wirehair().dll().wirehair_encoder_create(
            0, ctypes.byref(self.msg), ctypes.c_uint64(len(self.msg)), ctypes.c_uint32(packet_size)
        )
        self._buff = (ctypes.c_uint8 * packet_size)()

    def encode(self, block_id):
        print(self._eid)
        return b'a'
