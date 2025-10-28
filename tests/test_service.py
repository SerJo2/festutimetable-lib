import pytest
from unittest.mock import Mock

from src.festutimetable import TimetableService


def test_timetable_service():
    mock_client = Mock()
    mock_parser = Mock()

    service = TimetableService()
    service.client = mock_client
    service.parser = mock_parser

    result = service.get_2week_timetable("БО911ПИА", "29.10.2025")

    mock_client.fetch_timetable.assert_called_once_with("БО911ПИА", "29.10.2025")
    mock_parser.parse_2weeks.assert_called_once()