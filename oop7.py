class Person():
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    
    
def greeting(person):
    print(f"hello {person.name} your gender is {person.gender}")
    p1=Person("suresh","male")
    return p1


p=Person("prakash","male")

a=greeting(p)

print(a.name,a.gender)
print(p.name,p.gender)