# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open("README.rst") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="algorithms",
    version="0.1.0",
    description="Learning data structures and algorithms with Python",
    long_description=readme,
    author="Nhan Le",
    author_email="nhan99dn@gmail.com",
    url="https://github.com/NLe1/Pyrithms",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
)
