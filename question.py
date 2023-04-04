#Q.1: Positive or negative number.
# Given an integer input the objective is check weather the given integer is positive or negative
# In order to do so we have the following method.
# METHOD.1: USING BRUTE FORCE .
# This method uses brute force to check weather a given integer is positive or negative.
'''num = 15
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")'''

# METHOD.2: USING NESTED IF ELSE STATEMENT.
# This method uses nested if else statement to check weather a given number is positive or negative
'''num = 15
if num>=15:
    if num==0:
        print("Zero")
    else:
        print("positive")
else:
    print("negative")'''

# METHOD.3: TERNARY OPERATOR.
# This method uses ternary operator to check weather a given number is positive or negative
'''num = 15
print("positive" if num>0 else "negative")'''

#Q.2: Number even or odd .
# Divided by 2 and check if its divisible or not . Its even is its perfectly divisible by 2, or
# an odd no otherwise
# METHOD.1: USING BRUTE FORCE
# this method simply check if the given input integer is divisible then print Even or odd otherwise
'''num = int(input("enter a number:"))
if num%2==0:
    print("given number is Even")
else:
    print("Given number is odd")'''

#METHOD.2: USING TERNARY OPERATOR 
#This method uses ternary operator to check if the integer input is divisible by 2 
#if true print Even or odd otherwise
'''num = 19
print("Even") if num%2==0 else print("odd")'''

#METHOD.3: USING BITWISE OPERATOR
#This Method uses bitwise operators to check if a given number is Even or Odd.
'''def isEven(num):
  return not num&1

if __name__ == "__main__":
  num = 13
  if isEven(num):
    print('Even')
  else:
    print('Odd')'''

#Q.3: Program to find the sum of first N natural numbers.
# Method.1: Using for loop :- In this method we'll add all the natural numbers until the given 
# integer input using for loop in python.
#num = int(input("enter a number"))
'''num = 5
sum = 0
for i in range(num+1):
    sum+=i
print(sum)''' #output : 15

# Method.2: Using formula for the sum of Nth Numbers :- In this method we uses the formula for 
# finding the sum of N terms.
#formula: sum=(num*(sum+1))/2
'''num = 5
print(int(num*(num+1)/2))'''

# Method.3:- Using Recursion :- This method uses Recursion to recursively add the natural numbers
# up to the given integer input using recursion in c++

'''def getSum(num):
    if num ==1:
        return num+getSum(num-1)
num = 5
print(getSum(num))''' # confusion

#leap year or not ?
'''year = 2000
if ((year%4==0) and (year%100!=0) or (year%400==0)):
    print("leap year")
else:
    print("not a leap year")'''

'''year = int(input("enter a year"))
if year%400==0 or year%4==0 and year%100!=0:
    print("leap year")
else:
    print("not a leap year")    '''
# percentage

'''p =int(input("enter a marks "))
c =int(input("enter a marks "))
m =int(input("enter a marks "))
t = p+c+m
pr = t/3
print(pr)
if pr>=90:
    print("grade a+")
elif pr>75:
    print("grade a")
elif pr>=60:
    print("grade b")
elif pr>=45:
    print("grade c")
elif pr>=35:
    print("grade d")
else:
    print("fail")'''
    
# Q. prime or not

'''a = int(input("enter a number"))
for i in range(2,a):
    if a%i==0:
        print("not prime")
        break
else:
    print("prime number")'''
    




