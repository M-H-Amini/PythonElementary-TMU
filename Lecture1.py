# grade = 5.5

# if grade >= 17:
#     print('A')
# elif grade >= 14:
#     print('B')
# elif grade >= 10:
#     print('C')
# else:
#     print('D')

# print('Hi there!')

# print("Hi there! We're going to calculate your average!")
# math = float(input('Please enter your math grade: '))
# physics = float(input('Please enter your physics grade: '))
# chemistry = float(input('Please enter your chemistry grade: '))

# avg = (math + physics + chemistry) / 3
# print(f'Your average is {avg}!')

# grades = [20, 19, 16.2, 14, 9.5, 20, 0]

# avg = sum(grades) / len(grades)

# print(f'Your average is {avg}!')

# range(a, b)  -> [a, a+1, ..., b-1]
# range(a) === range(0, a) -> [0, 1, ..., a-1]
# range(a, b, c)
# for i in range(20):  #  range(20) -> [0, 1, 2, ..., 19]
#     print(f'i = {i}')
#     print('Hi')
#     print('Bye')

# print('This is the end!')

##  Sum of numbers from 1 to 100
# s = 0
# for i in range(101):
#     s += i
# print('The sum is:', s)

##  Average of numbers from 1 to 100
# s = 0
# for i in range(101):
#     s += i
# s /= 100
# print('The average is:', s)

##  Multiples of 5 from 0 to 100
# l = []
# for i in range(101):
#     if not i%5:  #  if i % 5 == 0:
#         l.append(i)
# print(l)
# l = [i for i in range(101) if not i%5]  #  List comprehension
# print(l)

##  Factors of 24
# l = []
# for i in range(1, 25):
#     if not 24 % i:
#         l.append(i)
# print(l)
# l = [i for i in range(1, 25) if not 24%i]
# print(l)
# l = []
# for i in range(1, int(24/2) + 1):
#     if not 24 % i:
#         l.append(i)
# l.append(24)
# n = 25465
# l = [i for i in range(1, int(n/2) + 1) if not n % i]
# l.append(n)
# print('Factors: ', l)
# print('No of factors: ', len(l))

##  If n is prime?
# n = 6
# l = [i for i in range(1, int(n/2) + 1) if not n % i]
# l.append(n)
# if len(l) == 2:
#     print("It's prime!")
# else:
#     print('Not prime!!')

# n = 29
# flag = True
# for i in range(2, int(n/2) + 1):
#     if not n % i:
#         flag = False
#         break

# if flag == True:
#     print("It's prime!")
# else:
#     print("It's not prime!")

##  Exercise: Print all prime numbers from a to b
# a = 100
# b = 10000
# l = []

##  List, Tuple
##  Dictionary, Set
##  Key:Value
# grades = {'Mohammad':20, 'Shayan':20, 'Hasan':19.5}
# grades['Ali'] = 17
# print(grades)
# print(grades.keys())
# print(grades.values())
# l = [5, 2, 49]
# for i in l:
#     print(i)
# for name in grades.keys():
#     print('Name: ', name, '\tGrade:', grades[name])
##  Exercise: Find the average of grades

# s = {1, 1, 1, 2}
# t = {2, 3}
# print(s, t)
# print(s.union(t))
# print(s-t)
# #print(s[0])
# for i in s:
#     print(i)

# id = [5, 6, 7, 5, 5, 9, 6]
# s = set(id)
# print(s)

# d = {key:2*key for key in range(10)}
# print(d)