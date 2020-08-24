import sys
from PyQt5.QtWidgets import QDialog, QApplication
from aa import Ui_Form      

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.pushButton_Click)
        self.show()

    def pushButton_Click(self):
        self.ui.label.setText("Hello World")

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())