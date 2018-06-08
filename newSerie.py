# -*- coding: utf-8 -*-

from functools import partial
from PyQt5.QtWidgets import (QDialog, QDialogButtonBox, QHBoxLayout, QGroupBox, QCheckBox, QVBoxLayout, QLabel, QFrame)
from PyQt5.QtCore import (Qt, QRect)

class NewSerie_dlg(QDialog):
    
    def __init__(self, availableSections):
        super().__init__()
        if not(type(availableSections) is dict):
            raise TypeError('Sections should be a dictionnary !!')
        self.availableSections = availableSections
        
        self.setWindowTitle("Création d'une nouvelle série")
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(300, 200)

        self.main_vb =  QVBoxLayout(self)
        
        self.main_hb = QHBoxLayout(self)
        self.main_vb.addLayout(self.main_hb)

        self.left_vb = QVBoxLayout(self)
        self.main_hb.addLayout(self.left_vb)

        self.sections_gb = QGroupBox(self)
        self.left_vb.addWidget(self.sections_gb)
        self.sections_vb = QVBoxLayout(self.sections_gb)
        self.sections_gb.setTitle("Sections")
        self.checkBox = {}
        for s in availableSections.keys():
            self.checkBox[s] = QCheckBox(self)
            self.checkBox[s].setText(s)
            self.checkBox[s].stateChanged.connect(partial(self.updateSections, s))
            self.sections_vb.addWidget(self.checkBox[s])
        self.sections_vb.addStretch()
        
        self.nbStudent_lb = QLabel(self)
        self.nbStudent_lb.setFrameShape(QFrame.StyledPanel)
        self.nbStudent_lb.setText('0')
        self.left_vb.addWidget(self.nbStudent_lb)

        self.buttonBox = QDialogButtonBox(self)
        self.main_vb.addWidget(self.buttonBox)
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        
    def updateSections(self, sections, state):
        nbStudent = 0
        for s in self.availableSections:
            if self.checkBox[s].checkState() == Qt.Checked:
                nbStudent += self.availableSections[s]
        self.nbStudent_lb.setText(str(nbStudent))

    def showDlg(self):
        if (self.exec_()):
            print('OK pressed')
        else:
            print('Cancel pressed')


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton)
            
    def window():
        app = QApplication(sys.argv)
        w = QWidget()
        availableSections = {'EIT': 21, 'EM1':18, 'EM2': 12}
        newSerie = NewSerie_dlg(availableSections)
        btn = QPushButton('Dialog', w)
        btn.move(50,50)
        btn.clicked.connect(newSerie.showDlg)
        w.setWindowTitle('test newSerieDlg')
        w.show()
        sys.exit(app.exec_())
    

    window()
