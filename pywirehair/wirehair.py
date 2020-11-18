
import ctypes
from os.path import join as path_join, abspath, dirname

_dll_path = path_join(dirname(abspath(__file__)), 'libwirehair.so')
_wirehair = ctypes.CDLL(_dll_path)


class wirehair:
    def doit(self):
        print(_wirehair)
        pass
