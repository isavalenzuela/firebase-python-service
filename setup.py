# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="firebase-python-service",
    version="0.1.0",
    description="simple project that extracts data from firebase and exposes it with python service",
    license="MIT",
    author="isavalenzuela",
    keywords='firebase cloud development',
    install_requires=[
        'cachecontrol>=0.12.6',
        'google-api-core[grpc] >= 1.14.0, < 2.0.0dev; platform.python_implementation != "PyPy"',
        'google-api-python-client >= 1.7.8',
        'google-cloud-firestore>=1.4.0; platform.python_implementation != "PyPy"',
        'google-cloud-storage>=1.18.0',
    ],
    packages=find_packages(),
    python_requires='>=3.5',
    classifiers=[
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.8",
        ]
)