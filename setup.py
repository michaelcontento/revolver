#!/usr/bin/env python

from setuptools import setup, find_packages

from revolver.core import version

setup(
    name = "revolver",
    version = version,
    install_requires = ["fabric", "cuisine"],
    packages = find_packages(),
    author = "Michael Contento",
    author_email = "michaelcontento@gmail.com",
    url = "https://github.com/michaelcontento/revolver",
    keywords = ["fabric", "cuisine", "chef", "puppet", "ssh"],
    description = "Pythonic server orchestrating based on fabric / cuisine",
    long_description = open('README.md').read(),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Clustering",
        "Topic :: System :: Software Distribution",
        "Topic :: System :: Systems Administration",   
        "Topic :: Utilities"
    ],
)
