# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys

import bidiutils

try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command

version = bidiutils.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys, subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

setup(
    name='django-bidi-utils',
    version=version,
    description='context processors and filters for handling Bi-directional (BiDi) in django templates',
    long_description=readme + '\n\n' + history,
    author='Meir Kriheli',
    author_email='mkriheli@gmail.com',
    url='https://github.com/MeirKriheli/django-bidi-utils',
    packages=[
        'bidiutils',
    ],
    include_package_data=True,
    install_requires=[
    ],
    cmdclass={'test': PyTest},
    license="MIT",
    zip_safe=False,
    keywords='django-bidi-utils',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
