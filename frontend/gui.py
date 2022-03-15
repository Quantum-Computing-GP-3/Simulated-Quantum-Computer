from PyQt5 import QtWidgets, uic
import sys

class GUI(QtWidgets.QWidget):
    def __init__(self):
        super(GUI, self).__init__()
        uic.loadUi('resource/mainpage.ui', self)
        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = GUI()
    app.exec_()

if __name__ == '__main__':
    main()