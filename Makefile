.PHONY: default pypi clean dist-clean build wheel test flake

default: flake build test

pypi:
	python setup.py sdist
	twine upload dist/*.tar.gz

clean:
	find . -name '*.py[co]' -delete
	find . -name '__pycache__' -delete
	rm -rf build/ *.egg *.egg-info/
	rm pywirehair/libwirehair*

dist-clean:
	rm -rf dist/

build:
	python setup.py build
	python dev-copy-libs.py

wheel: build
	python setup.py bdist_wheel

test:
	coverage run -m unittest
	coverage report

flake:
	flake8
