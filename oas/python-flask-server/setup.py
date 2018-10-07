# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "jatdb_server"
VERSION = "0.0.1"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="NGenetzky&#39;s API",
    author_email="Nathan@Genetzky.us",
    url="",
    keywords=["Swagger", "NGenetzky&#39;s API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['jatdb_server=jatdb_server.__main__:main']},
    long_description="""\
    This is an API I am designing for myself using swagger. You can find  out more about Swagger at [http://swagger.io](http://swagger.io) 
    """
)

