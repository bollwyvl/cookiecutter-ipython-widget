#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    setup,
    find_packages,
)

try:
    from jupyterpip import cmdclass
except:
    import importlib
    import pip
    pip.main(['install', 'jupyter-pip'])
    cmdclass = importlib.import_module('jupyterpip').cmdclass


# load version without side-effects
__version__ = None
with open('{{ cookiecutter.pkg_name }}/version.py') as f:
    exec(f.read())


setup(
    name='{{ cookiecutter.repo_name }}',
    version=__version__,
    description='{{ cookiecutter.project_short_description }}',
    long_description=open('README.rst').read(),
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=find_packages(include=['{{ cookiecutter.pkg_name }}']),
    include_package_data=True,
    license='{{ cookiecutter.license }}',
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }} ipython',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: {{ cookiecutter.license }} License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Widget Sets',
        "Programming Language :: Python :: 2",
    ],
    tests_require=[
        "nose",
    ],
    setup_requires=[
        "IPython>=3.0.0,<4.0.0",
        "requests",
    ],
    install_requires=[
        "IPython>=3.0.0,<4.0.0",
    ],
    test_suite='nose.collector',
    cmdclass=cmdclass('{{ cookiecutter.pkg_name }}/static/{{ cookiecutter.pkg_name }}')
)
