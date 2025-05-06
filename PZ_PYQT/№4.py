from PyQt5 import QtWidgets
import numpy as np
import sys
from zadanie4 import Ui_MainWindow
import matplotlib.pyplot as plt

class interplot(QtWidgets.QMainWindow):
    def __init__(self):
        super(interplot, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked (self):
        try:
            amp_1 = float(self.ui.amp_1.text())
            fre_1 = float(self.ui.fre_1.text())
            pha_1 = np.radians(float(self.ui.pha_1.text()))
            amp_2 = float(self.ui.amp_2.text())
            fre_2 = float(self.ui.fre_2.text())
            pha_2 = np.radians(float(self.ui.pha_2.text()))

            a = max(fre_2, fre_1)
            time_points = np.linspace(0, 10/a, 500)
            y1 = amp_1 * (np.sin(2 * np.pi * fre_1 * time_points) + pha_1)
            y2 = amp_2 * (np.sin(2 * np.pi * fre_2 * time_points) + pha_2)
            yint = y1 + y2

            plt.figure()
            plt.plot(time_points, y1, label = 'Волна 1')
            plt.plot(time_points, y2, label = 'Волна 2')
            plt.plot(time_points, yint, label = 'Интерфернеция', linewidth = 3)
            plt.xlabel("time")
            plt.ylabel("amplitude")

            plt.title("graphik inteferience")
            plt.grid(True)
            plt.tight_layout()
            plt.legend()
            plt.show(block=False)

        except ValueError as s:
            QtWidgets.QMessageBox.critical(self, "Неверный формат данных в строке", str(s))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = interplot()
    window.show()
    sys.exit(app.exec())