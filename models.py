class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = {}

    def add_course(self, course_name, grade=None):
        self.courses[course_name] = grade

    def update_grade(self, course_name, grade):
        if course_name in self.courses:
            self.courses[course_name] = grade

    def get_grades(self):
        return self.courses


class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.enrolled_students = []

    def enroll_student(self, student):
        self.enrolled_students.append(student)




class SchoolManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def enroll_student(self, name, student_id):
        student = Student(name, student_id)
        self.students.append(student)
        print(f"Student {name} enrolled successfully.")

    def register_student_in_course(self, student_id, course_code):
        student = self.find_student(student_id)
        course = self.find_course(course_code)

        if student and course:      #  None , None      
            course.enroll_student(student)
            student.add_course(course.course_name)
            print(f"Student {student.name} registered in {course.course_name} successfully.")
        else:
            print("Student or course not found.")

    def assign_grade(self, student_id, course_code, grade):
        student = self.find_student(student_id)
        course = self.find_course(course_code)

        if student and course:
            student.update_grade(course.course_name, grade)
            print(f"Grade {grade} assigned to {student.name} for {course.course_name}.")
        else:
            print("Student or course not found.")

    def view_student_grades(self, student_id):
        student = self.find_student(student_id)
        if student:
            grades = student.get_grades()
            if grades:
                print(f"Grades for {student.name}:")
                for course, grade in grades.items():
                    print(f"{course}: {grade}")
            else:
                print(f"No grades available for {student.name}.")
        else:
            print("Student not found.")

    def generate_transcript(self, student_id):
        student = self.find_student(student_id)
        if student:
            print(f"Transcript for {student.name}:")
            grades = student.get_grades()
            for course, grade in grades.items():
                print(f"{course}: {grade}")
        else:
            print("Student not found.")

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def find_course(self, course_code):
        for course in self.courses:
            if course.course_code == course_code:
                return course
        return None

    def add_course(self, course_name, course_code):
        course = Course(course_name, course_code)
        self.courses.append(course)
        print(f"Course {course_name} added successfully.")

    def find_students_with_all_A_grades(self):
        students_with_all_As = []
        for student in self.students:
            if all(grade == "A" for grade in student.courses.values()):
                students_with_all_As.append(student)
        return students_with_all_As
