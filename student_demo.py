"""
registrar office needs to handle

students => Student class
Attributes/fields:
- first_name
- last_name
- year
- major
- student_id
methods (they represent the "behavior" of the student class)
- print_student_info()
- add_class()
- check_pre_reqs()

courses => Course class
- time

professors => Professor class

"""

class Student:

    # constructor
    def __init__( self, first_name, last_name, student_id ):
        # set the attributes/fields
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def print_student_info(self):
        print("Firstname: ", self.first_name)
        print("Lastname: ", self.last_name)
        print("Student ID: ", self.student_id)
        try:
            print("Student's major: ", self.major)
        except AttributeError:
            pass
        print("\n")

    def set_major( self, major ):
        # set a major for the student
        self.major = major


student1 = Student( "Jill", "Land", 444222 )
student1.print_student_info()
student1.set_major("CS")
student1.print_student_info()


student2 = Student( "Tom", "Sea", 344222 )
student2.print_student_info()
