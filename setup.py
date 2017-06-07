#!/usr/bin/env python
#-*- coding: utf-8 -*-

from setuptools import setup

readme = open('README.md').read()

setup(
    name = 'wombat',
    version = '0.2',
    description = "A webapp for stylelend renting price suggestion",
    long_description = readme,
    author = "Patrick Spencer",
    author_email = "pkspenc@gmail.com",
    url = "http://bitbucket.org/patrickspencer/wombat/",
    py_modules = ['wombat'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
        'Programming Language :: Python :: 3.4'
    ]
)
