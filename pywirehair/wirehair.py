import ctypes
from os.path import join as path_join, abspath, dirname

from .constants import Wirehair_Success

_dll_path = path_join(dirname(abspath(__file__)), 'libwirehair.so')


class wirehair:
    _wirehair = None
    _init = -1

    def __new__(cls, *args, **kwargs):
        # do wirehair init stuff on first run
        if cls._wirehair is None:
            cls._wirehair = ctypes.CDLL(_dll_path)
        if cls._init != Wirehair_Success:
            cls._init = cls._wirehair.wirehair_init_(2)
        return super().__new__(cls, *args, **kwargs)

    def dll(self):
        return self._wirehair
