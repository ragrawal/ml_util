#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.command.test import test as TestCommand
import re

for line in open('mlplumber/__init__.py'):
    match = re.match("__version__ *= *'(.*)'", line)
    if match:
        __version__, = match.groups()


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        raise SystemExit(errno)


setup(name='mlplumber',
      version=__version__,
      description='ML Utilities for constructing pipelines using baikal and sklearn_pandas',
      maintainer='Ritesh Agrawal',
      maintainer_email='ragrawal@gmail.com',
      url='https://github.com/ragrawal/mlplumber',
      packages=['mlplumber'],
      keywords=['scikit', 'sklearn', 'pandas', 'baikal'],
      install_requires=[
          'sklearn-pandas>=2.0.0',
          'baikal>=0.4.1'
      ],
      tests_require=['pytest', 'mock'],
      cmdclass={'test': PyTest},
      )
