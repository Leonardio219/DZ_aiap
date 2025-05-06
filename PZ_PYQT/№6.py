from PyQt5 import QtWidgets
import numpy as np
import sys
from zadanie6 import Ui_MainWindow
import matplotlib.pyplot as plt

class plot(QtWidgets.QMainWindow):
    def __init__(self):
        super(plot, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        try:
            A = (float(self.ui.amp.text()))
            fre = float(self.ui.fre.text())
            k = float(self.ui.k.text())

            time_points = np.linspace(0, 5/fre, 500)
            y = np.radians(A) * np.exp(-k * time_points) * np.sin(2 * np.pi * fre * time_points)

            plt.figure()
            plt.plot(time_points, y)
            plt.xlabel("Время, c")
            plt.ylabel("Отклонение")
            plt.grid(True)
            plt.tight_layout()
            plt.show(block=False)

        except ValueError as s:
            QtWidgets.QMessageBox.critical(self, "Некорректные данные в строке", str(s))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = plot()
    window.show()
    sys.exit(app.exec())