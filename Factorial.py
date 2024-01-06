import math # using yield and for loop and predefined functions.
def gen():
    for i in range(5,10):
        yield math.factorial(i)  
g1=gen()
for p in g1:
    print(p) 
    
def fact(s, e): # using yield and for loop and no predefined functions.
    for i in range(s, e+1):
        f=1
        for j in range(1,i+1):
            f=f*j
        yield f
g=fact(5,10)
for p in g:
    print(p)
