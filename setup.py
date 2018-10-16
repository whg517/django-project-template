#!/usr/bin/env python

from setuptools import find_packages, setup

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

EXCLUDE_FROM_PACKAGES = []

setup(
    name='{{ project_name }}',
    version='0.0.1',
    author='Example Author',
    author_email="author@example.com",
    description="A Django project template.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python',
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
)
