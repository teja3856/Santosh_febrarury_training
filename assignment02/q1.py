class User:
    def __init__(self, user_id, name, email):
        self.__user_id = user_id
        self.__name = name
        self.__email = email

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def display_details(self):
        print(f"ID: {self.__user_id}")
        print(f"Name: {self.__name}")
        print(f"Email: {self.__email}")


class Student(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.__courses = []
        self.__mentor = None

    def enroll_course(self, course):
        self.__courses.append(course)
        print("Course enrolled successfully!")

    def assign_mentor(self, mentor):
        self.__mentor = mentor

    def get_mentor(self):
        return self.__mentor

    def display_details(self):
        print("\n----- Student Details -----")
        super().display_details()
        print("Courses:", self.__courses if self.__courses else "None")
        if self.__mentor:
            print("Mentor:", self.__mentor.get_name())
        else:
            print("Mentor: Not Assigned")


class Mentor(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.__assigned_students = []

    def assign_student(self, student):
        self.__assigned_students.append(student)

    def view_students(self):
        print("\n--- Assigned Students ---")
        if not self.__assigned_students:
            print("No students assigned.")
        else:
            for student in self.__assigned_students:
                print(student.get_name())

    def display_details(self):
        print("\n----- Mentor Details -----")
        super().display_details()
        print("Assigned Students:", len(self.__assigned_students))


class Admin(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)

    def view_all_students(self, students):
        print("\n===== All Students =====")
        if not students:
            print("No students available.")
        else:
            for student in students:
                student.display_details()

    def view_all_mentors(self, mentors):
        print("\n===== All Mentors =====")
        if not mentors:
            print("No mentors available.")
        else:
            for mentor in mentors:
                mentor.display_details()


students = []
mentors = []

admin = Admin("A1", "System Admin", "admin@edtech.com")

while True:
    print("\n====== EdTech Management System ======")
    print("1. Add Student")
    print("2. Add Mentor")
    print("3. Enroll Student in Course")
    print("4. Assign Mentor to Student")
    print("5. Mentor View Assigned Students")
    print("6. Admin View All Students")
    print("7. Admin View All Mentors")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sid = input("Enter Student ID: ")
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        student = Student(sid, name, email)
        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        mid = input("Enter Mentor ID: ")
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        mentor = Mentor(mid, name, email)
        mentors.append(mentor)
        print("Mentor added successfully!")

    elif choice == "3":
        sid = input("Enter Student ID: ")
        course = input("Enter Course Name: ")
        found = False
        for student in students:
            if student.get_user_id() == sid:
                student.enroll_course(course)
                found = True
                break
        if not found:
            print("Student not found!")

    elif choice == "4":
        sid = input("Enter Student ID: ")
        mid = input("Enter Mentor ID: ")

        student_obj = None
        mentor_obj = None

        for student in students:
            if student.get_user_id() == sid:
                student_obj = student

        for mentor in mentors:
            if mentor.get_user_id() == mid:
                mentor_obj = mentor

        if student_obj and mentor_obj:
            student_obj.assign_mentor(mentor_obj)
            mentor_obj.assign_student(student_obj)
            print("Mentor assigned successfully!")
        else:
            print("Invalid ID(s)!")

    elif choice == "5":
        mid = input("Enter Mentor ID: ")
        found = False
        for mentor in mentors:
            if mentor.get_user_id() == mid:
                mentor.view_students()
                found = True
                break
        if not found:
            print("Mentor not found!")

    elif choice == "6":
        admin.view_all_students(students)

    elif choice == "7":
        admin.view_all_mentors(mentors)

    elif choice == "8":
        print("Exiting system...")
        break

    else:
        print("Invalid choice! Please try again.")
