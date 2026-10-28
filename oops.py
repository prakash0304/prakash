#creating class & object
'''
class Vehicle():
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def drive(self):
        res=self.x+self.y
        print("result is : ",res)
car=Vehicle(10,20)
car.drive()
'''
#create class App
'''
class App():
    def __init__(self,users,storage,username):
        self.users=users
        self.storage=storage
        self.username=username
    def login(self):
        if self.username=="owner" and self.users>=1:
            print("welcome!",self.username)
            print("your storage is :",self.storage)
        else:
            print("login is denied!")
    def increase_capacity(self,number):
        self.storage+=number
        print("updated storage : " ,self.storage)
product1=App(35,256,input("enter username: "))
product1.login()
product1.increase_capacity(50)

product2=App(35,128,input("enter username: "))
product2.login()
'''
#
'''
class Onlinecourse():
    def __init__(self,course,instructor):
        self.course=course
        self.instructor=instructor
        self.students=[]

    def enroll(self,name):
        self.students.append(name)
        print(f"{name} has been enrolled in the {self.course} course.")

    def course_details(self):
        print(f"Course : {self.course}")
        print(f"instructor name : {self.instructor}")
        print(f"enrolled students : {self.students}")
        

    def complete(self,name):
        if name in self.students:
            self.students.remove(name)
            print(f"{name} has completed the course.")
        else:
            print(f"{name} has not in the course")

    def average(self,grades):
        total=sum(grades)
        average=total/len(grades)
        print(f"the average grade is {average}")


course=input("enter course: ").lower()
instructor=input("enter the instructor: ").lower()
students=input("enter the student: ").lower()
name=input("enter the name: ").lower()


course=Onlinecourse(course,instructor)
grades=eval(input("list of grades: "))

course.average(grades)
course.enroll(students)
course.complete(name)
'''
#
class Atm():
    def __init__(self):
        self.pin=""
        self.balance=0
    def menu(self):
        user_input=input()
        
        
        


        
        













































