import random 
def gen():
    for i in range(4):
        yield random.randint(1000,10000)
g1=gen()
for p in g1:
    print(p) 
