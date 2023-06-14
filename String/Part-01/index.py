############## String:
Name = 'Noyon Sarker'
txt = '''Hi, My name is Purna.
I am student of Daffodil International University
'''
print(Name)
print(txt)

############## Strings are Arrays
a = 'Hello world'
print(a[0])

############## Looping through a string and find each letter
for i in 'Noyon':
    print(i) #This line into the for loop

print(len(Name)) #returns length of string

############### Check String
if 'is' in txt:
    print('Yes')
    
print('Hi' in txt) #It returns boolean value 'true'


################## check if not
if 'is' not in txt:
    print('Yes, is not here.') #'is' contain into the txt.That's why 28 no. line is not run
    
print('is' not in txt) #It returns boolean value 'false'


################## Slicing String:
a = 'Hello world'
print(a[2:6]) #start included but end not included
print(a[:3]) #It returns start to index 2, (end not included)
print(a[3:]) #It returns index 4 to end, (start included)

#### Negative indexing counting from the end
print(a[-5:-2]) #It is easy to understand if you consider it a[end:start]. start(include), end(exclude)


#################### Modify String
let = 'I Love You'
print(let.upper()) #return a Upper-Case string 
print(let.lower()) #return a Lower-Case string

##################### strip():
x = '         Hi'
print(x.strip()) #This method remove whitespace

###################### replace():
print(let.replace('Love', 'Hate'))

###################### split():
print(let.split(' ')) #slipt('x') method convert a string into list & devide string when it find 'x' using ','


####################### String concatenation
m = 'Hello'
n = 'World'

print(m + n)
print(m+" "+n)


####################### format():
'''
format method takes number arguments and insert into string
'''
age = 23
money = 20304
test = 'My name is Noyon. My age is {}'
test2 = 'My name is Noyon. My age is {}. My salary is monthly {} taka.'
print(test.format(age))
print(test2.format(age, money))


