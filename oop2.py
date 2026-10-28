#creating class & object

class Vehicle():
    def __init__(self,a,b):
        self.x=a
        self.y=b
        
    def drive(self):
        res=self.x+self.y
        print("result is : ",res)
car=Vehicle(int(input("Enter first number: ")), int(input("Enter second number: ")))
car.drive()
print(f"x: {car.x}, y: {car.y}")

