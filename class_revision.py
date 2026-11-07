class Student:
    def __init__(self,name,grade,school_name):
        self.name = name
        self.grade = grade
        self.school_name = school_name


    def show_details(self):
        print(f"i am {self.name}, i go to {self.school_name}, i am in {self.grade} grade")


isaac = Student("isaac","10th","marino colege")
isaac.show_details()

class Marks(Student):
    def __init__(self, name, grade, school_name,subject1,subject2,subject3):
        super().__init__(name,grade,school_name)
        self.__subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3
        

    def show_details(self):
        super().show_details()
        print(f"i got {self.__subject1}, in {self.subject2}  in {self.subject3} ")


jacob = Marks("isaac","10th","marino college",100,90,85)
jacob.show_details()

print(jacob.__subject1)