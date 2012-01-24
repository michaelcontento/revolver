#!/usr/bin/env python

from distutils.core import setup

from revolver.core import version

setup(
    name='revolver',
    version=version,
    author='Michael Contento',
    author_email='michaelcontento@gmail.com',
    packages=['revolver', 'revolver.test'],
    url='https://github.com/michaelcontento/revolver',
    license='LICENSE',
    description='Pythonic server orchestrating based on fabric / cuisine',
    long_description=open('README.md').read(),
    keywords=['fabric', 'cuisine', 'chef', 'puppet', 'ssh'],
    requires=['fabric (>= 1.3)', 'cuisine (>= 0.1)'],
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
