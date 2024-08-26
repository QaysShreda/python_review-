from models import SchoolManagementSystem


def main():
    sms = SchoolManagementSystem()

    while True:
        print("\nSchool Management System")
        print("1. Enroll Student")
        print("2. Add Course")
        print("3. Register Student in Course")
        print("4. Assign Grade")
        print("5. View Student Grades")
        print("6. Generate Transcript")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            sms.enroll_student(name, student_id)

        elif choice == "2":
            course_name = input("Enter course name: ")
            course_code = input("Enter course code: ")
            sms.add_course(course_name, course_code)

        elif choice == "3":
            student_id = input("Enter student ID: ")
            course_code = input("Enter course code: ")
            sms.register_student_in_course(student_id, course_code)

        elif choice == "4":
            student_id = input("Enter student ID: ")
            course_code = input("Enter course code: ")
            grade = input("Enter grade: ")
            sms.assign_grade(student_id, course_code, grade)

        elif choice == "5":
            student_id = input("Enter student ID: ")
            sms.view_student_grades(student_id)

        elif choice == "6":
            student_id = input("Enter student ID: ")
            sms.generate_transcript(student_id)

        elif choice == "7":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

