import json

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")


class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject, grade):
        if subject in self.courses:
            self.grades[subject] = grade
            print(f"Grade {grade} added for {subject} for student {self.name}")
        else:
            print(f"Student {self.name} is not enrolled in {subject}.")

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"Student {self.name} enrolled in {course}")
        else:
            print(f"Student {self.name} is already enrolled in {course}.")

    def display_student_info(self):
        self.display_person_info()
        print(f"Student ID: {self.student_id}")
        print(f"Enrolled Courses: {self.courses}")
        print(f"Grades: {self.grades}")


class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"Student {student} added to course {self.course_name}")
        else:
            print(f"Student {student} is already enrolled in {self.course_name}.")

    def display_course_info(self):
        print(f"Course Name: {self.course_name}, Course Code: {self.course_code}, Instructor: {self.instructor}")
        print("Enrolled Students:", self.students)


class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self):
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        address = input("Enter Address: ")
        student_id = input("Enter Student ID: ")
        student = Student(name, age, address, student_id)
        self.students[student_id] = student
        print(f"Student {name} (ID: {student_id}) added successfully")

    def add_course(self):
        course_name = input("Enter Course Name: ")
        course_code = input("Enter Course Code: ")
        instructor = input("Enter Instructor Name: ")
        course = Course(course_name, course_code, instructor)
        self.courses[course_code] = course
        print(f"Course {course_name} (Code: {course_code}) added successfully")

    def enroll_student_in_course(self):
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")

        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course = self.courses[course_code]
            student.enroll_course(course_code)
            course.add_student(student_id)
        else:
            print("Invalid Student ID or Course Code.")

    def add_grade_for_student(self):
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")
        grade = input("Enter Grade: ")

        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            if course_code in student.courses:
                student.add_grade(course_code, grade)
            else:
                print("Student is not enrolled in this course.")
        else:
            print("Invalid Student ID or Course Code.")

    def display_student_details(self):
        student_id = input("Enter Student ID: ")
        if student_id in self.students:
            self.students[student_id].display_student_info()
        else:
            print("Student not found.")

    def display_course_details(self):
        course_code = input("Enter Course Code: ")
        if course_code in self.courses:
            self.courses[course_code].display_course_info()
        else:
            print("Course not found.")

    def save_data(self):
        data = {
            "students": {
                student_id: {
                    "name": student.name,
                    "age": student.age,
                    "address": student.address,
                    "student_id": student.student_id,
                    "grades": student.grades,
                    "courses": student.courses
                } for student_id, student in self.students.items()
            },
            "courses": {
                course_code: {
                    "course_name": course.course_name,
                    "course_code": course.course_code,
                    "instructor": course.instructor,
                    "students": course.students
                } for course_code, course in self.courses.items()
            }
        }
        with open("student_management_data.json", "w") as file:
            json.dump(data, file)
        print("Data saved successfully.")

    def load_data(self):
        try:
            with open("student_management_data.json", "r") as file:
                data = json.load(file)
            for student_id, info in data["students"].items():
                student = Student(info["name"], info["age"], info["address"], student_id)
                student.grades = info["grades"]
                student.courses = info["courses"]
                self.students[student_id] = student
            for course_code, info in data["courses"].items():
                course = Course(info["course_name"], info["course_code"], info["instructor"])
                course.students = info["students"]
                self.courses[course_code] = course
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No saved data found.")

    def run(self):
        while True:
            print("\n==== Student Management System ====")
            print("1. Add New Student")
            print("2. Add New Course")
            print("3. Enroll Student in Course")
            print("4. Add Grade for Student")
            print("5. Display Student Details")
            print("6. Display Course Details")
            print("7. Save Data to File")
            print("8. Load Data from File")
            print("0. Exit")
            option = input("Select Option: ")

            if option == "1":
                self.add_student()
            elif option == "2":
                self.add_course()
            elif option == "3":
                self.enroll_student_in_course()
            elif option == "4":
                self.add_grade_for_student()
            elif option == "5":
                self.display_student_details()
            elif option == "6":
                self.display_course_details()
            elif option == "7":
                self.save_data()
            elif option == "8":
                self.load_data()
            elif option == "0":
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.run()
