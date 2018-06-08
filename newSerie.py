# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import (QDialog)
from PyQt5.QtCore import Qt

class NewSerie_dlg(QDialog):
    
    def __init__(self):
        super().__init__()
        self.ok_btn = QPushButton("OK", self)
        self.ok_btn.move(50,50)
        self.setWindowTitle("test dialog")
        self.setWindowModality(Qt.ApplicationModal)

    def showDlg(self):
        self.exec_()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton)
            
    def window():
        app = QApplication(sys.argv)
        w = QWidget()
        newSerie = NewSerie_dlg()
        btn = QPushButton('Dialog', w)
        btn.move(50,50)
        btn.clicked.connect(newSerie.showDlg)
        w.setWindowTitle('test newSerieDlg')
        w.show()
        sys.exit(app.exec_())
    

    window()
