# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

import warnings
import json
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu import Dejavu
config = {
        "database": {
                "host": "127.0.0.1:3306",
                "user": "STEVEN",
                "passwd": "1234",
                "db": "TESTDB",
                }
        }

from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

# create a Dejavu instance
djv = Dejavu(config)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        #Variables the I created
        self.song = ""
        
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(300, 164)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.FP = QtGui.QPushButton(self.centralwidget)
        self.FP.setGeometry(QtCore.QRect(10, 90, 75, 23))
        self.FP.setObjectName(_fromUtf8("FP"))
        
        self.Mic = QtGui.QPushButton(self.centralwidget)
        self.Mic.setGeometry(QtCore.QRect(90, 90, 91, 23))
        self.Mic.setObjectName(_fromUtf8("Mic"))

        self.File = QtGui.QPushButton(self.centralwidget)
        self.File.setGeometry(QtCore.QRect(190, 90, 91, 23))
        self.File.setObjectName(_fromUtf8("File"))
        
        self.Text_Output = QtGui.QLabel(self.centralwidget)
        self.Text_Output.setGeometry(QtCore.QRect(20, 10, 251, 61))
        self.Text_Output.setText(_fromUtf8(""))
        self.Text_Output.setObjectName(_fromUtf8("Text_Output"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.FP.setText(_translate("MainWindow", "Finger Print", None))
        self.Mic.setText(_translate("MainWindow", "Recognize Mic", None))
        self.File.setText(_translate("MainWindow", "Recongize File", None))
        self.FP.clicked.connect(self.Fingerprint) #Button For Fingerprint
        #self.Mic.clicked.connect(self.Mic) #Button For Mic
        #self.File.clicked.connect(self.File) #Button for File

    def Fingerprint(self):
        djv.fingerprint_directory("mp3", [".mp3"])

    def Mic(self):
        self.song = djv.recognize(MicrophoneRecognizer, seconds=10)

    def File(self):
        print ("This Works")
         

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

