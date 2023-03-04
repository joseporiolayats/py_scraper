#!/usr/bin/env python
"""Tests for `py_scraper` package."""
import pytest

from py_scraper import py_scraper


@pytest.fixture
def dummy_fixture():
    """Dummy fixture to avoid import error."""
    return 'REPLACE ME!'


def test_has_metadata():
    """Test if package has metadata."""
    assert hasattr(py_scraper, '__author__')
    assert hasattr(py_scraper, '__email__')
    assert hasattr(py_scraper, '__version__')
