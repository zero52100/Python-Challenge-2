class Student:
    def __init__(self, name, height):
        self.name = name
        self.height = height

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_records(self):
        if not self.students:
            print("No student records available.")
        else:
            for student in self.students:
                print(f"{student.name}: {student.height} cm")

    def sort_by_height(self):
        self.students.sort(key=lambda x: x.height)

school = School()

while True:
    try:
        total_students = int(input("Enter the total number of students: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

for i in range(total_students):
    name = input(f"Enter name of student {i+1}: ")
    while True:
        try:
            height = int(input(f"Enter height of student {i+1} (in cm): "))
            break
        except ValueError:
            print("Invalid input for height. Please enter a numeric value.")

    student = Student(name, height)
    
    school.add_student(student)

school.sort_by_height()

print("\nSorted Student Height Records:")
school.display_records()
