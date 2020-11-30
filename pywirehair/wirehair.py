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
            print(cls._wirehair)
        if cls._init != Wirehair_Success:
            print('attempting init:')
            cls._init = cls._wirehair.wirehair_init_(2)
            print(cls._wirehair)
        return super().__new__(cls, *args, **kwargs)

    def dll(self):
        return self._wirehair
