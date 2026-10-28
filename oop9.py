class Person():
    def __init__(self,name,country):
        self.name=name
        self.country=country




p1=Person("prakash","india")

p2=Person("suresh","usa")

p3=Person("sonia","uk")

print(id(p1),id(p2),id(p3))
print(p1.name,p2.name,p3.name)