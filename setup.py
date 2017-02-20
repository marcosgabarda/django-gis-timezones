# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division, absolute_import

import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')) as history:
    HISTORY = history.read().replace('.. :changelog:', '')

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Dynamically calculate the version based on belt.VERSION.
version = __import__('gis_timezones').__version__


setup(
    name='django-gis-timezones',
    version=version,
    packages=[
        'gis_timezones.management.commands',
        'gis_timezones.migrations',
        'gis_timezones',
    ],
    include_package_data=True,
    license='MIT License',
    description='Simple model to save timezones using geo-spatial data',
    long_description=README + '\n\n' + HISTORY,
    url='https://github.com/marcosgabarda/django-gis-timezones',
    author='Marcos Gabarda',
    author_email='hey@marcosgabarda.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
    install_requires=[
        'django-belt>=1.0a1',
        'pyshp>=1.2.3',
        'requests>=2.0',
    ],
)
