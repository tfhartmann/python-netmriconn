from setuptools import setup, find_packages
import sys, os

long_description = 'netmriconn is a library for working with the netmri rest api'
version = '0.1'

setup(
    name='netmriconn',
    version=version,
    description="netmri client library",
    long_description=long_description,
    url='http://github.com/huit/python-netmriconn',
    keywords='netmri',
    author='Luke Sullivan',
    author_email='luke_sullivan@harvard.edu',
    license='MIT',
    packages=['netmriconn'],
    install_requires=[
        # -*- Extra requirements: -*-
        ],
    entry_points= {
        },
    )
