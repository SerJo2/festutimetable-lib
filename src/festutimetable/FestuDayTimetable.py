from .Lecture import Lecture

class FestuDayTimetable:
    def __init__(self, date, lectures: list[Lecture]):
        self.lectures = lectures
        self.date = date

    def append_lecture(self, lecture):
        self.lectures.append(lecture)

    def print(self):
        for i in self.lectures:
            print(i.date)
            print(i.name)