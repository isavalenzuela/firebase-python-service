# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

install_requires = [
    'cachecontrol>=0.12.6',
    'google-api-core[grpc] >= 1.14.0, < 2.0.0dev; platform.python_implementation != "PyPy"',
    'google-api-python-client >= 1.7.8',
    'google-cloud-firestore>=1.4.0; platform.python_implementation != "PyPy"',
    'google-cloud-storage>=1.18.0',
]

setup(
    name="firebase-python-service",
    version="0.1.0",
    description="simple project that extracts data from firebase and exposes it with python service",
    license="MIT",
    author="isavalenzuela",
    packages=['firebase_admin'],
    install_requires=install_requires,
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ]
)
