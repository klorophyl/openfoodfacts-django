#!/usr/bin/env python

import os
import sys

from setuptools import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'off_django',
]

requires = open('requirements.txt').read().split('\n')

version = "0.0.1"

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='off_django',
    version=version,
    description='OpenFoodFacts Django app.',
    long_description=readme,
    author='Gabriel Samain',
    author_email='gabriel@foodvisor.io',
    url='http://openfoodfacts.org',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'off_django': 'off_django'},
    include_package_data=True,
    install_requires=requires,
    license='Apache 2.0',
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English', 'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
    extras_require={
    },
)
