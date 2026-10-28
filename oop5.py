class Person():
    def __init__(self,name,country):
        self.name=name
        self.country=country
    def greeting(self):
        if self.country=="India":   
            print(f"namaste {self.name}")
        else:
            print(f"hello {self.name}")

p=Person(input("enter name: "),input("enter country: ").capitalize())
p.greeting()
print(p.name)
print(p.country)