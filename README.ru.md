# 🎓 FESTU Timetable Library

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://img.shields.io/pypi/v/festutimetable.svg)](https://pypi.org/project/festutimetable/)

[English](https://github.com/SerJo2/festutimetable-lib/blob/master/README.ru.md) | Russian

Библиотека для удобного получения и работы с расписанием занятий ДВГУПС (FESTU).

## ✨ Особенности

- 🚀 Простой и интуитивно понятный API
- 📅 Получение расписания на день и на две недели
- 🏫 Поддержка всех групп университета
- 🛡️ Полная типизация и обработка ошибок
- 📚 Подробная документация

## 📦 Установка

```bash
pip install festutimetable
```
## 🚀 Быстрый старт

### Получение расписания на день
```python
python
from festutimetable import TimetableService

service = TimetableService()

# Получить расписание на конкретный день
timetable = service.get_timetable_by_day("БО911ПИА", "29.10.2025")

# Вывести расписание
timetable.print()
```
### Получение расписания на две недели
```python
from festutimetable import TimetableService

service = TimetableService()

# Получить расписание на две недели
two_week_timetable = service.get_2week_timetable("БО911ПИА", "29.10.2025")

# Вывести расписание
two_week_timetable.print()

```

## 🐛 Поиск и отчетность об ошибках
Если вы обнаружили ошибку или у вас есть предложение по улучшению, создайте [issue](https://github.com/SerJo2/festutimetable-lib/issues) на GitHub.

## 🤝 Разработка

Установка для разработки
```bash
git clone https://github.com/SerJo2/festutimetable.git
cd festutimetable
```

## 📄 Лицензия
Этот проект распространяется под лицензией MIT. Подробнее см. в файле [LICENSE](https://github.com/SerJo2/festutimetable-lib/blob/master/LICENSE).


## 👨‍💻 Автор
#### Onii-Chan
 - Email: skobochki.ad@mail.ru
 - GitHub: [SerJo2](https://github.com/SerJo2)

## ⭐ Не забудьте поставить звезду на GitHub, если проект вам помог!