# function ia a subprogram that performs a specific operation.
# A self contained block of one or more statements is called as function.
# Advantages of functions:
#     a self contained block of one or more statements is called as function.
#     code reusability(writing the code once and use it multiple times).
#     Understanding the logic becomes easy.
#     in python programming we can define a function using def keyword.
#     functions are divide into 4 types:
#         1.function without arguments and without return type.
#         2.function with arguments and without return type.
#         3.function with arguments and with return type.  
#         4.function without arguments and with return type.

def even_odd(): #function without arguments and without return type
    n=int(input())
    if n%2==0:
        print(n,"is even number")
    else:
        print(n,"is odd number")        
even_odd() # function calling    
 

def even_odd(n): #function with arguments and without return type
    if n%2==0:
        print(n,"is even number")
    else:
        print(n,"is odd number")  
n = int(input())              
even_odd(n)

# in this approach we pass the argument from main program to sub program and we get the result from sub program to main program.

def even_odd(n): #function with arguments and with return type
    if n%2==0:
        return 1
    else:
        return 0
n = int(input())              
s=even_odd(n) 
if (s==1):
    print(n,"is even number")
else:
    print(n,"is odd number")  

n = {
    'A'==1,
    'B'==100,
    'C'==1000,
    'D'==10000,
    'E'==100000,
    'F'==1000000,
    'G'==10000000
}

def letterNumber(letter):
    return n[letter]

def sumvalues(letters):
    sum=0
    for letter in letters:
        sum+=letterNumber(letter)
    return sum

print(sumvalues('DDCD'))
    
def weight(p):
    w=10**(ord(p)-ord('A'))
    return w
d=input()
s=0
for p in d:
    r=weight(p)
    s=s+r
print(s)

def check_palindrome(i):
    r=i[::-1]
    if i==r:
        return 1
    else:
        return 0    

n=int(input())
s=input()[:n]
t=s.split()
flag=False
for i in t:
    if check_palindrome(i) ==1:
        flag=True
    else :
        flag=False

if flag==True:
    print("Yes")
else:
    print("No")
    
    
a=input()
b=input()
c=input()
print(a.replace (b,c))    
    
    
# lambda is a special function.if the fumc doesn't have any name is called as lambda or anonymous function. 
# uisng the lambda func we can reduce no of lines in our Code. 
# lambda is called as higher order function.
          
s=lambda a,b:a+b
r=s(10,5)
print(r)

s=lambda x:x%2==0
l=[1,2,3,4,5,6]
r=[p for p in l if(s(p))]
print(r) 

s=lambda x:x%2!=0
r=[p for p in range(30,50) if(s(p))]
print(r)                   

# Write a program to find the factorial of the numbers from 5 to 10 in 3 lines
f = lambda n: 1 if n==0 else n*f(n-1)
print([f(i) for i in range(5, 11)])

import math
print([math.factorial(i) for i in range(5, 11)])

# Write a prog to perform add, sub, mul, div using single function and lambda function
def cal(f, a, b):
    return f(a, b)

add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b if b != 0 else 'Error: Division by zero'

print(cal(add, 10, 5))
print(cal(mul, 10, 5))
print(cal(div, 10, 5))
print(cal(sub, 10, 5))

def op(s, a, b):
    return s(a, b)
s1 =op(10,5, lambda a, b: a + b)
s2 =op(10,5, lambda a, b: a - b)
s3 =op(10,5,lambda a, b: a * b)
print(s1, s2,s3)

l=lambda a,b:[a+b,a-b,a*b,a/b]
x,y,z,w=l(10,5) 
print(x,y,z,w)

# Map and Filter Functions:
#     filter requires a condition but map requires a expression.

with filter and without lambda    
def even(n):
    return n%2==0
l=list(range(10,31))
r=list(filter(even,l))
print(r)

 with filter and lambda
l=list(range(10,31))
r=list(filter(lambda n:n%2==0,l))
print(r)


filter negative numbers with lambda
l=list(range(-10,31))
r=list(filter(lambda n:n<0,l))
print(r)

l=["abc", "DEF", "ghi", "JKL"] # filter upper case letters
r=list(filter(lambda s:s.isupper(),l))
print(r)

def sq(n)
    return n*n
l=[1,2,3,4,5]
r=tuple(map(sq,l))
print(r)

reduce function:
    its is a function that is imported from functools module.

from functools import reduce
s=[1,2,3,4,5]
r=reduce(lambda a,b:a+b,s)
r1=reduce(lambda a,b:a*b,s)
print(r,r1,sep="\n")  

from functools import reduce
s=[1,2,3,4,5]    
min = reduce(lambda a, b: a if a < b else b, s)
max = reduce(lambda a, b: a if a > b else b, s)
print(min, max)

   
        
