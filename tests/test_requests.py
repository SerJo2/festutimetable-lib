from importlib.metadata import version
import pytest

from src.festutimetable import FestuApi


def test_get_2week_timetable():
    result = FestuApi.TimetableService()
    x = result.get_2week_timetable("БО911ПИА", "29.10.2025")
    assert x is not None

def test_get_1day_timetable_by_teacher():
    result = FestuApi.TimetableService()
    x = result.get_timetable_by_day_by_teacher(3857, '14.01.2026')
    assert x is not None