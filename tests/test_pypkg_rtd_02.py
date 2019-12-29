"""Tests for `pypkg_rtd_02` package."""

import pytest
from pkg_resources import parse_version

import pypkg_rtd_02


def test_valid_version():
    """Check that the package defines a valid ``__version__``."""
    v_curr = parse_version(pypkg_rtd_02.__version__)
    v_orig = parse_version("0.1.0-dev")
    assert v_curr >= v_orig
