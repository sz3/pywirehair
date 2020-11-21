.PHONY: default pypi build clean test flake

default: flake build test

pypi:
	python setup.py sdist
	twine upload dist/*.tar.gz

clean:
	find . -name '*.py[co]' -delete
	find . -name '__pycache__' -delete
	rm -rf build/ dist/ *.egg *.egg-info/

build:
	python setup.py build
	python dev-copy-libs.py

test:
	coverage run -m unittest
	coverage report

flake:
	flake8
