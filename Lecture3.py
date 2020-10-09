def findAverage(g):
    return sum(g)/len(g)

# grades = []

# while True:
#     grade = float(input('Enter a grade please: '))
#     if grade<0:
#         break
#     grades.append(grade)

# print('The average is: ', findAverage(grades))
# print(findAverage(grades))

s = 'hello everyone!'
# print(s.capitalize())
# print(s.count('ll'))
# print(s.endswith('hi'))
# print(s.startswith('bye'))
# index = s.find(' ')
# print(s[:index])
# print(s[index+1:])
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())
# print(s.islower())
# print(s.isupper())
# print(s.lower())
# print(s.upper())
# print(s.replace('e', '*'))

# grades = [20, 19, 18]
# # grades = ['20', '19', '18']
# s = '***'
# print(s.join([str(i) for i in grades]))

# grades = '20, 18, 19, 15, 16 - 17 - 19 * 12'
# grades = grades.replace('-', ',')
# grades = grades.replace('*', ',')
# print(grades)
# print(grades.split(','))

# grades = input('Please enter all the grades with commas between them: ')
# grades = grades.split(',')
# grades = [float(i) for i in grades]
# print(grades)

def getGrades():
    return [float(i) for i in input('Enter your grades please: ').split(',')]

# grades = getGrades()
# average = findAverage(grades)
# print('The Average is: ', findAverage(getGrades()))


# print('Name is: ', fn[1], ln[1], 'Phone: ', pn[1])

class Student:
    def __init__(self, first_name, last_name, id):
        self.fn = first_name
        self.ln = last_name
        self.id = id
        self.grades = []

    def setGrades(self):
        self.grades = [float(i) for i in input('Enter the grades please: ').split(',')]

    def getAverage(self):
        return sum(self.grades) / len(self.grades)

    def getMin(self):
        return min(self.grades)

    def getMax(self):
        return max(self.grades)

    def display(self):
        print(f'Firstname: {self.fn}\tLastname: {self.ln}\tID: {self.id}')
        print('Grades: ', self.grades)
        print('Average: ', self.getAverage())
        print(f'Min: {self.getMin()}\tMax:{self.getMax()}')

a = Student('Mohammad Hossein', 'Amini', 9423013)
a.setGrades()
a.display()
