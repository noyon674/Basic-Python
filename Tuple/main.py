'''
   Tuple
'''

Tuple = ('Noyon', 'Purna', 'Ope', 'Rizwan')
print(Tuple)
print(type(Tuple))
print(Tuple[-1])

tuple2 = ('Noyon') ##not a tuple
print(type(tuple2))

tuple3 = ('Noyon',) ##creating a tuple with single value
print(type(tuple3))

##convert a tuple to list and list to tuple
x = list(Tuple)
print(x)
y = tuple(x)
print(y)

##add new item. 1st conver tuple to list then add and then convert list to tuple
x.append('Baby')
m = tuple(x)
print(m)

## similarly removes item

newTuple = (2,4,6,5,8,7)

##unpack tuple
(a, b, c, d) = Tuple
print(a, b, c, d)

(a, b, *c) = newTuple
print(a, b)
print(c) ## *c store a list of value

(x, *y, z) = newTuple
print(x, z)
print(y)

'''
  Loops
'''
for i in newTuple:
    print(i)


## join tuple
print(Tuple + newTuple)
print(Tuple * 3) ## Tuple adding 3 times