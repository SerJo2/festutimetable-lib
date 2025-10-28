class Lecture:
    """Class for SINGLE lecture

    """
    def __init__(self, group: str, number: int, time: str, name: str, classroom: str, teacher: str, date: str):
        """Initialize a Lecture


        Args:
            group: group name
            number: number of lecture
            time: time when lecture is on
            name: name of lecture
            classroom: classroom of lecture
            teacher: teacher
            date: date
        """
        self.group = group
        self.date = date
        self.number = number
        self.time = time
        self.name = name
        self.classroom = classroom
        self.teacher = teacher

    def print(self):
        """Print a lectures (WIP)

        """
        print(self.group)
        print(self.date)
        print(self.number)
        print(self.time)
        print(self.name)
        print(self.classroom)
        print(self.teacher)

