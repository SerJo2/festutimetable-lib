from .FestuDayTimetable import FestuDayTimetable

class FestuTimetable:
    def __init__(self, day_timetables: list[FestuDayTimetable]):
        self.day_timetables = day_timetables

    def append(self, table: FestuDayTimetable):
        self.day_timetables.append(table)

    def print(self):
        for i in self.day_timetables:
            print(i.date)
            for j in i.lectures:
                print(j.name)

