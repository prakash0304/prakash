a=eval(input("enter the character: "))
if len(a)%2==1:
    if type(a)==tuple:
        print("tuple")
    else:
        print(" not a tuple")
else:
    print("doesnt have a middl value.")
