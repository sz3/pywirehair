#!/bin/sh
## targeting old glibc
# docker run --mount type=bind,source="$(pwd)",target="/usr/src/app" -it quay.io/pypa/manylinux2014_x86_64

cd /usr/src/app

for py in $(ls /opt/python/ | grep cp3); do
	echo $py
	rm /usr/bin/python -f
	ln -s /opt/python/$py/bin/python /usr/bin/python

	make clean
	make wheel
done
