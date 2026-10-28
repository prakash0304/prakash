class Atm():
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()
    def menu(self):
        user_input=input(
            """Welcome to ATM\n1. Create Pin\n2. Check Balance\n3. Deposit\n4. Withdraw\nENter your choice: """
            )
        if user_input=="1":
            print("Create Pin") 
            self.pin=input("Enter new pin: ")
        elif user_input=="2":
            print("Check Balance")
            print(f"Your balance is: {self.balance}")
        elif user_input=="3":
            print("Deposit")
            amount=int(input("Enter amount to deposit: "))
            self.balance+=amount
        elif user_input=="4":
            print("Withdraw")
            amount=int(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance-=amount
            else:
                print("Insufficient balance")
        else:
            print("Invalid input")


obj=Atm()
obj.menu()
print(type(obj))