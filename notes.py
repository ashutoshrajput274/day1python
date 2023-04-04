# Advance Python : 
# object oriented programing : There are many aprochases to solve any problems by programing one of the method
#  solving problem using objects. This is know object oriented programing its provide. 
# * modulerity 
# * Reuseability 
# * Security ...
# 1.Modulerity  :- Means breking the long code into small code.. 
# 2.Reuseabilty :- Allowing reuse of the small code..  
# 3.Security    :-------------------------------------

# Object oriented programing consist of two block: Class & Object ..
# Class :- its the blueprint of the objects .in otherway the properties of charractoristics of the object is defined
#inside this block..
 
'''ex :
class Ashu():
    properties'''

# Object :- Its a real life entity meaning providing memory to the defined properties. State, Behaviour and identity.
''' ex :
 object = Classname()'''

'''class fan():
    a="start rotating"
   # print("start rotating")
object = fan()
print(object.a)'''

# Features    :- Inheritance, Encapsulation, Polymorphism, Data abstracts.
# Constractor :- Its a special member of call----------------------------

'''class Fan():
    def rotate(self,a):
        self.a = a
        return self.a
      # print("start rotating")
obj = Fan()
print(obj.rotate(2))'''

'''class Fan():
    def __init__(self,a):
        self.a = a
obj = Fan(25)
print(obj.a)'''

#(1) Inheritance :- Its the concept that allow inheriting (coping) one class properties into another class.
#* Parent class(Base class): the class of which properties are going to inherited is know as parent class..
#* Child Class(Derived Class): the class that inherit the properties of another is know as child class ..
#ex:
'''                      class Parent():
                               parent properties

                      child class(parent) 
                               child properties                              '''

#(1) :- Single inheritance :- Single parent and single child..
#ex:
'''class Dog():
    def sound1(self):
        print("my sound is bow bow")
        return
class Puppy(Dog):
    def sound2(self):
        print(Dog.sound1(self))
        return
obj = Puppy()
obj.sound2()
obj.sound1()'''

#(2) :- Multilevel Inheritance :- Each class will act as a parent class for another class..(har class dusri class ke liye parent ka kam karti hai)
'''                             Class A()
                                   |
                                Class B(A)
                                   |
                                Class c(B)
                                   |
                                Obj = ()                                            '''


'''class A():
    def func1(self):
        print("class A, function")
        return
class B(A):
    def func2(self):
        print("class B, function")
        return
class C(B):
    def func3(self):
        print("class C, function")
        return
        
obj = C()
obj.func1()
obj.func2()
obj.func3()'''

#(3) :- Multiple inheritance :- A child class inheriting properties of two or more parent class...

'''          class A()                 class B()
            
                        class C(A,B)                             '''

'''class A():
    def func1(self):
        print("class A, functon")
        return
class B():
    def func2(self):
        print("class B, function")
        return
class C(A,B):
    def func3(self):
        print("class C, funtion")
        return
obj = C()
obj.func1()
obj.func2()
obj.func3()'''

#(4) Hirachical Inheritance :- A single parent class having many child classes..
'''
                                       class A()----------parent

                          class B(A)   -----child-----   class C(A)                  '''


'''class A():
    def func1(self):
        print("class A, function")
        return
class B(A):
    def func2(self):
        print("class B, function")
        return
class C(A):
    def func3(self):
        print("class C, function")
        return
obj = C()
obj.func1()
obj.func3()

obk = B()
obk.func1()
obk.func2()'''

#(5) Hybrid Inheritance :- A child class having two parents classes

'''    (Grand father)------->       Class A()

            (Mother)---->   Class B()       Class C() -------->(Father)       
                                           
                                       
                                     Class D()
                                      (son)                                           '''
'''
class A():
    def func1(self):
        print("class A, function")
        return
class B(A):
    def func2(self):
        print("class B, function")
        return
class C(A):
    def func3(self):
        print("class C, function")
        return
class D(B,C):
    def func4(self):
        print("class D, function")
        return
obj = D()
obj.func1()
obj.func2()
obj.func3()
obj.func4()'''

#(2) Encapsulation :- Meaning binding all the things into single entry , In python the process of 
# wrapping all variables and method into a single entry is know as encapsulation..
# 
# *. Class modefiers :- 

# Private :- Meaning only file owner can access the method. In python it required by "__a" double underscore.. 

'''class A():
    def __init__(self,a):
        self.a = a
    def show(self):
            print(f"this is a private var (self.__a)")
            return
class B(A):
    def __init__(self,b):
        super().__init__(b)
    def show(self):
            print(f"this is a private var (self.__a)")
            return
obj=B(5)
obj.show()'''

