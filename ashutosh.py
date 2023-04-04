# Q. what is module and how to create ?
# ans. consider a module to be the same as a code library. A file containing a set of functions
# you want to include a application .0
# ................................................
#module ko import karte hai dusri file me se 
# first example
'''import abcd
print(abcd.ashu(10,5))
print(abcd.tawar(5,5))'''

# ab jaise hamari file ka name bahut bada hai to hame use chhota karke use karna hai to asse karte hai 
# second example
'''import abcd as a
print(a.ashu(10,5))
print(a.tawar(5,5))'''

# ab ham ye chahte hai ki abcd se me access ho jana chahiye data or a se bhi to uske liye ye karna hoga
# third example
'''import abcd as a
import abcd
print(abcd.ashu(10,5))
print(a.tawar(5,5))'''

# ab ham ye chate hai ki ye ashu wale function ko ya tawar wale ko darectally call karna hai to 
#fourth example
'''from abcd import ashu
from abcd import tawar
print(ashu(10,5))
print(tawar(5,5))'''

# achha suppose hame tisare function boss ko bhi call karna hai to phir same process hogi 
# but module ke pass 100 function hai to hame to ye 100 times baar likhna padega to isse bachne ke 
# liye kya karna 
# fifth example
'''from abcd import *
print(ashu(10,5))
print(tawar(5,5))
print(boss(25,20))'''

# ab ham ye chahte hai ki hamne module jaha create kiye hai us file ko dusre folder me rakh dete hai to
# us condition me ham kaise uske data ko access kar sakte hai 
# six example 
'''from second.abcd import *
print(ashu(10,5))
print(tawar(5,5))
print(boss(25,5))'''

#example seven
'''import second.abcd
print(second.abcd.ashu(10,5))
print(second.abcd.tawar(5,5))
print(second.abcd.boss(25,5))'''

# ab jaise hamara module dusre folder ke ander bhi ek folder hai usme rakha hai or hame access karna hai to hame 
# ye karna hoga
'''from second.third.xyz import *
print(ashu(25,25))
print(tawar(25,20))
print(boss(250,150))'''

# kya ham module ke ander varible ko define kar sakte hai kya to bilkul kar skate hai jaha par module 
# create kiya hai vaha par varible define karte hai
'''import abcd
print("x=",abcd.x)'''

# abhi module ke ander class banate hai or usko show karate hai to sabse pahle hame class A ka object banana 
# padega then object.fuction name likh kar run karna padega.. or ek sath ham sabhi to comma ke sath access kar
# sakte hai jaise

'''from second.third.ashu import A,B,x,multi
a1 = A() # class a ka a1 object bana liya
a1.show()
b1 = B()
b1.show1()
print("x",x)
print(multi(7,2))'''

#-------------------------------------------------------------------------------------------------------------------
#  Loops 
# while loops--> with the while loop we can execute a set of statements as long as condition is true..
# while loop tab tak execute hota rahega jab tak condition true hai jaise condition false hoti hai baise loop
# break ho jayega..
# First example
'''
i = 1 # sabse pahle inisilisation hoga 
while(i<5): # condition check hogi agr true hogi condition to  
    print("Jai Shree Radhe krishna") # ye body ka code execute hoga 
    i=i+1
print("jai shree ram")'''

# example second





