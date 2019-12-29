"""Set up the environment for doctests

This file is automatically evaluated by py.test. It ensures that we can write
doctests without distracting import statements in the doctest.
"""
import pytest

import pypkg_rtd_02


@pytest.fixture(autouse=True)
def set_doctest_env(doctest_namespace):
    doctest_namespace['pypkg_rtd_02'] = pypkg_rtd_02