# protect :- Meaning file owner and permited user can only access the methods.In python its required by "_a" underscore

'''class A():
    def __init__(self,a):
        self.a = a
    def show(self):
            print(f"this is a private var (self._a)")
            return
class B(A):
    def __init__(self,b):
        super().__init__(b)
    def show(self):
            print(f"this is a private var (self._a)")
            return
obj=B(5)
obj.show()'''

#(3) Polymorphism :- Means many form of single name. Also in python its means functions having same 
# name but different signature...
'''Types :-  Compiled type :-
Method overloading :- Method overloading means having same name or method in same class but different parametters 
and arguments.
{ Here in the python method overloading concept is not applicable because its an interpreted language..}'''

'''Interpreted type :-
Method overriding :- Means having same name of method but class name will we different also, parameters and 
argument will we same .. Inheritance is Compulsary..'''

'''class MO1():
    def myfunction(self,a):
        self.a = a
        return "this is mo1 function"
class MO2():
    def myfunction(self,a):
        self.a = a
        return "this is mo2 function",super().myfunction(10)
mo = MO2()
print(.myfuncton(10))'''#program error

# Abstraction :- Abstraction means hidden..
#                In python a consist of one or more abstract method is called the abstract class..
#                Abstract method do not conatain their implementation.
#                Abstract class be inherited  by the abstract method and sub classes.

'''class RBI():
    def intrest(self):
        pass
class SBI(RBI):
    def intrest(self):
        print("my rate is 8%")
class BOB(RBI):
    def intrest(self):
        print("my rate is 9%")
obj = BOB()
obj.intrest()'''

#Data base :- Database (DB) are organized they have a structure and all the data they store its fits into that 
#             structure.. Database are quite similar to spreadsheets consist of tables (having rows and colomn)..

#<<<<--------------------------------------------------------------------------------------------------------------------->>>>

# Pattern Questions . 
# Q1. Simple number triangle pattern ?
#numers print
'''row = 6
for i in range(row):
    for j in range(i):
        print(i,end=' ') # number print ho jayenge
    print("") '''# jaisa chahiye baisa ho jayega
   

# star print

'''row = 6
for i in range(row):
    for j in range(i):
        print("* ",end="")
    print("")'''

# Q2. Inverted  pyramid of numbers ?
# number print
'''row = 5
a = 0
for i in range(row,0,-1):
    a+=1
    for j in range(1,i+1):
        print(a,end=" ")
    print('\r')'''

# stars print
'''row = 5
a = 0
for i in range(row,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print('\r')'''

'''size = 5
m = (2*size)-2
for i in range(0,size):
    for j in range(0,m):
        print(end=" ")
    m = m-1
    for j in range(0,i+1):
        print("*",end=" ")
    print("")'''

'''n =6
for i in range(1,6):
    print('  ','* '*i)'''

'''n = int(input())
for i in range(n):
    print('  '*(n-i)+('* ')*(2*i+1))'''
'''
x,y=0,1
while y<30:
    x,y = y,x+y
    print(y)''' #not understand



# Q3. Half pyramid pattern of numbers.

'''row = 5
for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("")'''

# Q4. inverted pyramid of decending numbers.

'''row = 5
for i in range(row,0,-1):
    num = i
    for j in range(0,i):
        print(num,end=' ')
    print('\r')'''

# Q5. Inverted pyrramid of the same digit .

'''row = 5
num = row
for i in range(row,0,-1):
    for j in range(0,i):
        print(num,end=" ")
    print('\r')'''

# Q6. Reverse pyramid of numbers.

'''row = 6
for i in range(1,row):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("")'''

# Q7. Inverted half pyramid numbers pattern ?

'''row = 5
for i in range(row,0,-1):
    for j in range(0,i+1):
        print(j,end=" ")
    print("\r")'''

'''this program to we need a 
1.Input
2.for loop
3.range()
4.print()''' 

'''    * 
       * * 
       * * * 
       * * * * 
       * * * * *      ''' 

'''num = int(input('enter a number of row'))
for i in range(1,num+1):
    for j in range(1,i+1):
        print('*',end=" ")
    print('')'''

'''
* 
* * * 
* * * * *
'''

'''num = 3
k = 1
for i in range(1,4):
    for j in range(1,k+1):
        print('*,end=" ")
    k = k+2
    print('')'''

'''     *
       ***
      *****
     *******
    *********    '''

'''num = int(input("enter a number of row"))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,1*i+1):
        print("*",end=" ")
    print("")'''


















'''-------------------------------------------------------------------------'''


    