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

install_requires = [
    "openfoodfacts",
    "requests>=2.18.4",
    "tqdm>=4.19.6",
    "django<2"      # Python 2.7
]

dependency_links = [
    "git+https://github.com/openfoodfacts/openfoodfacts-python.git@master#egg=openfoodfacts",
]

tests_require = [
    "mock==2.0.0"
]

version = "0.9"

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
    install_requires=install_requires,
    dependency_links=dependency_links,
    license='Apache 2.0',
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English', 'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
    test_suite='tests',
    tests_require=tests_require,
    extras_require={
    },
)
