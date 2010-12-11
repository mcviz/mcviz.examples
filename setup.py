#! /usr/bin/env python

from os import walk
from os.path import join as pjoin

from setuptools import setup, find_packages
from distutils.core import Extension
from distutils.util import convert_path

def find_all_files(where, ignore=lambda x: False):
    all_files = []
    for path, dirs, files in walk(convert_path(where)):
        all_files.extend(pjoin(path[len(where)+1:], f) 
                         for f in files if not ignore(f))
    return all_files

setup(
    name='mcviz.examples',
    version='0.1',
    description="A package to contain example inputs for mcviz",
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Physicists :: Developers',
        'GNU Affero General Public License v3',
    ],
    keywords='mcviz hep examples hepmc montecarlo',
    author='Johannes Ebke and Peter Waller',
    author_email='dev@mcviz.net',
    url='http://mcviz.net',
    license='Affero GPLv3',
    namespace_packages=["mcviz"],
    packages=find_packages(),
    package_data={
        "mcviz.examples.inputs" : 
            find_all_files("mcviz/examples/inputs", 
                           lambda f: f.endswith(".py") or 
                                     f.endswith(".pyc")),
    }
)
