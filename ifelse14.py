a=eval(input("ENTER THE list:"))
if len(a)%2!=0:
    print("contains a middle value.")
    print(a[len(a)//2])
else:
    print("doen't contain middle value.")
