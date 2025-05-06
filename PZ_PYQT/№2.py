from PyQt5 import QtWidgets
import numpy as np
import sys
from zadanie2 import Ui_MainWindow
import matplotlib.pyplot as plt

class plot(QtWidgets.QMainWindow):
    def __init__(self):
        super(plot, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked (self):
        try:
            amplitude = float(self.ui.line_amp.text())
            frequency = float(self.ui.Line_chas.text())
            phaza = float(self.ui.Line_faz.text())
            phaza_rad = np.radians(phaza)

            period = 1/frequency
            time_points = np.linspace(0, 5*period, 550)
            y = amplitude * np.sin(2 * np.pi * frequency * time_points + phaza_rad)

            plt.figure(figsize=(10, 5))
            plt.plot(time_points, y)
            plt.title("График колебаний")
            plt.xlabel("Время, с")
            plt.ylabel("Амплитуда")
            plt.grid(True)
            plt.tight_layout()
            plt.show(block = False)

        except ValueError as s:
            QtWidgets.QMessageBox.critical(self, "Ошибка", f"некоректные данные {str(s)}")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = plot()
    window.show()
    sys.exit(app.exec())