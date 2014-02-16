#/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

setup(
    name="django-zurb-foundation",
    version="5.1.1",
    description="Django Zurb Foundation package.",
    author="Amar Šahinović",
    author_email="amar@sahinovic.com",
    url="https://github.com/amarsahinovic/django-zurb-foundation",
    license='BSD License', 
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
    install_requires=[

    ],
)
