import os
import re
import sys
import platform
import subprocess
from glob import iglob
from os.path import join as path_join, abspath, dirname, basename
from shutil import copyfile

from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
from distutils.version import LooseVersion


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):
    def run(self):
        try:
            out = subprocess.check_output(['cmake', '--version'])
        except OSError:
            raise RuntimeError("CMake must be installed to build the following extensions: " +
                               ", ".join(e.name for e in self.extensions))

        cmake_version = LooseVersion(re.search(r'version\s*([\d.]+)', out.decode()).group(1))
        if cmake_version < LooseVersion('3.5.0'):
            raise RuntimeError("CMake >= 3.5.0 is required")

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = path_join(abspath(dirname(self.get_ext_fullpath(ext.name))), 'pywirehair')
        print(f'extdir is {extdir}')
        cmake_args = ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + extdir]
        cmake_args += ['-DBUILD_SHARED_LIBS=1']

        build_type = os.environ.get("BUILD_TYPE", "Release")
        build_args = ['--config', build_type]

        # Pile all .so in one place and use $ORIGIN as RPATH
        cmake_args += ["-DCMAKE_BUILD_WITH_INSTALL_RPATH=TRUE"]
        cmake_args += ["-DCMAKE_INSTALL_RPATH={}".format("$ORIGIN")]

        if platform.system() == "Windows":
            cmake_args += ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{}={}'.format(build_type.upper(), extdir)]
            if sys.maxsize > 2**32:
                cmake_args += ['-A', 'x64']
            build_args += ['--', '/m']
        else:
            cmake_args += ['-DCMAKE_BUILD_TYPE=' + build_type]
            build_args += ['--', '-j4']

        env = os.environ.copy()
        env['CXXFLAGS'] = '{} -DVERSION_INFO=\\"{}\\"'.format(env.get('CXXFLAGS', ''),
                                                              self.distribution.get_version())
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        subprocess.check_call(['cmake', ext.sourcedir] + cmake_args, cwd=self.build_temp, env=env)
        subprocess.check_call(['cmake',
                               '--build', '.',
                               '--target', os.path.basename(ext.name)
                               ] + build_args,
                              cwd=self.build_temp)

        # copy over the built library for local dev
        localdir = path_join(dirname(abspath(__file__)), 'pywirehair')
        for f in iglob(f'{extdir}/libwirehair*'):
            copyfile(f, path_join(localdir, basename(f)))


def read_version():
    with open("VERSION") as f:
        return f.readline().strip()


setup(
    name='pywirehair',
    license='MIT',
    url="https://github.com/sz3/pywirehair",
    version=read_version(),

    author='Stephen Zimmerman',
    author_email='sz@galacticicecube.com',
    description='Python wrapper for wirehair FEC',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',

    ext_modules=[CMakeExtension('wirehair', 'wirehair')],
    packages=find_packages(exclude=["tests"]),
    cmdclass=dict(build_ext=CMakeBuild),
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
)
