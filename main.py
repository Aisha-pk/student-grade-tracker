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
def show_menu():
    print("\n=== Student Grade Tracker ===")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. View All Students")
    print("4. Find Student")
    print("5. Remove Student")
    print("6. Exit")
def handle_add_student(tracker):
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    if tracker.find_student(roll):
        print("A student with this roll number already exists!")
        return
    tracker.add_student(name, roll)
    print(f"Student {name} added.")


def handle_add_grade(tracker):
    roll = input("Enter student roll number: ")
    student = tracker.find_student(roll)
    if not student:
        print("Student not found.")
        return
    subject = input("Enter subject: ")
    try:
        mark = float(input("Enter mark: "))
    except ValueError:
        print("Invalid mark. Please enter a number.")
        return
    student.add_grade(subject, mark)
    print(f"Grade added for {student.name}.")


def handle_view_all(tracker):
    students = tracker.list_all()
    if not students:
        print("No students yet.")
        return
    print("\n--- All Students ---")
    for s in students:
        print(s)


def handle_find(tracker):
    roll = input("Enter roll number to find: ")
    student = tracker.find_student(roll)
    if student:
        print(student)
        print("Grades:", student.grades)
    else:
        print("Student not found.")


def handle_remove(tracker):
    roll = input("Enter roll number to remove: ")
    if tracker.remove_student(roll):
        print("Student removed.")
    else:
        print("Student not found.")
if __name__ == "__main__":
    tracker = Tracker()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            handle_add_student(tracker)
        elif choice == "2":
            handle_add_grade(tracker)
        elif choice == "3":
            handle_view_all(tracker)
        elif choice == "4":
            handle_find(tracker)
        elif choice == "5":
            handle_remove(tracker)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")