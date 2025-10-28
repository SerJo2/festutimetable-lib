class Lecture:
    def __init__(self, group: str, number: int, time: str, name: str, classroom: str, teacher: str, date: str):
        """

        Группа
        Дата
        № пары
        Время пары
        Тип + Название пары
        Аудитория
        Препод
        Доп инфа


        """
        self.group = group
        self.date = date
        self.number = number
        self.time = time
        self.name = name
        self.classroom = classroom
        self.teacher = teacher

    def print(self):
        print(self.group)
        print(self.date)
        print(self.number)
        print(self.time)
        print(self.name)
        print(self.classroom)
        print(self.teacher)

