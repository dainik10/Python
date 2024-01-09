def smart_div(d):
    def division(a,b):
        if type(b)==str:
            return "Second input must be integer"
        else:
            return d(a,b)
    return division
@smart_div
def div(a,b):
    return a/b
a=div(10,2)
print(a)
a=div(10,"abc")
print(a)

# Dictionary object can be created by using {} are by calling dict() function.
# dictionary is a mutable object.
# insertion order is preserved.
# indexing and slicing is not supported.
# duplicate keys are not allowed.
# duplicate values are allowed.
# dictionary is a collection of homogeneous and heterogeneous keys and values.
# dictionary is a collection of key-value pairs.
# the key and value pair are called items.

d={}
type(d)
d=['a':10,'b':20,'c':30]
print(d)
d['a']=60
print(d)


e={"Name":"Raj","id1":101, "Dept":20, "Salary":70000}
print(e)
print(e["Dept"])
d=e.get("Salary")
print(d)
e["Salary"]=80000
print(e)
e["subject"]="python"
print(e)
for p in e.keys():
    print(p)
for p in e.values():
    print(p)
for p,q in e.items():
    print(p,q)        
for s in e.items():
    print(s)       
for s in e.items():
    print(s[0],s[1])
r=sorted(list(e.keys()))
print(r)        
   
# Dictionary comprehension: the concepts of generating elements into dictionary object by writing some logic in the dictionary oios called as dictionary comprehension. By using the dictionary comprehension we can reduce the number of lines of code

# Write a program to print the square of the given number from 1 to 20.
d={p*p for p in range(1,20) if(p%2==0)}
print(d)

# Write a program to print cubes of the odd number from 30 to 50
d={p*p*p for p in range(30,50) if(p%2!=0)}
print(d)

x="Mumbai"
d={p:x.count(p) for p in x}
print(d)

# write a prog to read string from the user and print vowel characters count
s = input()
vowels = 'aeiouAEIUO'
d={p:s.count(p) for p in s if p in vowels}
print(d)


# print the maximum repeated vowel character from the given string.
s = input()
vowels = 'aeiouAEIUO'
d={p:s.count(p) for p in s if p in vowels}
max_vowel = max(d, key=d.get)
print(max_vowel)

s = input()
vowels = 'aeiouAEIOU'
d={p:s.count(p) for p in s if p in vowels}
m=max(d.values())
for p,q in d.items():
    if q==m:
        print(p)


# replacement of the maximum repeated vowel character from the given string (Accenture).        
x = input() #1
f = {char: x.count(char) for char in set(x)}
m = max(f, key=f.get)
r = input()
if m != r:
    s=x.replace(m, r)
print( s)

s=input() #2
x=input()   
d={p:s.count(p) for p in s}
m=max(d.values())   
l=[]
for p,q in d.items():
    if q==m:
        l.append(p)
l.sort()
res=''
for p in s:
    if p in l:
        res=res+x
    else:
        res=res+p
print(res)                

st=int(input()) #code for key=value means if 3 comes 3 times then ans is 3
l=list(map(int,input().split()))[:st]
n=[]
d={p:l.count(p) for p in l}
for p,q in d.items():
    if q==p:
        n.append(p)
if(n==[]):
    print("-1")
else:
    print(max(n))       

d={"raju":45,"ravi":50,"rajesh":60,"rakesh":2,"raj":80}
r=sorted(d.keys())
e={}
print(r)
for s in r:
    for p,q in d.items():
        if s==p:
            e.update({p:q})
            break
print(e)        
        
d={"raju":45,"ravi":50,"rajesh":60,"rakesh":2,"raj":80}
r=sorted(d.values())
e={}
print(r)
for s in r:
    for p,q in d.items():
       if s==q:
           e.update({p:q})
           break
print(e)        
            
            
# A dictionary within the another dictionary is called as nested dictionary

d={"Krishna":[45,67,89],"Raju":[56,78,90],"Ravi":[67,89,90],"Rajesh":[78,90,100]}
for p,q in d.items():
    print(p)
    s=sum(q)
    avg=s/len(q)
    print("Avg:%.2f"%avg)
 
to find the avg marks of a student from a dictionary    
n=int(input())
d={}
for i in range(n):
    st=input()
    l=st.split(" ")
    d[l[0]]=[int(l[1]),int(l[2]),int(l[3])]   
name=input()
for p,q in d.items():
    if name==p:
      s=sum(q)
      avg=s/len(q)
      print("Avg:%.2f"%avg)
             

d={"Krishna":{"Python":23,"Java":45, "C":67},"Raju":{"Python":56, "Java":78, "C":90}, "Ravi":{"Python":67, "Java":89, "C":90},"Rajesh":{"Python":78, "Java":90, "C":100}}  
for i,j in d.items():
    print(i)
    for p,q in j.items():
        print(q)
print()    
        
            
# String Methods:-    
s="Good Morning all"
r=s.split()
print(r)
for p in r:
    print(p) 

s=["Good","Morning","all"]
r='-'.join(s)
print(r)
r=" ".join(s)
print(r)
