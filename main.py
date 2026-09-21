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
class Tracker:
    def __init__(self):
        self.students = []  # list of Student objects

    def add_student(self, name, roll_number):
        """Create a Student and add to the list. Return the new student."""
        new_student = Student(name, roll_number)
        self.students.append(new_student)
        return new_student

    def find_student(self, roll_number):
        """Find a student by roll number. Returns None if not found."""
        for student in self.students:
            if student.roll_number == roll_number:
                return student
        return None

    def list_all(self):
        """Return the list of all students."""
        return self.students

    def remove_student(self, roll_number):
        """Remove a student by roll number. Returns True if removed."""
        student = self.find_student(roll_number)
        if student:
            self.students.remove(student)
            return True
        return False

if __name__ == "__main__":
    tracker = Tracker()

    tracker.add_student("Aisha", "22-SE-01")
    tracker.add_student("Bob", "22-SE-02")

    # Add grades
    aisha = tracker.find_student("22-SE-01")
    aisha.add_grade("Math", 85)
    aisha.add_grade("Math", 90)
    aisha.add_grade("Physics", 78)

    bob = tracker.find_student("22-SE-02")
    bob.add_grade("Math", 75)
    bob.add_grade("Physics", 88)

    # List everyone
    print("--- All Students ---")
    for s in tracker.list_all():
        print(s)

    # Test remove
    tracker.remove_student("22-SE-02")
    print("\n--- After removing Bob ---")
    for s in tracker.list_all():
        print(s)