#Q. positive or negative 
'''a=int(input("enter a number"))
if a>0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("zero")'''

'''num=-10
print("positive" if num>0  else "negative")'''

# Q. Even or odd
'''ashu =int(input("enter a number"))
if ashu%2==0:
    print("even")
else:
    print("odd")'''

'''a=10
print("even") if a%2==0 else print ("odd")'''

# Q Sum first n natural number ..
'''a=int(input("enter no"))
sum = 0
for i in range(1,a+1):
    sum+=i
print(sum)'''

'''num = 5
print(int(num*(num+1)/2))'''
'''
def getSum(num):
    if num ==1:
        return 1
    return num+ getSum(num-1)
num =5
print(getSum(num))'''


'''def f1(n):
    if n == 1:
        return 1
    return n* f1(n-1)
n = 5
print(f1(n))'''

'''n= 3
m = 6
sum =0
for i in range(n,m+1):
    sum+=i
    print(sum)'''

'''num1 = 3
num2 = 6
sum =int((num2*(num2+1)/2) - (num1*(num1+1)/2) +num1)
print(sum)'''

# find the greatest of the three numbers of python
'''a,b,c = 40,20,30
if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)'''

# Prime number 
'''n =int(input())
f =0
for i in  range (2,n):
    if n%i==0:
        f=1
        break
if f ==1:
    print("not prime")
else:
    print("prime")'''

# Prime number with in range 
'''a =int(input("enter a first no"))
b =int(input("enter a second no"))
list =[]
for i in range (a,b):
    f = 0
    if i<=2:
        list.append(2)
        continue
    for x in range (2,i):
        if i % x ==0:
            f =1
            break
    if f ==0:
        list.append(i)
print(list)'''

# Q. sum of Digits of a Number
#first method
'''num=(input())
sum =0
for i in num :
    sum=sum+int(i)
print(sum)'''
#Second method
'''num = 12345
sum = 0
def findSum(num,sum):
    if num == 0:
        return sum
    digit =int(num % 10)
    sum += digit
    return findSum(num/10, sum)
print(findSum(num,sum))'''

#Riverse of a number 

'''num=input("enter the number:")
i=num[::-1]
print(int(i))'''

'''num = 654321
print(str(num)[::-1])'''

#method 2. recursion
'''def recurSum(number,reverse):
    if number==0:
        return reverse
    remainder = int(number%10)
    reverse = (reverse*10)+remainder
    return recurSum(int(number/10),reverse)
num =1234
reverse =0
print(recurSum(num,reverse))'''

# Q. Find the number of palindrome or not
'''string = "1221"
rev = ""
for char in string:
  rev =char+rev
if string == rev:
    print("palindrome")
else:
    print("not palindrome")
print("string:" + str(string))
print("rev:" +str(rev))'''

# method 2. slicing
'''num =1234
reverse =int(str(num)[::-1])
if num == reverse:
    print("palindrome")
else:
    print("not palindrome")'''

# Find the number of armstrong or not 

'''a = input("enter a number:")
sum=0
for i in a:
    c=int(i)**3
    sum=sum+c
if str(sum)==a:
    print("is armstrong number")
else:
    print("is not armstrong number")'''
    

    

        