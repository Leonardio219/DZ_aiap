from matplotlib import pyplot as plt
import numpy as np
x = np.random.uniform(-10.0, 10.0, size=5)
y = np.random.uniform(-10.0, 10.0, size=5)
color = ['r', 'g', 'b', 'orange', 'y']
label = ['p1','p2','p3','p4','p5']
print(x, y)
#plt.axis('equal')  # equal ломает лимиты по осям, так что и без него норм


for i in range(5):
    plt.plot(x[i], y[i], color=color[i], label=label[i], marker = 'o')
    plt.plot ([x[i]-1, x[i]+1], [y[i], y[i]], linestyle='-', color=color[i])
    plt.plot([x[i], x[i]], [y[i]-1, y[i]+1], linestyle='-', color=color[i])
    x1 = np.random.uniform(x[i]-1, x[i]+1, size=10)
    y1 = np.random.uniform(y[i]-1, y[i]+1, size=10)
    plt.plot(x1, y1, color=color[i], linestyle='none', marker = 'o', markersize=3)
    average_x, average_y = sum(x1)/10, sum(y1)/10  # среднее значение
    plt.plot(average_x, average_y, color='black', marker='o', markersize=5)  # Средня точка
    max = 0
    for k in range(10):
        for n in range(10):
            if (x1[k]**2 + y1[n]**2)**0.5 > max:
                max = (x1[k]**2 + y1[k]**2)**0.5
    print('максимальное удаление от average', label[i],'=', max)
plt.xlim(-11, 11)
plt.ylim(-11, 11)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()
