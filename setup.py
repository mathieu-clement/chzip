#!/usr/bin/env python3

from distutils.core import setup

setup(
    # Metadata
    name='Switzerland ZIP codes (chzip)',
    version='1.0',
    description='Query Switzerland ZIP codes from Python',
    long_description='The chzip package provides a quick and easy Python interface to look for zip codes and cities in Switzerland.',
    author='Mathieu Clément',
    author_email='mathieu.clement@freebourg.org',
    url='https://bitbucket.org/freebourg/chzip',
    classifiers=['Topic :: Communications', 
                 'Topic :: Office/Business',
                 'Programming Language :: Python :: 3',
                 'Operating System :: OS Independent',
                 'License :: OSI Approved :: BSD License',
                 'Intended Audience :: Customer Service',
                 'Intended Audience :: Telecommunications Industry']
    license='BSD'

    # What's included
    py_modules=['chzip'],
    package_dir={'chzip': 'chzip'},
    packages_data={'chzip': ['test_resources']}
    )
