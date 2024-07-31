class Student:
    school='SHSS' #1 static variable outside method
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        Student.center_code=101 #2 Static variable inside constuctor
    def display(self):
        Student.grade='10th' #3 Static variable instance method
        print("Name",self.name)    
        print("Roll no",self.roll)    
        print("School",Student.school)    
        print("Center",Student.center_code)    
        print("grade",Student.grade)
        print("city",Student.city)        
        

        

obj=Student("nishant",185)
Student.city="Bhopal"
obj.display()
print("school",Student.school)
# obj=Student("dev",385)
# obj.display()
# print("school",Student.school)