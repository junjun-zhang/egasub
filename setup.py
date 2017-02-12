#!/usr/bin/env python
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

with open('requirements.txt') as f:
    install_reqs = f.read().splitlines()
with open('requirements-test.txt') as f:
    tests_require = f.read().splitlines()

setup(
    name = 'egasub',
    version='0.1.0rc2',
    url='https://github.com/icgc-dcc/egasub',
    description = 'ICGC tool for assisting EGA data submission',
    license='GPL-3.0',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires = install_reqs,
    tests_require = tests_require,
    cmdclass = {'test': PyTest},
    package_data={'egasub': [
                                'ega/data/enums/*.json',
                                'submission/metadata_template/*/*.yaml'
                            ]},
    include_package_data = True,
    entry_points={
        'console_scripts': [
            'egasub=egasub.cli:main',
        ]
    },
)
