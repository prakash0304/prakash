#digital root a number
'''n=int(input("n: "))
while n>=10:
    total=0
    while n>0:
        total+=n%10
        n//=10
    n=total
print(n)'''
#harshad or not
'''n=int(input("n: "))
og=n
total=0
while n>0:
    
    total+=n%10
    n//=10
if og%total==0:
    print("is harshad")
else:
    print("not a harshad")
'''
#sum of num
'''n=int(input("n: "))
sum=0
for i in range(0,n+1):
    sum+=i
print(sum)'''
#factorial
'''n=int(input("n: "))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)'''
#count num div by 5 from 1 to N
'''n=int(input("n: "))
count=0
for i in range(1,n+1):
    if i%5==0:
        count+=1
print(count)'''
#average of numbers 1 to 10
'''total=0
count=0
for i in range(1,11):
    total+=i
    count+=1
print(total/count)'''
#sum from1 to 100
'''total=0
for i in range(1,101):
    total+=i
print(total)
'''
#product from 1 to 10
'''pro=1
for i in range(1,11):
    pro*=i
print(pro)
'''
#




































    

