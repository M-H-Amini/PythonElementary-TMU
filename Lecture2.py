# for i in range(1, 100, 2):
#     print(i)

# a = 99
# while a >= 1:
#     print(a)
#     a = a-2

# g = float(input('Enter the grade: '))
# s = 0
# n = 0
# while g!=-1:
#     s += g
#     n += 1
#     g = float(input('Enter the grade: '))

# print('The average is: ', s / n)

# s, n = 0, 0
# while True:
#     g = float(input('Enter the grade: '))
#     if 0 <= g <= 20:
#         s += g
#         n += 1
#     else:
#         break

# print(f'The average is : {s/n:4.2f}')

def factors(n):
    # f = []
    # for i in range(1, int(n/2) + 1):
    #     if not n%i:
    #         f.append(i)
    # f.append(n)
    # print(f)
    f = [i for i in range(1, int(n/2) + 1) if not n%i]
    f.append(n)
    return f

# a = factors(24)
# b = factors(30)
# print(a + b)

def isPrime(n):
    f = factors(n)
    if len(f) == 2:
        return True
    else:
        return False

#print(isPrime(11))

def primes(a, b=1000):
    # p = []
    # for i in range(a, b):
    #     if (isPrime(i)):
    #         p.append(i)
    return [i for i in range(a, b) if isPrime(i)]

# print(primes(100))

grades = [20, 20, 10]
# s = 0
# for g in grades:
#     s += g
# print('Average: ', s/len(grades))

def average(grades):
    return sum(grades)/len(grades)

print(average(grades))

a = 1 + 1j
b = 1 + 1j
# print(a + b)

def firstPrimes(n):
    p = []
    i = 2
    while (len(p) < n):
        if isPrime(i):
            p.append(i)
        i += 1
    return p

print(firstPrimes(1000))