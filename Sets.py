# Set objects can be created by using {} are by calling set() function.
# set is a mutable object.
# duplicate elements are not allowed in Sets.
# insertion order is not preserved.
# set does not support indexing and slicing.
# set is a collection of homogeneous and heterogeneous elements.    
# set is mainly used to perform the mathematical operations like union, intersection, difference, symmetric difference, subset, superset, disjoint, etc.

s=set
type(s)

s={10,40,50,60,70,80,90,100}
s.add(200)
print(s)

s=input()
r=set(s)
l=list(r)
l.sort()
for p in l:
    print(p,"=",s.count(p))

s=input()
r=set(s)
for i in sorted(s):
    c=s.count(i)
    print(i,"=",c)

s=input()   
r=set(s)
l=list(r)
l.sort()
res=''
for p in l:
    res=res+p+str(s.count(p))
    print(res)    

s=input()   
r=set(s)
l=list(r)
l.sort()
res=''
for p in l:
    if s.count(p) > 1:
        res=res+" "+p+"-"+str(s.count(p))
print(res)

# Matheatical operations on sets:-

a={10,20,30,40,50}
b={60,70,80,90,100}
s=a.union(b)
s1=a.intersection(b)
s2=a.difference(b)
s3=b.difference(a)
s4=a-b
print(s,s1,s2,s3,s4,sep="\n")
print(a.union(b))

n=int(input())
l=list(map(int,input().split()))[:n]
n=int(input())
r=list(map(int,input().split()))[:n]
s1=set(l)
s2=set(r)
print(s1,s2)
s3=s1^s2
for p in s3:
    print(p)

s={1,2,3,4,5}
print(s.add(6))
print(s.remove(4)) #if element is not present in set then it will raise an error
print(s.discard(7)) #if element is not present in set then it will not raise an error
print(s.pop())
print(s.clear())

# code for the same element in two strings:
s1=input()
s2=input()
set1=set(s1)
set2=set(s2)
d1=sorted(set1 & set2)
d2=''.join(d1)
print(d2)

