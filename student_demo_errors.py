
class Student:

    # constructor
    def __init__( self, first_name, last_name, student_id ):
        # set the attributes/fields
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.courses = []

    # method to print the information related to a student
    def print_student_info(self):
        print("Firstname: ", self.first_name)
        print("Lastname: ", self.last_name)
        print("Student ID: ", self.student_id)
        try:
            print("Student's major: ", self.major)
        except AttributeError:
            pass

        try:
            print("Student's gpa: ", self.gpa)
        except AttributeError:
            pass


    # method to set a value to the major attribute
    def set_major( self, major ):
        # set a major for the student
        self.major = major

    # method to add course to the list of courses attended by the student
    def add_course( self, course ):
        self.courses.append( course )

    # method that returns the list of courses
    def get_courses( self ):
        return self.courses

