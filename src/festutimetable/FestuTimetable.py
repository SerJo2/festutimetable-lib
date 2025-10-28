from .FestuDayTimetable import FestuDayTimetable

class FestuTimetable:
    """Class for store Timetables for MANY days

    """
    def __init__(self, day_timetables: list[FestuDayTimetable]):
        """Initialize a FestuTimetable

        Args:
            day_timetables (list[FestuDayTimetable]): List of FestuDayTimetable objects, may be empty
        """
        self.day_timetables = day_timetables

    def append(self, table: FestuDayTimetable):
        """Append a new day to list of timetables

                Args:
                    table (FestuDayTimetable): FestuDayTimetable object

                """
        self.day_timetables.append(table)

    def print(self):
        """Print a lectures (WIP)

        """
        for i in self.day_timetables:
            print(i.date)
            for j in i.lectures:
                print(j.name)

