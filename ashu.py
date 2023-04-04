# Day 1.
'''features of pyhton :- simple and streght forword language, object oriented programing
code readability, automatic memory management, large library,casesensitive,dynamically type,
huge cummunity,plateform indepentent, open source '''

# Day 2.
#comments:-Readability improve karne ke liye use karte hai.
'''there are two type of comments :- 
1. Single line comments. # se comment hote hai.
2. multiline comments. '''''' se comments hote hai'''

#variable:- variable are used to hold data during excution of the program.
'''ek tarike ka container hota hai jaha ham value store karte hai.

variable name is any combination to alphabet, digit and underscore.
variable name not start a digit.
variable name are casesensitive.
keyword cannot be used as variable name.'''

# type() :- is a pridefine function which return the data type of a specified variable
#Data type :- 
# Number --- int , float , complex (3+j) 
'''boolean : True , False.
String : Str.'''

# Data Type 
'''Numbers :- int, float, complex : these are classes.-----> All data types are classes
Boolean : bool :- True , False :
String : Str''' 
'''empty string is -->  False
non empty string is---> True'''        

'''Q. What is an object ?
Answer :- Object is something which can store data and has methods (function) to handle data.'''

#print() : is a pridefine function
'''(i)   printing simple text.
(ii)  printing multiples value.
(iii) end.   (end ="") same line me print hota hai.
(iv)  sep.   value seprarte karta hai.'''

# Day 3 :-
'''*Import :
*Keyword :
*Operators :
*User input :'''

'''1:-import :----> Modules :---> .py file is a module...
module contain python code with three kind of reuseable element:
1. Variable.
2. function.
3. classes.
ex=> do file hai hamare pass first is my.py and second is you.py ab hame you.py file me se 
variable, function.classes use karna hai to ham asse karenge...'''

# jis file me ham code kar rahe hai hye hamari pahli file ho gyi hai ab dusri file ke variable
# ko use karne ke liye hame import ka use karna hoga jaise ..

'''import guess
print(guess.attempts)'''

#2 :Keywords:---> bassically two types of keyword ..
'''first one is ----> Predefined Words.
second is -------> Reserved Words...
Bassically kisi bhi programing language me kuch words asse hote hai jo pahle se hi define hote 
hai unhe ham KEYWORDS kahte hai.'''

'''import keyword
print(keyword.kwlist)'''
#print(len(keyword.kwlist)) isse numbers of keyword ka pta chalta hai kitne hai.

# Operators :---
'''1.Airthmatic Operators:--> **(power calculate) %(modules) //(floor division) +,-,*,/(division)
2.Reletional Operators:--> greater then > , less then <, >= greater than equal to ,
------------------------->  <= less than equal to , == equal to , != not equal to.. 
3.Logical Operators:--> not , and , or
4.Bitwise Operators:--> &, |, ^, ~, >>, <<
5.Assignment Operators:--> =, +=, -=, /=, %=, //=, **=, *=, 
6.Identify Operators:--> is , is not
7.Membership Operators:--> in, not in'''

# Day. 4:
'''Input ()--->its a predefined function take a input from user
*can take at most one arguments.
*its always return str type value.
* You can be conversion function to input data into desired type..'''

# Type conversion :-input hamesha str me value return karta hai OR hame str me type me nahi chahiye
'''to hame type convirsion kanta padta hai jaise str ko int me karne ke liye int() ka use hota hai baise hi
binary no ke liye--> bin()
                     oct()
                     hex()
                     ord() unicode nikalne ke liye hota hai
                     chr()'''

# Desicion Control :
'''1.if 
2.if else
3.if elif else
4.single line if else'''

# If consition :
# Ye condtion koi bhi python ka expretion ho sakta hai jisko true ya false me evaluete kiya jayega
# Agr condition true ho to hi if condition ka block chalega..nahi to ye dusri condition check karega.

#Q. Write a program to check weather a given number is positive or not.
 
'''a =int(input("enter a number"))
if a>0:
    print("positive")
else:
    print("negative")'''
# Method 2 :-

'''a = int(input("enter a number"))
print("positive" if a>0 else "nagative")'''

#Q. Write a program to print grade obtained in a test. take marks obtained from 
# user and display the grade.

'''a = int(input("enter marks "))
if a>=90:
    print("grade A")
elif a>=80:
    print("grade B")
elif a>=70:
    print("grade C")
elif a>=60:
    print("grade D")
elif a>=50:
    print("grade E")
else:
    print("fail")'''
    
# Q : write a program leap year or not

'''year= int(input("enter"))
if ((year%4==0) and (year%100!=0) or (year%400==0)):
    print("leap year")
else:
    ("not a leap year")'''

# Q : Write a python script to calculate area of a rectangle..
'''length = int(input("enter"))
breadth = int(input("enter"))
area = length*breadth
print("area",area)'''

# Q : Write a python script to calculate simple interest.

