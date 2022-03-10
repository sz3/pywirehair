import ctypes
from os.path import join as path_join, abspath, dirname

from .constants import Wirehair_Success

_DLL_PATH = path_join(dirname(abspath(__file__)), 'libwirehair.so')


class _Wirehair:
    _dll = None
    _init = -1

    def __new__(cls, *args, **kwargs):
        # do wirehair init stuff on first run
        if cls._dll is None:
            cls._dll = ctypes.CDLL(_DLL_PATH)
        if cls._init != Wirehair_Success:
            cls._init = cls._dll.wirehair_init_(2)
        return super().__new__(cls, *args, **kwargs)

    def dll(self):
        return self._dll


def wirehair():
    return _Wirehair().dll()
