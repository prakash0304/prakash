a=eval(input("a: "))
if type(a)==list:
    if type(a[len(a)//2])==str:
        print(a[len(a)//2])
    else:
        print("mid value is not a string.")
else:
    print("value is not a list")
        
