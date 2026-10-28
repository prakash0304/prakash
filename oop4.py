#

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

