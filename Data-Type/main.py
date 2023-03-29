'''
 // Data Types
'''

## String type
a = 'Noyon'
b = '40'
print(a, b)
print(type(a), type(b))

## Number types
Integer = 23
Float = 30.5
Complex = 30j
print(Integer, Float, Complex)
print(type(Integer), type(Float), type(Complex))

## Sequence types
List = [3,5,'Noyon', 50]
Tuple = ('a', 'b', 'c', 6, 7)
Range = range(10)
print(List,";", Tuple,";", Range)
print(type(List), type(Tuple), type(Range))

## Mapping type: a set of (key-value) pairs
Map = {'Bangladesh':'Dhaka', 'India': 'Delhi', 'Japan': 'Tokyo'}
print(Map)
print(Map['Bangladesh']) ## It return 'Dhaka'
print(type(Map))

## Set types
Set = {2,3,4,2, 'noyon', "noyo"} ## set store unique value
print(Set)
print(type(Set))

## frozenset type
Frozen = ({2,4,6,7}, {3,5,7,4}, {2,4})
print(Frozen, "; ", Frozen[0])
print(type(Frozen))

## Boolean types
x = True
y = False
print(x, y)
print(type(x), type(y))

## None type
z = None
print(z)
print(type(z))