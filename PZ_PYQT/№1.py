import numpy as np
from PyQt5 import QtWidgets
from zadanie1 import Ui_MainWindow
import sys
import matplotlib.pyplot as plt
g = 9.81

class plot(QtWidgets.QMainWindow):
    def __init__(self):
        super(plot, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pb.clicked.connect(self.btnClicked)

    def btnClicked(self):
        try:
            speed = float(self.ui.speed.text())
            ugol = float(self.ui.ugol.text())
            ugol_rad = np.radians(ugol)
            time = 2 * speed * np.sin(ugol_rad) / g
            time_point = np.linspace(0, time, 200)
            x = speed * np.cos(ugol_rad) * time_point
            y = speed * np.sin(ugol_rad) * time_point - 0.5 * g * time_point**2
            plt.figure()
            plt.plot(x, y)
            plt.axis('equal')
            plt.xlabel('Расстояние в м')
            plt.ylabel('Высота в м')
            plt.axhline(0, color='black')
            plt.show()
        except ValueError:
            None

app = QtWidgets.QApplication([])
window = plot()
window.show()
sys.exit(app.exec())