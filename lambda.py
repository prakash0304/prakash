#harshad or not for loop
'''n=int(input("n: "))
og=n
total=0
while n>0:
    
    total+=n%10
    n//=10
if og%total==0:
    print("is harshad")
else:
    print("not a harshad")'''

#harshad or not while loop
'''n = int(input('Enter number: '))
temp = n
digit_sum = 0
while temp > 0:
    digit_sum += temp % 10
    temp //= 10
print('Harshad Number' if digit_sum != 0 and n % digit_sum == 0 else 'Not Harshad')'''
#Check strong number
'''n = int(input('Enter number: '))
temp = n
total = 0
while temp > 0:
    digit = temp % 10
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i
    total += factorial
    temp //= 10
print('Strong Number' if total == n else 'Not Strong')
'''
#Strong numbers from 1 to 10000
'''for n in range(1, 10001):
    temp = n
    total = 0
    while temp > 0:
        digit = temp % 10
        factorial = 1
        for i in range(1, digit + 1):
            factorial *= i
        total += factorial
        temp //= 10
    if total == n:
        print(n)''' 
# Check Armstrong number
'''n = int(input("Enter a number: "))
temp = n
total = 0
while temp > 0:
    d = temp % 10     
    total += d ** 3
    temp //= 10  
print(n, "is an Armstrong number" if total == n else "is not an Armstrong number")''' 

# Armstrong numbers from 1 to 1000
'''for n in range(1, 1001):
    temp = n
    digits = 0
    while temp > 0:
        digits += 1
        temp //= 10
    temp = n
    total = 0
    while temp > 0:
        digit = temp % 10
        power = 1
        for i in range(digits):
            power *= digit
        total += power
        temp //= 10
    if total == n:
        print(n)'''
#Check whether a number is a Spy number (sum of digits equals product of digits).
'''n = input("Enter a number: ")
total = 0
product = 1
i = 0
while i < len(n):
    d = int(n[i])
    total += d
    product *= d
    i += 1
print("Spy number" if total == product else "Not a spy number")'''
#Check if a number is a perfect number or not using while loop
'''n = int(input("Enter a number: "))
i = 1
total = 0
while i < n:
    if n % i == 0:
        total += i
    i += 1
print(n, "is a perfect number" if total == n else "is not a perfect number")'''


#Check perfect number or not using for loop
'''n = int(input('Enter number: '))
total = 0
for i in range(1, n):
    if n % i == 0:
        total += i
print('Perfect Number' if total == n else 'Not Perfect')'''

#Print perfect numbers from 1 to 1000
'''for n in range(1, 1001):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    if total == n:
        print(n)'''
#Check whether a number is a Neon number (e.g. 9**2=81 -> 8+1=9).
'''n = int(input("Enter a number: "))
sq = n ** 2
temp = sq
total = 0
while temp > 0:
    total += temp % 10
    temp //= 10
print(n, "is a neon number" if total == n else "is not a neon number")'''

#





























#integer is palindrome or not
'''rev=lambda n:'palindrome' if str(n)==str(n)[::-1] else 'not a palindrome'
print(rev(int(input("enter the number: "))))'''
#harshad or not
'''harshad=lambda n:'is harshad' if n%sum(int(digit) for digit in str(n))==0 else 'not harshad'
print(harshad(int(input("enter the number: "))))'''

#palindrome
'''pal=lambda s:s if type(s)==str and s==s[::-1] else s[::-1]
print(pal(eval(input("enter data: "))))'''



#1.is even or not
'''is_even=lambda n:'is even' if n%2==0 else 'not even'
print(is_even(int(input("enter the input: "))))'''

#2.is odd or not
'''is_odd=lambda n: 'is odd' if n%2!=0 else 'not odd'
print(is_odd(int(input("enter the input: "))))'''

#3.ascii value of character
'''asci=lambda ch:ord(ch)
print(asci(input("enter the ch: ")))'''

#4.reverse a string
'''rev=lambda s:s[::-1]
print(rev(input("enter the string: ")))'''

#5.find sum of two values
'''sum=lambda a,b:a+b
a=int(input("enter a: "))
b=int(input("enter b: "))
print(sum(a,b))'''
#6.find sum of minimum 2 values and maximum of 5 values


#7.check given data is mutable or not
'''mut=lambda data:'mutable' if type(data) in(list,set,dict) else 'immutable'
print(mut(eval(input("enter the data: "))))'''
#8.check if given integer ends with 5 or not
'''end_5=lambda n:'ends with 5' if n%10==5 else 'does not end with 5'
print(end_5(int(input("enter the number: "))))'''
#9.check if the given data is string or not
'''st=lambda s:'is string' if type(s)==str else 'is not string'
print(st(eval(input("enter s: "))))'''
#10.check if given list has middle value or not
'''middle=lambda l:'has middle value' if len(l)%2!=0 else 'does not have a middle value'
print(middle(eval(input("enter the list :"))))'''
#11.count number of characters of a string only if its palindrome
#else reverse the string
'''count=lambda s:len(s) if s==s[::-1] else s[::-1]
print(count(eval(input("enter the string: "))))'''

#
'''import keyword
key_word=lambda x:'keyword' if x in keyword.kwlist else 'not keyord'
print(key_word(input()))'''

























































































