#!/usr/bin/env python
# NOTE: This file is only used for tox to be able to install the library to test it.
# See pyproject.toml for the actual setup file.
import sys

from setuptools import setup

with open("yeelight/version.py") as f:
    exec(f.read())

classifiers = [
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

setup(
    name="yeelight",
    version=__version__,  # type: ignore
    author="Stavros Korokithakis",
    author_email="hi@stavros.io",
    url="https://gitlab.com/stavros/python-yeelight/",
    description="A Python library for controlling YeeLight RGB bulbs.",
    long_description=open("README.rst").read(),
    license="BSD",
    classifiers=classifiers,
    packages=["yeelight"],
    python_requires=">=3.4",
    install_requires=["future", "ifaddr", 'pypiwin32;platform_system=="Windows"',],
    test_suite="yeelight.tests",
    tests_require=[],
)
