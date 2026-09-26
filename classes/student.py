class Student:

    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):

        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)

    def is_pass(self):

        if(self.marks>40):

            print("Pass")

        else:

            print("Fail")

    
student1 = Student("Lawanya",20,100)

student1.display()

student1.is_pass()