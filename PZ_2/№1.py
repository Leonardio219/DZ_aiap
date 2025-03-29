from matplotlib import pyplot as plt
x = [x for x in range (10)]
y1 = [x for x in range (10)]
y2 = [x*2 for x in range (10)]
y3 = [x*3 for x in range (10)]
y4 = [x**2 for x in range (10)]
y5 = [2*x**2 for x in range (10)]
plt.plot (x, y1, color='r', label='y1 = x')
plt.plot (x, y2, color='g', label='y2 = x*2')
plt.plot (x, y3, color='b', label='y3 = x*3')
plt.plot (x, y4, color='k', label='y4 = x^2')
plt.plot (x, y5, color='c', label='y5 = 2*x^2')
plt.show()