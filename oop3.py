#create class App

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


print(product1.users,product1.storage)
print(product2.users,product2.storage)
