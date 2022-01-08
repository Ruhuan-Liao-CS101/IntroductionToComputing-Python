'''
Write a Python script that implements a Course class. It should include at least the attributes:
course_title
course_id
Implement the constructor, a method that prints all the information related to the class, a method that updates the title of the course.
Create at least 2 course objects to show how your class works.
'''

class Course:

    # constructor
    def __init__( self, course_title, course_id ):
        self.course_title = course_title
        self.course_id = course_id

    def print_course_info(self):
        print("Course title: ", self.course_title)
        print("Course ID: ", self.course_id)

    
course1 = Course("Introduction to Computing", "CPSC1101")
course1.print_course_info()

course2 = Course("Ethnic American Literature", "ENGL1230")
course2.print_course_info()

course3 = Course("Imperialism and Colonialism", "HIST1106")
course3.print_course_info()

course4 = Course("Calculus I", "MATH1141")
course4.print_course_info()

course5 = Course("Introduction to Catholicism", "RLST1402")
course5.print_course_info()