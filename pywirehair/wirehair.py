import ctypes
from os.path import join as path_join, abspath, dirname

from .constants import Wirehair_Success

_dll_path = path_join(dirname(abspath(__file__)), 'libwirehair.so')


class wirehair:
    _wirehair = None
    _init = False

    def __new__(cls, *args, **kwargs):
        # do wirehair init stuff on first run
        if cls._wirehair == None:
            cls._wirehair = ctypes.CDLL(_dll_path)
        if cls._init == False:
            cls._init = (cls._wirehair.wirehair_init_(2) == Wirehair_Success)
        return super().__new__(cls, *args, **kwargs)

    def dll(self):
        return self._wirehair

    def create_encoder(self, msg, packet_size):
        from .encoder import encoder
        return encoder(msg, packet_size)
