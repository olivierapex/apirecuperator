import os
import shutil
from setuptools import setup, find_packages
from codecs import open

# Setup script to install Api Recuperator as package, used by PIP
# A lot of installation variables, exemple "version",
# "Classifiers" can be found in setup.cfg
# Some documentations can be found here :
# Classifiers : https://pypi.python.org/pypi?%3Aaction=list_classifiers

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # Some Info about the python Api Recuperator project
    name='apirecuperator',
    version='1.0.0',
    description='Api Recuperator',
    long_description=long_description,
    author='Olivier Giroux',
    license='Do what the fuck you want',

    classifiers=[
        'License :: Do what the fuck you want',
        'Programming Language :: Python :: 3',
    ],

    # Package to include or exclude
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    # List of required dependencies
    install_requires=[
        'falcon>=1.1.0',
        'uwsgi>=2.0.14',
        'requests>=2.13.0',
        'configparser>=3.5.0',
        'python-logstash>=0.4.6',
        'pymongo>=3.6.0',
    ],

    # Creation of the BIN file
    scripts=['bin/apirecuperator'],

    data_files=[
        ('/bin', ['bin/apirecuperator']),
        ('/etc/init.d', ['etc/init.d/apirecuperator']),
        ('/usr/share/doc/apirecuperator', ['config.json.example']),
    ],
)

if not os.path.exists('/etc/apirecuperator'):
    os.mkdir('/etc/apirecuperator')
    shutil.copyfile('/usr/share/doc/apirecuperator/config.json.example', '/etc/apirecuperator/config.json')
if not os.path.exists('/var/log/apirecuperator'):
    os.mkdir('/var/log/apirecuperator')