'''p =int(input("enter a principle: ")) # amount 200000
t =int(input("enter a time : "))        # time 1 year
r =int(input("enter a rate : "))      # 3 percent
si= p*t*r/100                    
print("simple interest is",si) '''     #output : 72000

# Q : Write a program to even or odd .
# Method 1:
'''a = int(input("enter a  number"))
if a%2==0:
    print("Number is even")
else:
    print("number is odd")'''

# Method 2: Single line code
'''a =int(input("enter a number"))
print("even" if a%2==0 else ("odd"))'''

# Day 5: ------------->    
# Loops : for loop , while loop, nested loop
# While loop : Jab tak while block me condition galat nahi hoti hai tab tak bo chalega. false hote hi ruk jayega..

# Q : Write a program to print mysirG five time on the screen...

'''i = 1
while i<=5:
    print("my sir g")
    i+=1 '''

# Q : Write a program to print first N natural numbers.

'''n = int(input("enter a number"))
i = 1
while i<=n:
    print(i,end=' ')
    i+=1'''

# Q : Write a python script to print first 10 odd natural numbers.

'''i = 1
while i<=19:
    print(i,end=' ')
    i+=2'''

'''i =1
while i<=10:
    print(2*i-1,end=' ')
    i+=1'''

'''for i in range(1,11):
    print(2*i-1,end=' ')'''

# Q : Write a pyton script to print squares of first n natural number .

'''i = 1
while i<10:
    print(i**2,end=' ')
    i+=1'''

# Q : Write a python script to calculate lcm of two numbers .
# Lcm ---> Least common multiple... 

'''a = int(input("enter a first no"))
b = int(input("enter a second no"))
c = a if a>b else b # yadi a, b se bada hai to a ki value c me store hogi nhi to b ki
while c<=a*b:
    if c%a==0 and c%b==0:
        print("lcm is",c)
        break
    c+=1'''

# Day 7 :-------------> 
# * What are iterables ? 
#An iterable object is something that contains a countable number of value ....
# bassically iterable object means jisme countable no hai .

#Various Iterable :--> *range, *tuple, *dict, *str, *list, *set, *frozonset, *bytes, *bytearray..
'''* range = range is a class in python..
* range is a immutable sequence.(immutable means --> Unchangeable)
* range can cantain only int type values.
 (range object me multiple value to hogi but int type me honi chahiye)
* range contains sequence of integer with common difference. (Airthmatic prograssion)
( airthmatic progression ek assi series hai jisme pahli term ko agr a bolte hai to usme koi value 
ko jod kar dusra term banta hai phir usko jod kar tisra term banta hai jaise.
a, a+d, a+2d, a+3d)

range(begning,end,step) 
range(1,10,1) (1 begning hai 10 end hai then 1 step hai ) output1,2,3,4,5,6,7,8,9 aayega
begning -- matalb range ke start ka digit konsa hoga . jo (inclusive) hota hai
end -- mtalb kaha par ja kar end hoga but jo bhi no diya hoga us no ko chhod dega bo.(Exclusive)
step-- mtlb common gap -- '''
'''range(2,8,2) output-- 2,4,6
range(10,3,-2) output-- 10,8,6,4'''
# agr tumne range me koi single value pass ki hai to use bydefault end man leta hai 
# jaise range(10) to bo begning 0 le lega jaha se start hona hai or step bhi 1 le lega..
# or agr begning or end diya hai to step ko bo apne man se 1 le lega ..

# Q. write a program to print first n natural numbers.
'''n= int(input("enter a number"))
for i in range(1,n+1):
    print(i,end=" ")'''

# Q. Write a program to print squares of the first n natural no.
'''n= int(input("enter a no"))
for i in range(1,n+1):
    print(i**2)'''

# Day 8 : ---> List : List is a collection which is orderd and  changeable.. 
# in python are list written with square bracket..[1,1,2,12,] like this..

'''What are attributes ?
class is a group of variables and function.. there variables and function are called attributes.

python me kisi bhi class ke ander jitne bhi variable or function banaye jate hai unko bolte hai
attributes'''

#String method() : String is a data type in python its a sequence of characters is closed is Quotes.
# we can primarily , write a string in these three ways: 
# 1. Single Quotes string a = 'python'
# 2. Double Quotes string a = "pyhton"
# 3. Triple Quotes string a = '''python'''

# string slicing : A string python can be sliced for getting a part of the string.
'''n = 'python'
print ( n[2:5])'''

# 1. Upper case(): The upper () method returns the string in upper case:
'''a = "hello, world!"
print(a.upper())'''

# 2. Lower case(): The lower () returns the string in lower case().
'''a = "HELLO, WORLD!"
print(a.lower())'''

# 3.Remove whitespace : the split () method removes any whitespace from the beginning or the end.
'''a ="  hello world "
print(a.strip())'''

