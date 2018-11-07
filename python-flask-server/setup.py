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
    description="jatdb",
    author_email="Nathan@Genetzky.us",
    url="",
    keywords=["Swagger", "jatdb"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['jatdb_server=jatdb_server.__main__:main']},
    long_description="""\
    JSON API to DB: Fetch JSON from APIs and send to a TinyDB database.
    """
)

