'''
  Dictionary stores key value pairs
'''

person = {
    'name': 'Noyon',
    'age': 23,
    'Profession': 'Engineer'
}

print(person)
print(person.get('name'))# returns name's value

print(person.keys())## returns all keys
print(person.values())## returns all values

person['age'] = 30 ##value changing
print(person.get('age'))

person['height'] = '5.7 feet' ## adding new elements
print(person)

print(person.items()) ## returns key and value pairs

##check key is exist
if 'age' in person:
    print('yes')


'''
  Loop
'''
for i in person.keys():
    print(i)

for j in person.values():
    print(j)

for x, y in person.items():
    print(x, y)


a = person.copy() ## copy dictionary
print(a)