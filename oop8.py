class Person():
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        print(self.name,self.gender) 
    
def greeting(person):
    person.name="alex"
    return person

p=Person("prakash","male")

a=greeting(p)

print(id(p))
print(id(a))
print(p.name,p.gender)
print(a.name,a.gender)
