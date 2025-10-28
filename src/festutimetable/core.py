from .FestuDayTimetable import FestuDayTimetable



class Utils:
    @staticmethod
    def get_timetable_by_day(day: str, timetable: FestuDayTimetable):
        for i in timetable.day_timetables:
            if i.day == "day":
                return i
        return None

