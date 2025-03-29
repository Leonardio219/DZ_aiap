import matplotlib.pyplot as plt

# Пример данных: точки (x, y)
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Создание графика
plt.plot(x, y, marker='o')  # marker='o' для отображения точек
plt.title('График собора в Гос Думе')  # Заголовок графика
plt.xlabel('Ось X')  # Подпись оси X
plt.ylabel('Ось Y')  # Подпись оси Y
plt.grid(True)  # Включение сетки
plt.show()  # Отображение графика