#!/usr/bin/env python
# encoding: utf-8

import os, sys
from setuptools import setup

setup(
    name             = 'imagetext',
    description      = 'Save text into images and read text from images created by imagetext',
    long_description = """
imagetext is a project that allows one to save data
visually into an image, and to read that data back out.

Raw bytes from the input text are shown visually in the
resulting image.
""",
    license          = 'MIT',
    version          = '0.0.1',
    author           = 'James \'d0c_s4vage\' Johnson',
    maintainer       = 'James \'d0c_s4vage\' Johnson',
    author_email     = 'd0c.s4vage@gmail.com',
    url              = 'https://github.com/d0c-s4vage/imagetext',
    platforms        = 'Cross Platform',
	download_url     = "https://github.com/d0c-s4vage/imagetext/tarball/v0.0.1",

	install_requires =  open(os.path.join(os.path.dirname(__file__), "requirements.txt")).read().split("\n"),

    classifiers      =  [
        'Programming Language :: Python :: 2',
        #'Programming Language :: Python :: 3',
    ],
    scripts          =  [ "bin/imagetext" ],
    packages= ['imagetext'],
)
