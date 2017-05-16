#Fernando Madrigal
#Juan Zuniga
#Steven Walton
#CST 205 Group 253
#5-16-2017

#https://github.com/stwalton/CST205proj3

#Import PyQt Items
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import*


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
import os

warnings.filterwarnings("ignore")

#The lowercase dejavu is the main py file in the folder, the import is everything from the folder
from dejavu import Dejavu
from dejavu import Dejavu

#Access SQL Database
config = {
        "database": {
                "host": "127.0.0.1:3306",
                "user": "STEVEN",
                "passwd": "1234",
                "db": "TESTDB",
                }
        }

#Dejavu reconize items, left this in just in case. ALso got it recalled in the function
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

# create a Dejavu instance
djv = Dejavu(config)

#Main Gui
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.song = "" #Global Variable that was set. Didn't need to leave it here, but left it for testing reasons
        #Also this variable is a string and is used to output if a song was found
        
        #Initializing of the main window
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 620) 
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        #Picture is the QGraphicsView name that was used for putting in the background picture
        self.Picture = QtGui.QGraphicsView(self.centralwidget)
        self.Picture.setObjectName(_fromUtf8("Picture"))
        self.verticalLayout.addWidget(self.Picture)
        #The next two lines of code was the only way we figured out how to get the image used
        self.Picture.setAutoFillBackground(True)
        self.Picture.setStyleSheet("background-image: url(music.jpg); background-attachment: fixed")

        #All of this is for initializing and setting the paramaters for the button
        #FP is for fingerprinting
        #Mic is the Microphone Recognize
        #File is for file recognizing
        self.FP = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FP.setFont(font)
        self.FP.setObjectName(_fromUtf8("FP"))
        self.verticalLayout.addWidget(self.FP)
        self.File = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.File.setFont(font)
        self.File.setObjectName(_fromUtf8("File"))
        self.verticalLayout.addWidget(self.File)
        self.Mic = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Mic.setFont(font)
        self.Mic.setObjectName(_fromUtf8("Mic"))
        self.verticalLayout.addWidget(self.Mic)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Destiny", None)) #Set name on top of application. Can change name of program here
        self.FP.setText(_translate("MainWindow", "Finger Print Song", None)) #FP button
        self.File.setText(_translate("MainWindow", "Search For Song Through File", None)) #File button
        self.Mic.setText(_translate("MainWindow", "Search For Song Through Microphone", None)) #Mic button
        self.FP.clicked.connect(self.Fingerprint) #Set FP button to a function once the button is clicked
        self.Mic.clicked.connect(self.mic_recognizing) #Set Mic button to a function once the button is clicked
        self.File.clicked.connect(self.file_recognizing) #Set File to a function once the button is clicked

    #Function for the Fingerprint button
    def Fingerprint(self):
        #The next three lines are needed to successfully open a file explorer window, and take in the file destination
        filePath = QFileDialog.Options()
        filePath |= QFileDialog.DontUseNativeDialog
        filepath = QFileDialog.getOpenFileName(QMainWindow(),"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options = filePath)
        #The replace call is to replace the back slashes that windows uses for file destination to forward slash to be able to read where the file is at in python
        #Might need to comment this line out if running on a non windows machine
        filepath.replace('\\', '/')
        #Call for the fingerprint module in Dejavu. The str is needed to convert Qstring to a regular string for Dejavu to recongnize the file location
        djv.fingerprint_file(str(filepath), [".mp3"])

    #Function for Mic
    def mic_recognizing(self):
        #The same import as before, kept it in for testing reasons
        from dejavu.recognize import MicrophoneRecognizer
        #Give variable song the name of song that is being recognized. Also the call for Dejavu module. You can change how many seconds it listens here
        self.song = djv.recognize(MicrophoneRecognizer, seconds=15)
        print (self.song)
        

    #Function for file     
    def file_recognizing(self):
        #The four lines are same in the Fingerprint fucntion
        filePath = QFileDialog.Options()
        filePath |= QFileDialog.DontUseNativeDialog
        filepath = QFileDialog.getOpenFileName(QMainWindow(),"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options = filePath)
        filepath.replace('\\', '/')
        #Left import for testing reasons
        from dejavu.recognize import FileRecognizer
        #Song variable get name from calling the dejavu module
        self.song = djv.recognize(FileRecognizer, str(filepath))
        print (self.song)
        



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

