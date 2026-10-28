class Person():
    def __init__(self,name,country):
        self.name=name
        self.country=country

name="prakash"
country="india"
p=Person(name,country)

print(p.name,p.country)
q=p

print(id(p))
q.name="suresh"

print(p.name,p.country)

p.name="sonia"

print(id(q))

print(p.name,q.name,q.country)