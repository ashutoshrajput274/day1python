#random moduals
'''import random
liststu=["ashu","mahi","thakur","diksha"]
stu=random.choice(liststu)
print(stu)'''

'''import random
stu=random.randint(1000,9999)
print(stu)'''

#Q.1: Write a program to generate captcha code of 6 charactor ?
# First method :
'''import random
stg="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
a=random.choice(stg)
b=random.choice(stg)
c=random.choice(stg)
num_char=str(random.randint(0,9))
num_char1=str(random.randint(0,9))
num_char2=str(random.randint(0,9))
res_code=a+num_char+b+num_char1+c+num_char2
print(res_code)'''

# Second method :
'''import random
stg="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
res_code= " "
for i in range(3):
    a=random.choice(stg)
    num_char=str(random.randint(0,9))
    res_code+=(a+num_char)
    print(res_code)'''

'''Exception Handling :-Is the process to handels errorfull are abnormal condition 
occured while excution. It can be due to user invalid input etc.
So the process of exception handling involve 3 block for the same.'''
'''Try :- test the given condition...
Except :- is used to through error statement only when try block return True.
Finally :- final block through the result in respective of try block. meaning weather exception
occured .......'''

# First example :-
'''try:
    num=input("enter a number")
    print(num)
except: print("please enter a numbers only")'''

# Second Example :-
'''try:
    num=int("enter a number")
except:print("please enter a numbers")
finally:print("num")'''

