a=eval(input("enter the data: "))
if type(a)==list or type(a)==set or type(a)==dict:
    print("data  is mutable")
else:
    print("data is not mutable.")
