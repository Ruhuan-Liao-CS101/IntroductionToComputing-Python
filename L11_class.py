"""
registrar office needs to handle:

students => Student class
Attributes/fields:
- first_name 
- last_name
- year
- major
- student_id
Methods (they represent the "behavior" of the student class -- functions)
- print_student_info()
- add_class()
- check_pre_reqs()

courses => Course class
- time
- name
- id

professors => Professor class
"""

class Student:
    # special method (init) called constructor 
    def __init__(self, first_name, last_name, student_id): 
        # set attributes/fields
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.courses = []

    def print_student_info(self):
        print("First name: ", self.first_name)
        print("Last name: ", self.last_name)
        print("Student ID: ", self.student_id)
        try:
            print("Student's major: ", self.major)
        except AttributeError:
            pass
 
    def set_major(self, major):
        # set a major for the student
        self.major = major
    
    def add_course(self, course):
        self.courses.append(course)

    #method that returns the list of courses
    def get_courses(self):
        return self.courses
        
#creating objects
student1 = Student( "Jill", "Land", 333222 )
student1.print_student_info()
student1.set_major("CS")

student2 = Student("Maggie", "Harper", 123123)
student2.print_student_info()
