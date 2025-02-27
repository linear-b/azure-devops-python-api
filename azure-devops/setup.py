# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from setuptools import setup, find_packages

NAME = "linearb-azure-devops-client"
VERSION = "0.9.5"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "msrest>=0.6.0,<0.7.0"
]

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
]

setup(
    name=NAME,
    version=VERSION,
    license='MIT',
    description="Python wrapper around the Azure DevOps 6.x APIs",
    author="Microsoft Corporation",
    author_email="vstscli@microsoft.com",
    url="https://github.com/linear-b/azure-devops-python-api",
    keywords=["Microsoft", "LinearB", "VSTS", "Team Services", "SDK", "AzureTfs", "AzureDevOps", "DevOps"],
    install_requires=REQUIRES,
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    """
)
