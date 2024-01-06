# tuple objects can be created by using () are by calling tuple() function.
# by assigning more than one value to a single variable tuple object is created.
# tuple is a immutable object.
# insertion order is preserved.
# duplicate elements are allowed in tuple.
# tuple supports indexing and slicing.
# tuple is a collection of homogeneous and heterogeneous elements.

t=()
print(type(t))

t=tuple()
print(type(t))

t=tuple(range(1,11))
print(t)

t=1,2,3,4,5,6,7,8,9,10 # by assigning more than one value to a single variable tuple object is created.
print(t) 
print(type(t))
