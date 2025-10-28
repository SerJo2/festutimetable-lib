from dataclasses import dataclass
from typing import Optional

import requests
from bs4 import BeautifulSoup
from .FestuDayTimetable import FestuDayTimetable
from .FestuTimetable import FestuTimetable
from .Lecture import Lecture
from .GroupIds import group_ids


@dataclass
class RequestConfig:
    base_url: str = "https://dvgups.ru"
    endpoint: str = "/index.php"
    timeout: int = 15
    params: dict = None

    def __post_init__(self):
        if self.params is None:
            self.params = {
                'Itemid': '1246',
                'option': 'com_timetable',
                'view': 'newtimetable',
            }

class TimetableService:
    """Main class for action with FESTU api


    """
    def __init__(self):
        """Initialize TimetableService

        Initialize client and parser

        """
        self.client = TimetableClient()
        self.parser = TimetableParser()

    def get_2week_timetable(self, group: str, date: str) -> FestuTimetable:
        """Get a 2week timetable from FESTU site

        Important:
        Returns the timetable not from the current date,
        but from the start of the previous/current week
        (the two-week countdown starts on September 1st).

        Args:
            group (str): Abbreviated name of the group (Like: "БО911ПИА")
            date (str): The date for which you need to get the timetable

        Returns:
            FestuTimetable: Timetable object

        Raises:
            ValueError: If date format is invalid

        """
        if not self._is_valid_date(date):
            raise ValueError(f"Invalid date format: {date}. Use DD.MM.YYYY")
        fetched_timetable = self.client.fetch_timetable(group, date)
        parsed_timetable = self.parser.parse_2weeks(fetched_timetable)
        return parsed_timetable

    def get_timetable_by_day(self, group: str, date: str) -> FestuDayTimetable:
        """Get a single day timetable from FESTU site

        Args:
            group: Abbreviated name of the group (Like: "БО911ПИА")
            date: The date for which you need to get the timetable

        Returns:
            FestuDayTimetable: return a FestuDayTimetable for day

        Raises:
            ValueError: If date format is invalid
            DateNotFoundError: If timetable for date not found

        """
        if not self._is_valid_date(date):
            raise ValueError(f"Invalid date format: {date}. Use DD.MM.YYYY")

        try:
            fetched_timetable = self.client.fetch_timetable(group, date)
            return self.parser.parse_1day(fetched_timetable, date)
        except ValueError as e:
            raise DateNotFoundError(f"Timetable for date {date} not found") from e

    def _is_valid_date(self, date: str) -> bool:
        """Checks the date for valid

        Args:
            date: date for check

        Returns: Is date a valid

        """
        import re
        return bool(re.match(r'^\d{2}\.\d{2}\.\d{4}$', date))




class TimetableParser:
    """Class for parsing html for timetable Class

    """
    def _parse_lesson_row(self, cells, date: str) -> Lecture:
        """Parse table for 1 lesson

        Args:
            cells: Number of cells
            date: Date

        Returns:
            Lecture: Return a single Lecture Class

        """
        time = name = classroom = groups = teacher = ""

        for i, cell in enumerate(cells):
            text = cell.text.strip()
            match i:
                case 0:
                    time = text
                case 1:
                    name = text
                case 2:
                    classroom = text
                case 3:
                    groups = text
                case 4:
                    teacher = text

        return Lecture(
            number=time,
            group=groups,
            time=time,
            name=name,
            classroom=classroom,
            teacher=teacher,
            date=date
        )

    def _parse_day_table(self, table, date: str) -> FestuDayTimetable:
        """Parse table for 1 day

        Args:
            table: table for parse
            date: date

        Returns:
            object:
        """
        day_timetable = FestuDayTimetable(date, [])
        lessons = table.find_all('tr')

        for lesson_row in lessons:
            cells = lesson_row.find_all("td")
            if cells:  # проверяем что есть ячейки
                lecture = self._parse_lesson_row(cells, date)
                day_timetable.append_lecture(lecture)

        return day_timetable

    def parse_2weeks(self, html: str) -> FestuTimetable:
        """Parse 2week timetable

        Args:
            html: html for parse

        Returns:
            FestuTimetable: FestuTimetable object

        """
        root = BeautifulSoup(html, 'html.parser')
        all_dates = [h3.text[:10] for h3 in root.find_all('h3')]
        tables_by_day = root.find_all('table')

        timetable = FestuTimetable([])
        for date, table in zip(all_dates, tables_by_day):
            day_timetable = self._parse_day_table(table, date)
            timetable.append(day_timetable)

        return timetable

    def parse_1day(self, html: str, target_date: str) -> FestuDayTimetable:
        """Parse HTML to extract timetable for a specific day

        Args:
            html: HTML content to parse
            target_date: Target date in DD.MM.YYYY format to find in the timetable

        Returns:
            FestuDayTimetable: Timetable object for the specified day

        Raises:
            ValueError: If the target date is not found in the HTML content
        """
        root = BeautifulSoup(html, 'html.parser')
        all_dates = [h3.text[:10] for h3 in root.find_all('h3')]
        tables_by_day = root.find_all('table')

        for date, table in zip(all_dates, tables_by_day):
            if date == target_date:
                return self._parse_day_table(table, date)

        raise ValueError(f"Date {target_date} not found in timetable")


class TimetableClient:
    """Class for requests from site

    """
    def __init__(self, config: Optional[RequestConfig] = None):
        """

        Args:
            config: optional config (Don't recommend changing it)
        """
        self.config = config or RequestConfig()
        self.session = requests.Session()
        self._setup_headers()

    def _setup_headers(self):
        """Setup headers

        """
        self.session.headers.update({
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        })

    def fetch_timetable(self, group: str, date: str) -> str:
        """Fetching timetable from site

        Args:
            group: Abbreviated name of the group (Like: "БО911ПИА")
            date: The date for which you need to get the timetable

        Returns:
            str: fetched html

        """
        data = {
            'GroupID': self._get_group_id(group),
            'Time': date,
        }

        try:
            response = self.session.post(
                url=self.config.base_url + self.config.endpoint,
                params=self.config.params,
                data=data,
                timeout=self.config.timeout
            )
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            raise RequestError(f"Failed to fetch timetable for group {group}: {e}") from e

    def _get_group_id(self, group: str) -> str:
        """Gets an id from a dictionary given a group name.

        Args:
            group: Abbreviated name of the group (Like: "БО911ПИА")

        Returns:
            str: group id
            
        Raises:
            GroupNotFoundError: If group isn't in dict. If you are sure that
            the group exists in reality, then open the issue

        """
        if group not in group_ids:
            raise GroupNotFoundError(f"Unknown group: {group}")
        return group_ids[group]


class TimetableError(Exception):
    pass

class RequestError(TimetableError):
    pass

class DateNotFoundError(TimetableError):
    pass

class GroupNotFoundError(TimetableError):
    pass

