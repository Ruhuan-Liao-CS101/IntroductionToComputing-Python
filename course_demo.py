class Course:

    # constructor
    def __init__( self, title, id ):
        # set the attributes/fields
        self.title = title
        self.id = id

    # printing course information
    def print_course_info(self):
        print("Course title : ", self.title)
        print("Course ID: ", self.id)
        print("\n")

    # set a new value to the title attribute
    def set_title( self, title ):
        self.title = title

