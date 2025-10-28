# 🎓 FESTU Timetable Library

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Лицензия: MIT](https://img.shields.io/badge/Лицензия-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Версия PyPI](https://img.shields.io/pypi/v/festutimetable.svg)](https://pypi.org/project/festutimetable/)
[![Скачивания PyPI](https://img.shields.io/pypi/dm/festutimetable.svg)](https://pypi.org/project/festutimetable/)
English | [Russian](https://github.com/SerJo2/festutimetable-lib/blob/master/README.ru.md)

A Python library for easy access and manipulation of FESTU (Far Eastern State Transport University) class schedules.

## ✨ Features

- 🚀 Simple and intuitive API
- 📅 Get daily and bi-weekly schedules
- 🏫 Support for all university groups
- 🛡️ Full type annotations and error handling
- 📚 Comprehensive documentation

## 📦 Installation

```bash
pip install festutimetable
```

## 🚀 Quick Start
Get Daily Schedule
```python
from festutimetable import TimetableService

service = TimetableService()

# Get schedule for a specific day
timetable = service.get_timetable_by_day("БО911ПИА", "29.10.2025")

# Print the schedule
timetable.print()
```
Get Bi-Weekly Schedule
```python
from festutimetable import TimetableService

service = TimetableService()

# Get schedule for two weeks
two_week_timetable = service.get_2week_timetable("БО911ПИА", "29.10.2025")

# Print the schedule
two_week_timetable.print()
```

## 🐛 Bug Reports and Issues
If you find a bug or have a feature request, please create an issue on GitHub.

## 🤝 Development
Development Installation
```bash
git clone https://github.com/SerJo2/festutimetable.git
cd festutimetable
```
Running Tests
```bash
pytest tests/ -v
```
## 📄 License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/SerJo2/festutimetable-lib/blob/master/LICENSE) file for details.

## 👨‍💻 Author
#### Onii-Chan
- Email: skobochki.ad@mail.ru
- GitHub: [SerJo2](https://github.com/SerJo2)
## ⭐ If this project helped you, please give it a star on GitHub!

