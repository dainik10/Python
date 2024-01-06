
s=[1,2,3,4,5] # iterator
r=iter(s)
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r)) # StopIteration error will occur.

l=[1,2,3,4,5] # enumerator
r=enumerate(l)
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
l=[10,20,30,40,50] 
r1=enumerate(l,5)
print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))

def gen(): # generator
    yield 1
    yield 2
    yield 3
    yield 4
g1=gen()
r=next(g1)
r1=next(g1)
r2=next(g1)
r3=next(g1)
print(r,r1,r2,r3)
