# Student Result Management System

A short Python CLI project for a university course (CSE/IT).

## Features
- Add students (ID + name)
- Add/update marks per course
- Automatic letter grade and GPA (4.0 scale)
- Merit list sorted by GPA
- Data stored in `students.json` (file handling + JSON)

## Run
```
python main.py
```
No external libraries needed (Python 3.8+).

## Concepts used
Functions, dictionaries, file I/O, JSON, input validation, sorting with `sorted(key=...)`.

## Possible extensions
- Add a GUI with Tkinter
- Switch storage to SQLite
- Export result sheet to PDF/CSV
