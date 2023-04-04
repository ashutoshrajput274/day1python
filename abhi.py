#Q.1 Captcha Code
'''import random
r=''
for i in range(6):
    ashu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#&0123456789'
    a = random.choice(ashu)
    r += a
print(r)'''

'''# While try and except block :- while block is used for making process continues till the
exception is occuring..'''

'''while True:
    sal=input("enter your salary")
    try:
        sal=int(sal)
        if sal<0:
            print("enter positive value")
            continue
    except:
        print("please enter salary ony in no")
        continue
    else:
        print(sal)
        break'''
    
''' Q:2. Write atm program. enter account balance, print beginning balance. ask for deposite
      or withdrawl, depending on selection, call function to perform the action they wish,
      then print new balance.(use iteration) ''' 
'''
while True:
    print ("current balance:$")
    choice=int(input("please choose an option:\n1-withdraw \n 2- deposite \n3-check balance \n4-exit\n select your choise"))
    if choice==1:
        print('withdraw()');
    elif choice==2:
        print('deposite()');
    elif choice==3:
        print('balance()');
    
    more = input("would you like another transation ? (y/n)")
    if more.lower()!='y':
        print("goodbye")
        break'''

    
#Q. Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
#  between 1500 and 2700 (both included).
'''
for x in range(1500,2701):
    if (x%7==0) and (x%5==0):
     print(x,end=' ')'''
'''nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))'''
     

'''3. Write a Python program to guess a number between 1 to 9. Go to the editor
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears
again until the guess is correct, on successful guess, user will get a "Well guessed!" message,
and the program will exit.'''

'''guess = 5
while True :
    user = int(input("enter a number"))
    if user==guess :
        print("your guessing is perfactlly")
        break
    else:
        print("not well guess")'''
    
'''4. Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*'''

'''a=5
for i in range (1,6):
    print('* ' *i)
for j in range (1,5):
    print('* '*(a-j))'''

'''n=5
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')'''
#Q.your age is gretor then 18 you can drive, your age less then 18 you can't drive
# your age 18 then test drive and decided.. 
'''a=int(input("enter your age"))
if a<18:
    print("you can't drive")
elif a==18:
    print("test drive then dicided")
else: 
    print("you can drive")'''

#Q.
rows = 7

for i in range(0, rows):

    for j in range(0, i + 1):

        print('* ', end= '')

    print()

'''for i in range(1,6):
    
    for j in range(1,i+1):
        print("* ",end="")
        j=j+1
        i=i+1
    print()'''
    
    
'''n=6
for i in range(1,6+1):
    print(" "*(6-i)+"* "*i)

     * 
    * *     
   * * *    
  * * * *   
 * * * * *  
* * * * * * '''

'''for i in range(6,0,-1):
    print(" "* (6-i)+"* "*i)
    
* * * * * * 
 * * * * * 
  * * * *  
   * * *   
    * *    
     *    ''' 
     
'''for i in range(6,0,-1):
    print(" "*(6-i)+"* "*i)
for i in range(0,6+1):
    print(" "*(6-i)+"* "*i)'''
    
'''* * * * * * 
    * * * * *
     * * * *
      * * * 
       * *
        *
   
        *
       * *
      * * *
     * * * *
    * * * * *
   * * * * * *'''

'''a = 7
b = 8

if a<b:
    print(a,"smaller is", b)'''
    
i = 1
while i<=7:
    print(i)
    i+=1