#!/bin/sh
## targeting old glibc
# docker run --mount type=bind,source="$(pwd)",target="/usr/src/app" -it quay.io/pypa/manylinux2014_x86_64

cd /usr/src/app
rm /usr/bin/python
ln -s /opt/python/cp37-cp37m/bin/python /usr/bin/python

make wheel

