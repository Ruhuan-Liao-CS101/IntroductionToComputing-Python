# this is the application that should be run

from student_demo_errors import Student
from course_demo import Course


# creating a student object
student1 = Student( "Jill", "Land", 444222 )

# printing the information of the student Object
student1.print_student_info()

# creating a tudent object
student2 = Student( "Tom", "Sea", 344222 )

# printing the information of a student object
student2.print_student_info()

# creating a course object
course_icp = Course("Intro to Programming", "CS101")

# adding a course to the students
student1.add_course( course_icp )
student2.add_course( course_icp )

# creating a course object
course_hi1 = Course( "History", "HI101") 

#add the new course to student1nand student2
student1.add_course( course_hi1 )

# retrieving the list of courses for the object student1
courses_for_student1 = student1.get_courses()

# print the info for each course
i=0
while(i <= len(courses_for_student1)):
    try:
        courses_for_student1[i].print_course_info()
        i+=1
    except IndexError:
        pass
    