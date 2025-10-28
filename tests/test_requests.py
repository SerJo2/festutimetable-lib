from importlib.metadata import version
import pytest

from src.festutimetable import FestuApi


def test_get_2week_timetable():
    result = FestuApi.get_2weeks_timetable("БО911ПИА", "29.10.2025")
    assert result is not None
