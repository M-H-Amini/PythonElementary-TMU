'''
print('Hi there!', end=', ')
print(1399, end=', ')
print("MH")

#  Printing my name...
print('My name is "MohammadHossein"')
print("My name is 'MohammadHossein'")
input('Please Enter Something: ')

name = input('Enter your name please: ')
print('Hello ', name)

a = 5
print(a)
print(2 * a)
b = a + 10
print(b)
a = 28
print('a is', a)

m = 10
v = 10
k = 0.5 * m * v**2
print('Mass is', m)
print('Velocity is', v)
print('Kienetic Energy is', k)
m = 15
k = 0.5 * m * v * v

a = 5
print(type(a))
a = 5.5
print(type(a))
a = 'Salam'
print(type(a))

a = 20
b = 19
c = 17.3
d = 16
e = 19.5

##  List...
grades = [20, 19, 17.3, 18, 20, 17, 16, 19.5]
# print(type(grades))
# print(grades[1])  #  Indexing
# print(grades[-2])
# print(grades[1:5])  #  Slicing...[a, b]:a, a+1, ..., b-1
a = grades[1: 5]
# print(type(a))
# print(len(grades), len(a))
# a.append(18.5)
# print(grades)
# print(a)
# grades.append(a)
# print(len(grades))
# print(grades[-1][-2])
# grades.extend(a)
# print(grades)
# grades = grades + a
# print(grades)
# grades.insert(1, 10)
# print(grades)
# grades.pop()
# print(grades)
# grades.remove(19)
# print(grades)
print(grades)
grades[0] = 18
print(grades)

# grades = (19.5, 17.3, 16)
grades= 19.5, 17.3, 16
print(grades[0])
print(grades[0:3])
# grades[0] = 20
print(type(grades))

a, b, c = grades
print(c)
#a, *b = grades
#print(b)

a = [20, 16.5, 'Hi']
print(a[-1])
'''

# password = input('Enter your password please: ')


# if password=='Hello':
#     print('Hi There!')
#     print('Logged in!')
# elif password=='Hossein':
#     print('Hi Hossein!')
# elif password=='TMU':
#     print('Hi TMU!')
# elif password=='1398':
#     print('Hi 1398!')
# else:
#     print('Incorrect password!!!')

# if type(int(password))!=type(15):
#     print('Incorrect Password!')

# print('Bye')

n = int(float(input('Please enter a number: ')))

if not n%2:
    print('Even')
else:
    print('Odd')
