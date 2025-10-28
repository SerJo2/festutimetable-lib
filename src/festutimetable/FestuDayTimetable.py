from .Lecture import Lecture

class FestuDayTimetable:
    """Class for store Timetable for ONE day

    """
    def __init__(self, date: str, lectures: list[Lecture]):
        """Initialize a FestuDayTimetable

        Args:
            date (str): date of day
            lectures (list[Lecture]): List of lectures, may be empty
        """
        self.lectures = lectures
        self.date = date

    def append_lecture(self, lecture: Lecture):
        """Append a new lecture to list of lectures

        Args:
            lecture (Lecture):

        """
        self.lectures.append(lecture)

    def print(self):
        """Print a lectures (WIP)

        """
        for i in self.lectures:
            print(i.date)
            print(i.name)