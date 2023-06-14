'''
  List
'''

fruits = ['apple', 'banana', 'mango', 'cherry']
print(fruits)
print(type(fruits))
print(fruits[2])
print(len(fruits))
fruits[2] = 'Tomato' ## changing value
print(fruits)

fruits.append('orange') ## add new item to the list
print(fruits)

fruits.insert(2, 'kola') ##add new item into specific index
print(fruits)

arr = [2,4,6,7]
arr.extend(fruits) ## add 2 list or any iterable object
print(arr)

fruits.remove('apple') ##removing item by item's name
print(fruits)

fruits.pop(3) ## removing item from specific index
print(fruits)

## del method also delete specific index value and total list object
del fruits[0]
print(fruits)

del fruits

a = [5,35,7]
print(a)
a.clear()
print(a)


### Loops of list

aa = [4,6,2,6,8,0,3,5,7,10]
for i in aa:
    print(i)
aa.sort()
print(aa) ## sorting assending order
aa.reverse()
print(aa)

## copy list

bb = aa.copy()
print(bb)
