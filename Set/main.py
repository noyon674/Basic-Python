'''
   Set always store unique value
'''
set = {'Noyon', 'Purna', 'Ope', 'Rizwan', 'Noyon'}
print(set)

set.add('Love')
print(set)

set2 = {2,4,6,8}
set.update(set2)
print(set)

##remove methods
set.remove('Ope')
print(set)

set.discard('Purna')
print(set)

set.pop() ## pop() method removes item from the first
set.pop()
print(set)

set.clear() ## clear() methods remove all elements
print(set)

## Loops
for i in set2:
    print(i)


'''
Join set
'''
a = {1,4,8,4,7,9}
b = {1,14, 23, 57, 9}

print(a.union(b))
a.update(b)
print(a)

a.intersection_update(b)
print(a)

z = b.intersection(a)
print(z)