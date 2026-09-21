class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = {}

    def add_grade(self, subject, mark):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(mark)

    def average(self):
        all_marks = []
        for marks in self.grades.values():
            all_marks.extend(marks)
        if not all_marks:
            return 0
        return sum(all_marks) / len(all_marks)

    def __str__(self):
        return f"{self.name} (Roll: {self.roll_number}) - Avg: {self.average():.2f}"


if __name__ == "__main__":
    s1 = Student("Aisha", "22-SE-01")
    s1.add_grade("Math", 85)
    s1.add_grade("Math", 90)
    s1.add_grade("Physics", 78)

    print(s1)
    print("Math marks:", s1.grades["Math"])
    print("Physics marks:", s1.grades["Physics"])