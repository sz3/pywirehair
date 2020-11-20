import ctypes

from .constants import Wirehair_Success, Wirehair_NeedMore
from .wirehair import wirehair


class decoder:
    def __init__(self, msg_size, packet_size):
        self.msg_size = msg_size
        self._did = wirehair().dll().wirehair_decoder_create(0, ctypes.c_uint64(msg_size), ctypes.c_uint32(packet_size))

    def decode(self, block_id, buffer):
        buffer = (ctypes.c_uint8 * len(buffer)).from_buffer_copy(buffer)
        res = wirehair().dll().wirehair_decode(
            self._did,
            ctypes.c_uint(block_id),
            ctypes.byref(buffer),
            len(buffer)
        )
        if res == Wirehair_Success:
            return self._recover()
        elif res != Wirehair_NeedMore:
            raise Exception(f'wirehair decode failed :( {res}')
        return None

    def _recover(self):
        dec = (ctypes.c_uint8 * self.msg_size)()
        res = wirehair().dll().wirehair_recover(
            self._did,
            ctypes.byref(dec),
            ctypes.c_uint64(self.msg_size)
        )
        if res != Wirehair_Success:
            return None
        return bytes(bytearray(dec))