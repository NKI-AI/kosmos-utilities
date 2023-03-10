#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["fabric"]

test_requirements = []

setup(
    author="Jonas Teuwen",
    author_email="j.teuwen@nki.nl",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Python utilities to manage the Kosmos cluster",
    entry_points={
        "console_scripts": [
            "create-project=kosmos.cli:main",
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="kosmos_utilities",
    name="kosmos_utilities",
    packages=find_packages(include=["kosmos_utilities", "kosmos_utilities.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/NKI-AI/kosmos_utilities",
    version="0.1.0",
    zip_safe=False,
)
