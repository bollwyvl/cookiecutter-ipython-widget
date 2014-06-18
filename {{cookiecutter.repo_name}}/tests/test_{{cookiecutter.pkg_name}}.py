#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.pkg_name }}
----------------------------------

Tests for `{{ cookiecutter.pkg_name }}` module.
"""
import sys
import unittest

sys.path.append("..")

from {{ cookiecutter.pkg_name }} import widgets


class Test{{ cookiecutter.repo_name|capitalize }}(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
