#!/usr/bin/env python
from setuptools import setup, find_packages
import os

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='junit-xml',
	author='Brian Beyer',
	author_email='brian@kyr.us',
	url='https://github.com/kyrus/python-junit-xml',
	license='MIT',
	packages=find_packages(),
	description='Creates JUnit XML test result documents that can be read by tools such as Jenkins',
	long_description=read('README.md'),
	version = "1.0",
	classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Freely Distributable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Testing',
	    ],
	)

