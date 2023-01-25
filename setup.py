#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  setup.py
#
#  Copyright 2020 Bruce Schubert <bruce@emxsys.com>

import setuptools

# load the long_description from the README
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="callattendant-service",   # Add user name when uploading to TestPyPI
    version="0.1",        # Ensure this is in-sync with VERSION in config.py
    author="Bruce Schubert",
    author_email="bruce@emxsys.com",
    description="An automated call attendant and call blocker using a Raspberry Pi and USR-5637 modem",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://emxsys.github.io/callattendant/",
    packages=setuptools.find_packages(exclude=["tests"]),
    include_package_data=True,      # Includes files from MANIFEST.in
    install_requires=[
        "setuptools==66.1.1",
        "Werkzeug~=2.2.2",
        "gpiozero~=1.6.2",
        "pyserial~=3.5",
        "hardware~=0.30.0",
        "beautifulsoup4~=4.11.1",
        "pytest~=7.2.1",
    ],
    entry_points={
        "console_scripts": [
            "callattendant = callattendant.__main__:main",
        ]
    },
    scripts=[
        "bin/start-callattendant",
        "bin/stop-callattendant",
        "bin/restart-callattendant",
        "bin/monitor-callattendant",
    ],
    data_files=[
        ('share/applications', [
            'bin/configure-callattendant.desktop',
            'bin/monitor-callattendant.desktop',
            'bin/restart-callattendant.desktop',
            'bin/stop-callattendant.desktop',
        ]),
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Environment :: Other Environment",
        "Development Status :: 5 - Production/Stable",
        "Framework :: Flask",
        "Topic :: Communications :: Telephony",
        "Topic :: Home Automation",
    ],
    python_requires='>=3.5',

)
