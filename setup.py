import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-bidi-utils",
    version = "0.2",
    url = 'http://github.com/mksoft/django-bidi-utils',
    license = 'MIT',
    description = "context processors and helpers for BIDI in django templates",
    long_description = read('README.rst') + read('CHANGELOG.rst'),

    author = 'Meir Kriheli',
    author_email = 'meir@mksoft.co.il',

    packages = find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data = True,

    install_requires = ['setuptools'],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
