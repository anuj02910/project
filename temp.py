# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Arithemetic operator
a=10
b=20

a+b    #addition

a-b    #substraction

a*b    #Multiplication

a/b   #divison

a//b  #remove decimal

b%a  #remainder 20/10=0(remainder)

a**b #expontenial


#comparison operator
a=15  #Assignment
a==b #verifying

a!=b #not equal to

a>b

a<b

a>=b
a<=b


#assignment operator
c=a+b
c

c+=b #c=c+b
c

c-=b  #c=c-b
c

c*=b
c

c/=b
c

c%=b
c
c**=b
c

c//=b
c

a=60
b=13

format(a,"b")#binary format
format(b,"b")
help(format)
help("FORMATTING")

#help function help us 

#membership operator #in #bollean values #in and not in  
'i' in "nikhil"
'l' in "nikhil"
'p' in "nikhil"
'p' not in "nikhil"

#identity operator
"nikhil" is "Nikhil"
1 is 1
1 is not 1

"Nikhil" is "Nikhil"
1 is 0
1 is not 0




#STRING 

Name="shubham"

Name

print(Name)
print(Name[-2])
Name[3]

print(Name[1:4])#1,2,3(hub)#upper limit is not consider
print(Name[2:-5])
print(Name[-1])
print(Name[-3:-1])#(-3,-2)(h,a)

#string update
var1="Hello world!"
output=var1+'python'
print("updated ",var1+' python')


#string formatting
#%s String
#%d Integers
#%f Floating point numbers
#%<numberof fraction we want>f
#% <number of digits


print("My name is %s and weight is %f kgs! my father name is %s" %('anil',70,'ramu'))

#hard coding

number=10
number=input("enter num: ")#soft coding
number_1=eval(input("enter number:"))#numerical

Name=input("Enter your name ")#string just input
weight=eval(input("enter your weight: "))#int or floata
(Name,weight)



#""" Triple quotes

#my name os 'nikhil' and my age is "25"


Name="shubham"
Name.upper()
Name.center(50)
Name.count("shubham")
string="sies is training institute"
substring="n"
count=string.count(substring)
count

print("the count is",count)
num="1234";
print(num.isalnum())#is all numerical or not

Num="this is string"
Num.isalnum()

Num="this"
Num.isalpha()

num="this is string06666"
num.isalpha()

num="this is string"
num.isdigit()

num="THIS IS SHUBHAM"
num.lower()

num="this is shubham"
alpha=num.upper()


#REPLACE() method
reply="it is string example is really a string "
replaced=reply.replace("is","was")
reply.replace("is","was",1)

split1="line1-abcdeabc"
split1.split("d")
