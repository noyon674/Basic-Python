'''
   Arithmetic operators
'''
a, b = 21, 5
print(a+b) #Addition
print(a-b) #Substraction
print(a*b) #Multiplication
print(a/b) #Division with float point
print(a%b) #return remainder
print(a**b) #return exponentiation, b time a multiplication
print(a//b) #Division result without float point

'''
   Assignment operators
'''

#direct assign
x = 30
y = 5
x += y # x = x+y; x = 30+5
print(x)
'''
   similarly [ x-=y, x*=y, x/=y, x%=y, x//=y, x**=y ]
'''


'''
   Comparison operator 
'''
print(10 == 10)
print(10 != 5) ##It means 10 not equal 5. that is true.
print(20>5) ##20 is greater than 5
print(3 < 5) ## 3 is less than 5

## 4 is less than or equal 5
print(4 <= 5)  ##this time '<' condition true
print(4 <= 4) ##this time '=' condition true

## 10 is greater than or equal 7
print(10 >= 7) ##this time '>' condition true
print(10 >= 10) ##this time '=' condition true


'''
  Logical operators
'''
print(10 > 5 and 40 >  15) ##return true when both statements are true
print(20 > 5 or 30 > 4) ##return true when only one/ both statements are true

## not return reverse value: if condition is 'true' then 'not' return 'false'; if condition is 'false' then 'not' return 'true'
print(not (20 > 5 and 30 > 4))
print(not (20 < 5 and 30 < 4))


'''
   Identity operators
'''
a = [2, 5]
b = [2, 5]
c = a
print(a is c) ## returns true when both variables are in the same object, Here a and c are same object
print(a is b) ##Here a and b are not same object
print(a is not b) ##It returns true coz a and b is not same object though they are same content

'''
  Membership operator
'''
name = 'Noyon'
print('N' in name) ## 'N' is contain into name ? if conditon is true then it return true
print('i' in name)
print('m' not in name) ## 'm' is not into the name variable this is true.


