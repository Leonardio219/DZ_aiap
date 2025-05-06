from PyQt5 import QtWidgets
import numpy as np
import sys
from zadanie5 import Ui_MainWindow
import matplotlib.pyplot as plt

class plot(QtWidgets.QMainWindow):
    def __init__(self):
        super(plot, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        try:
            T = float(self.ui.T.text())
            n = float(self.ui.n.text())

            if self.ui.combo.currentText() == "Па":
                V_list = np.linspace(0.01, (n * T) / 100000000 * 8, 1000)
                P = n * 8.31 * T / V_list
            else:
                V_list = np.linspace(0.01, (n * T) / 10 * 8, 1000)
                P = n * 8.31 * T / (V_list * 100000)

            plt.figure()
            plt.plot(V_list, P)
            plt.xlabel("м2")
            plt.ylabel(self.ui.combo.currentText())
            plt.grid(True)
            plt.tight_layout()
            plt.show(block=False)

        except ValueError as s:
            QtWidgets.QMessageBox.critical(self, "Неверный формат данных в строке", str(s))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = plot()
    window.show()
    sys.exit(app.exec())