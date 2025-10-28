from importlib.metadata import version
import pytest
from src import festutimetable


def test_import():
    assert festutimetable is not None

def test_version():
    from importlib.metadata import version
    pkg_version = version("festutimetable")
    assert pkg_version is not None