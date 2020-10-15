import matplotlib.pyplot as plt 
import math 

# from TMU import *
# import TMU as t

# n = t.Number(10011)
# n.bin2dec()
# print(t.isPrime(70))
# n = Number(10011)
# n.bin2dec()
# m = Number(19)
# m.dec2bin()

# f = open('data.txt')
# content = f.read()
# content = f.readline()
# print(content)
# content = f.readline()
# print(content)
# content = f.readlines()
# print(content)
# f.close()

# with open('New folder/data.txt') as f:
#     content = f.readlines()

# print(content)

# with open('data1.txt', 'w') as f:
    # f.write('Hi there!')
    # f.writelines(['Hi there!\n', 'This is python tutorial!'])

# with open('data1.txt', 'a') as f:
#     f.write('Good bye!')

X = [1, 2, 4.5, 10, 14]
Y = [15, 12, 16.5, 14, 28]

# fig = plt.figure()
# plt.subplot(121)
# plt.plot(X, Y, 'r--x')
# plt.title('Sensor Measurments')
# plt.xlabel('Voltages')
# plt.ylabel('Currents')
# plt.xticks([7, 11])
# plt.yticks([10, 20, 25])
# # plt.axis('off')
# plt.grid()
# plt.subplot(122)
# plt.plot(Y, X, 'b--s')
# plt.show()
# #  fig.savefig('Plot.pdf')

# fig, ax = plt.subplots(2, 2, figsize=(10, 10))
# ax[0, 0].plot(X, Y, 'b--o', label='Exp1')
# ax[0, 0].plot(Y, X, 'g--o', label='Exp2')
# ax[0, 0].legend()
# ax[1, 1].plot(X, Y, 'b--o', label='Exp1')
# ax[1, 1].set_title('Voltages vs Currents')
# plt.show()

# X = [i for i in range(100, 500, 30)]
# Y = [150 + 80 * math.sin(i * 0.1) for i in X]

# img = plt.imread('gilbert.jpeg')
# fig = plt.figure()
# plt.imshow(img)
# plt.plot(X, Y, 'r--x', label='Sinusoidal')
# plt.text(200, 200, 'Gilbert Strang', fontdict={'color':'red', 'size':18, 'backgroundcolor':'green'})
# plt.axis('off')
# plt.legend()
# plt.show()
# fig.savefig('newgilbert.jpg')