# 4. Split(): the slipt() method returns a list where the text between the specified seperator
#become the list item.
'''a ="hello world "
print(a.split())'''
# 5. Replace (): The replace() method replace the string with another string.
'''a ="hello world "
print(a.replace("h","j"))'''

#6. Format(): The format() method tekes the passed argument formate them, and places them in the string
# where the placeholder {} are:
# Use the format() method to insert numbers into string:
'''age = 24
x = "my name is diksha , and i am {}"
print(x.format(age)) '''


#List methods : 
#(1) Append() :- The append method appends an element to the end of the list.
#append method jis bhi element ko append karega bo bydefoult last me add ho jayega
'''list = [1,2,3,4,5,6,7]
list.append(20)
print(list)''' #output : [1,2,3,4,5,6,7,20]

# 2. Clear(): The clear() method removes all the element from the list.
'''list = [1,2,3,4,5]
list.clear()
print(list)'''#output : []

# 3. copy(): The copy mrthod() returns a copy of the specified list.
'''list = [1,2,3,4,5,6]
x = list.copy()
print(x)'''# output : [1,2,3,4,5,6]

# 4. Count(): The count() method returns the number of element with the specified value.
'''list = [ 1,2,5,4,6,5,5,515,1]
x=list.count(5)
print(x)'''# output : 3

# 5.extend(): The extend() method add the specified list elements (or any iterable) 
# to the end of the current list.
'''list1 = [1,2,3,4,5,6]
list2 = ['ashu','singh','rajput']
list1.extend(list2)
print(list1)''' #output : [ 1,2,3,4,5,6, 'ashu','singh','rajput']

# 6. index(): returns the index of the first element with the specified value.
'''list = ['ashu','diksha','divya','somya','amrita','anshita','varsha','payal']
x = list.index("diksha")
print(x)'''#output : 1

# 7. Insert() : The insert() method insert the specified value at the specified position. 
'''list= [1,2,3,4,5]
list.insert(1,10)
print(list)#'''# output : [1,10,2,3,4,5]

# 8.Pop(): The pop() methods removes the element at the specified position. 
#jisko remove karna hai uska index number dena padta hai 
'''list = [1,2,3,4,5,6]
list.pop(1)
print(list)'''#output : [1,3,4,5,6]

# 9. Remove() : The remove() method removes the first occurrence of the element 
# with the specified value.
#jisko remove karna hai bo value dena padta hai
'''list = [1,2,3,4,5,6]
list.remove(2)
print(list)'''

# 10. Reverse(): The reverse() method reverses the sorting order of the element.
'''list = [1,2,3,4,5,15,55,521,1,2]
list.reverse()
print(list)'''

# 11. Sort(): The sort() method sort the list ascending order by default.
'''list = [1,55,45,35,5,8,6,9]
list.sort()
print(list)'''

# 12. Concatenate(): The concatenate() method used to add two lists.
'''list1 = [1,3,5]
list2 = [7,9,11]
list3 = list1+list2
print(list3)'''


# Tuple : tuple is a collection which is ordered and unchangeable, in python tuple are written 
# with round bracket like this-----> ()

#1. Count() : the count() method returns the numbers of time a specified value appears in the tuple.
'''tuple = (1,2,3,4,5,2,2,2,)
x = tuple.count(2)
print(x) '''

# 2. Index() : the index() method find the first occurrence of the specified value.
'''tuple = (1,2,3,5,4,1,2,)
x = tuple.index(2)
print(x)'''

# Dictionary : A dictionary is a collection which is unorderd and changeable and indexed. 
# In python dictionary are written with curly bracket. and keys and value.

# Accessing item : you can access the item of a dictionary by refering to its key name, inside
# square bracket. 
# Methods :
# 1. Clear(): The clear() method removes all the element from a dictionary.
'''dict = {"apple":"fruits","tamoto":"sabji","hero":"honda"}
dict.clear()
print(dict)'''

# 2. Copy(): the copy() method returns a copy of the specified dictionary .
'''dict = {"apple":"fruits","tamoto":"sabji","hero":"honda"}
x = dict.copy()
print(x)'''

# 3. Items( ): The items() method returns a view object.The view object contains the key-value 
# pairs of the dictionary, as tuples in a list.
'''car = {"brand": "Ford",
"model": "Mustang", 
"year": 1964
}
x = car.items() 
print(x)'''

#4. pop item(): the pop() method removes the item that was last inserted into the dictionary.
'''car = {"brand": "Ford",
"model": "Mustang", 
"year": 1964
}
car.popitem() 
print(car)'''

# 5. Set default(): The set default method returns the value of the item with the specified key. 
# if key exits no effect .if not it assigns the same value .
'''car = {"brand": "Ford","model": "Mustang", "year": 1964}
x = car.setdefault("aaja","chale")
print(x) 
y = car.setdefault("kaha","jaha tu kahe") 
print(y)
print(car)'''



def demo(a):
    print(a)
demo(100)

