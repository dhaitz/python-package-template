#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from pathlib import Path


setup(
    name='sample',
    version='0.1.0',
    description='Sample package',
    long_description=Path('README.md').open().read(),
    author='Dominik Haitz',
    author_email='-',
    url='https://github.com/dhaitz/python-package-template',
    license=Path('LICENSE').open().read(),
    packages=['sample'],
)
