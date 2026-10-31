class Student:
    def __init__(self,name,grade,school_name):
        self.name = name
        self.grade = grade
        self.school_name = school_name


    def show_details(self):
        print("i am "f"{self.name}, i go to "f"{self.school_name}, i am in "f"{self.grade} grade")


isaac = Student("isaac","10th","marino colege")
isaac.show_details()
        