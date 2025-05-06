from PyQt5 import QtWidgets
import numpy as np
import sys
from zadanie3 import Ui_MainWindow
import matplotlib.pyplot as plt

class Tempplot(QtWidgets.QMainWindow):
    def __init__(self):
        super(Tempplot, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked (self):
        try:
            Tenv = float(self.ui.line_Tenv.text())
            T0 = float(self.ui.line_T.text())
            k = float(self.ui.line_k.text())
            t = Tenv / (k * (T0 - Tenv))
            time_points = np.linspace(0, 100, 500)
            y = Tenv + (T0 - Tenv) * np.exp(-k * time_points)

            plt.figure()
            plt.plot(time_points, y)
            plt.xlabel("time, c")
            plt.ylabel("T, K")
            plt.title("graphik")
            plt.grid(True)
            plt.tight_layout()
            plt.show(block=False)

        except ValueError as s:
            QtWidgets.QMessageBox.critical(self, "Невенрый формат ввода в строке", str(s))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Tempplot()
    window.show()
    sys.exit(app.exec())