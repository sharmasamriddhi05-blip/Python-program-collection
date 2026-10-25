"""
Structure-to-Dictionary conversion.

In C you would store related data in a `struct`:

    struct Student { char name[50]; int roll_no; float marks; };

Python does not have `struct`, but a class (or a dataclass) does the same job.
A dictionary stores the same data as key-value pairs, which is easy to print,
save as JSON, or send over the internet.

This program shows three ways to convert a "structure" into a dictionary.
"""

import json
from dataclasses import dataclass, asdict


# ---------- Method 1: a normal class, converted by hand ----------
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def to_dict(self):
        """Build the dictionary ourselves, key by key."""
        return {
            "name": self.name,
            "roll_no": self.roll_no,
            "marks": self.marks,
        }


# ---------- Method 2: a dataclass, converted with asdict() ----------
@dataclass
class Book:
    title: str
    author: str
    pages: int


# ---------- Method 3: any object, using its built-in __dict__ ----------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    # Method 1
    student = Student("Riya", 101, 87.5)
    student_dict = student.to_dict()
    print("Method 1 (manual to_dict):", student_dict)

    # Method 2
    book = Book("Python Basics", "A. Author", 250)
    book_dict = asdict(book)
    print("Method 2 (dataclass asdict):", book_dict)

    # Method 3
    point = Point(3, 4)
    point_dict = vars(point)          # same as point.__dict__
    print("Method 3 (vars / __dict__):", point_dict)

    # Bonus: once it is a dictionary, converting to JSON text is one line
    print("\nStudent as JSON text:")
    print(json.dumps(student_dict, indent=2))

    # Bonus: reading values back from the dictionary
    print("\nStudent name from the dictionary:", student_dict["name"])


if __name__ == "__main__":
    main()
