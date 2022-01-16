#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    "Jinja2==3.0.3"
 ]

setup_requirements = [ ]

setup(
    author="James Stevenson",
    author_email='james.m.stevenson@gmail.comm',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 5 - Production/Stable'
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description="UMBC CMSC 291 (Special Topics in Computer Science: Continued Computer Science for Non-majors) lecture notes and slides",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='cmsc_210',
    name='cmsc_210',
    packages=find_packages(include=['cmsc_210', 'cmsc_210.*']),
    setup_requires=setup_requirements,
    url='https://github.com/mazelife/cmsc_210',
    version='1.0.0',
    zip_safe=False,
)
