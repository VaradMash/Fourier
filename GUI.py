from PyQt5 import QtWidgets,uic

app = QtWidgets.QApplication([])
dlc = uic.loadUi('load.ui')

dlc.show()
app.exec()
