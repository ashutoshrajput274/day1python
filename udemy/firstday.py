'''What is while loops ?

* Used to execute a set of statement continuously as log as a condition is true..
* While loop can have optional else clause.

ex. '''

'''i =1
while i<7:
    print(i)
    i+=1'''
#-------------------------------------------------------------

'''what is a for loop ?

* Used to iterate over a sequance
* Sequence is usually: (list, tuple, dict, set, string)
* Does not require and indexing variable to iterate loop
* they can use break and continue statement.'''
# example-

'''fruits =("greeps","mango","banana")
for x in fruits:
    print(x)'''
    
#--------------------------------------------------------------
'''what is nested loops ?
* Nested loops is a loop inside a loop.'''

# exmaple--

'''color = ['green','yellow','red']
fruits = ["mango","banana","apple"]
for x in color:
    for y in fruits:
        print(x,y)'''

#-------------------------------------------------------------------

# what are functions ?
'''* Function are block of code that does something..
* they are reusable.
* they execute or run when called bye their name
* they can have parameters(variables) and arguments(value)
* they can return data as a result
* there are built in function '''

# You can also create a your own custom functions.
# example-->
'''def function_name():
    print("hello world")
'''

# Calling a function
'''def sum(x,y): ----> parameters
    print(x+y)

sum(4,5)   ----> argument(value)'''

# Return keyword value in function 
'''
def ashu(x,y):
    return x+y

print(ashu(4,5))
print(ashu(4,8))'''

# Defualt parameter value 
# this is the value a function uses when called without passing it a value.
'''def student_names(names="rajput"):
    print("hello " + names)
student_names("ashu")
student_names("singh")
student_names()'''

# Keyword argument
'''def ashu(a,b=5,c=10):
    print("a",a, "b",b, "c",c)
    
ashu(3,15,5)
ashu(10,5,15)
ashu(10,20,30)  '''# mtlb ham function ko call karte time jo bhi value pass karna chahte hai kar sakte hai or nahi 
                   # ki to vo jo parameter me hamne di hai vo bydefault le lega


# Functions returning other functions.
'''def yashi():
    def ashu():
        return "hello"
    return ashu
cute =yashi()
print(cute())'''

# Assigning functions to variables
'''def num(x):
    return x+1
a = num
print(a(5))
print(num(9))'''

# Global vs Local variable scope
'''
* Variable defined inside a function body have a local variable.
* variable defined a outside a function have a global variable .
* global variable can be accesed anywhere in python file but local variable only be accessed inside a function it belong to.
'''
'''x =10     <-------- global variable
def ashu():
    global x
    print(x)
    x = 7        <------  local variable
    print("my fav no is",x)


ashu()
print(x)'''

# Nesting function 
'''def ashu(a):
    def singh(a):
        return a+1
    result=singh(a)
    return result
print(ashu(5))'''

# Nested function accessing variable scope
'''def display_message(message):
    "hello"
    def message_sender():
        "nested function"
        print(message)
    message_sender()
    
display_message("show me the money")'''

# Function pass statement
'''def dream_home():
    pass '''        # this function have no block of code this function is empty
    
# Passing function as arguments to other functions

'''def my(b):
    return b+1
def num(c):
    new = 7
    return c(new)
print(num(my))'''


'''def show(n):
    for i in range(n):
        print("-",end=" ")

show(20)   
print("\nram")
show(30)
print("\nsita")
show(40)
print("\nkrishna")
show(50)'''

#-----------------------------------------------------------------------

# Anonymous functions(Lambda)
