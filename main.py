"""Student Result Management System
A short CLI project: add students, enter marks, calculate GPA/grade,
search, and view a ranked result sheet. Data is saved in students.json.
"""
import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.json")


def load():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def grade_point(mark):
    """Bangladesh university-style 4.0 scale."""
    if mark >= 80: return "A+", 4.00
    if mark >= 75: return "A", 3.75
    if mark >= 70: return "A-", 3.50
    if mark >= 65: return "B+", 3.25
    if mark >= 60: return "B", 3.00
    if mark >= 55: return "B-", 2.75
    if mark >= 50: return "C+", 2.50
    if mark >= 45: return "C", 2.25
    if mark >= 40: return "D", 2.00
    return "F", 0.00


def gpa(student):
    marks = student["marks"]
    if not marks:
        return 0.0
    points = [grade_point(m)[1] for m in marks.values()]
    return round(sum(points) / len(points), 2)


def read_mark(prompt):
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 100:
                return value
        except ValueError:
            pass
        print("  Please enter a number between 0 and 100.")


def add_student(data):
    sid = input("Student ID: ").strip()
    if not sid:
        return print("  ID cannot be empty.")
    if sid in data:
        return print("  This ID already exists.")
    data[sid] = {"name": input("Name: ").strip(), "marks": {}}
    save(data)
    print("  Student added.")


def add_marks(data):
    sid = input("Student ID: ").strip()
    if sid not in data:
        return print("  Student not found.")
    course = input("Course name: ").strip()
    data[sid]["marks"][course] = read_mark("Marks (0-100): ")
    save(data)
    print("  Marks saved.")


def show_student(data):
    sid = input("Student ID: ").strip()
    s = data.get(sid)
    if not s:
        return print("  Student not found.")
    print(f"\n{s['name']} ({sid})")
    print(f"{'Course':<20}{'Marks':>7}{'Grade':>7}{'GP':>6}")
    for course, m in s["marks"].items():
        g, gp = grade_point(m)
        print(f"{course:<20}{m:>7.1f}{g:>7}{gp:>6.2f}")
    print(f"GPA: {gpa(s):.2f}")


def merit_list(data):
    ranked = sorted(data.items(), key=lambda kv: gpa(kv[1]), reverse=True)
    print(f"\n{'Rank':<6}{'ID':<12}{'Name':<20}{'GPA':>5}")
    for i, (sid, s) in enumerate(ranked, 1):
        print(f"{i:<6}{sid:<12}{s['name']:<20}{gpa(s):>5.2f}")


def main():
    data = load()
    actions = {
        "1": ("Add student", add_student),
        "2": ("Add/update marks", add_marks),
        "3": ("View student result", show_student),
        "4": ("Merit list", merit_list),
    }
    while True:
        print("\n=== Student Result System ===")
        for k, (label, _) in actions.items():
            print(f"{k}. {label}")
        print("0. Exit")
        choice = input("Choose: ").strip()
        if choice == "0":
            break
        if choice in actions:
            actions[choice][1](data)
        else:
            print("  Invalid choice.")


if __name__ == "__main__":
    main()
