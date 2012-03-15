#!/usr/bin/env python

import os
import re

from distutils.core import setup

# Extract the current version
# Based on: https://github.com/brosner/sqlalchemy/blob/master/setup.py#L12-14
v = open(os.path.join(os.path.dirname(__file__), 'revolver', 'core.py'))
VERSION = re.compile(r".*VERSION = '(.*?)'", re.S).match(v.read()).group(1)
v.close()

setup(
    name='revolver',
    version=VERSION,
    author='Michael Contento',
    author_email='michaelcontento@gmail.com',
    packages=['revolver', 'revolver.test', 'revolver.tool'],
    url='https://github.com/michaelcontento/revolver',
    license='LICENSE',
    description='Pythonic server orchestrating based on fabric / cuisine',
    long_description=open('README.md').read(),
    keywords=['fabric', 'cuisine', 'chef', 'puppet', 'ssh'],
    install_requires=['fabric', 'cuisine'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Clustering',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Systems Administration',   
        'Topic :: Utilities'
    ],
)
