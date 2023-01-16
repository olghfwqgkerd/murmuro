from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
import sys
import os

from MEG import *

def resourcePath(relative_path):
    # Get absolute path to resource, works for dev and for PyInstaller
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Ui_MainWindow(object):
    PRIVATE_KEY = None
    PUBLIC_KEY = None
    HASH = None
    SIGNATURE = None
    MESSAGE = None
    B_MESSAGE = None
    
    def setupUi(self, MainWindow):
        app_icon = QtGui.QIcon()
        app_icon.addFile(resourcePath("sprites/16.png"), QtCore.QSize(16,16))
        # app_icon.addFile(resourcePath('32.png'), QtCore.QSize(24,24))
        app_icon.addFile(resourcePath("sprites/32.png"), QtCore.QSize(32,32))
        #app_icon.addFile(resourcePath(resourcePath("sprites/icon.png")), QtCore.QSize(48,48))
        # app_icon.addFile(resourcePath('32.png'), QtCore.QSize(256,256))
        MainWindow.setWindowIcon(app_icon)
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(585, 532)
        self.tabManager = QtWidgets.QTabWidget(MainWindow)
        self.tabManager.setGeometry(QtCore.QRect(10, 10, 561, 501))
        self.tabManager.setObjectName("tabManager")
        self.tab_messages = QtWidgets.QWidget()
        self.tab_messages.setObjectName("tab_messages")
        self.logoImage = QtWidgets.QLabel(self.tab_messages)
        self.logoImage.setGeometry(QtCore.QRect(330, 10, 201, 91))
        self.logoImage.setText("")
        self.logoImage.setPixmap(QtGui.QPixmap(resourcePath("sprites/icon_2.png")))
        self.logoImage.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.logoImage.setObjectName("logoImage")
        self.notImg = QtWidgets.QLabel(self.tab_messages)
        self.notImg.setGeometry(QtCore.QRect(130, 430, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.notImg.setFont(font)
        self.notImg.setText("")
        self.notImg.setTextFormat(QtCore.Qt.PlainText)
        self.notImg.setPixmap(QtGui.QPixmap(resourcePath("sprites/not.png")))
        self.notImg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.notImg.setObjectName("notImg")
        self.importKeyBtn = QtWidgets.QPushButton(self.tab_messages)
        self.importKeyBtn.setGeometry(QtCore.QRect(140, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.importKeyBtn.setFont(font)
        self.importKeyBtn.setObjectName("importKeyBtn")
        self.importMsgBtn = QtWidgets.QPushButton(self.tab_messages)
        self.importMsgBtn.setGeometry(QtCore.QRect(140, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.importMsgBtn.setFont(font)
        self.importMsgBtn.setObjectName("importMsgBtn")
        self.verifyBtn = QtWidgets.QPushButton(self.tab_messages)
        self.verifyBtn.setGeometry(QtCore.QRect(20, 430, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.verifyBtn.setFont(font)
        self.verifyBtn.setObjectName("verifyBtn")
        self.exportKeyBtn = QtWidgets.QPushButton(self.tab_messages)
        self.exportKeyBtn.setGeometry(QtCore.QRect(20, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.exportKeyBtn.setFont(font)
        self.exportKeyBtn.setObjectName("exportKeyBtn")
        self.exportMsgBtn = QtWidgets.QPushButton(self.tab_messages)
        self.exportMsgBtn.setGeometry(QtCore.QRect(20, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.exportMsgBtn.setFont(font)
        self.exportMsgBtn.setObjectName("exportMsgBtn")
        self.msgInput = QtWidgets.QPlainTextEdit(self.tab_messages)
        self.msgInput.setGeometry(QtCore.QRect(20, 170, 511, 251))
        self.msgInput.setObjectName("msgInput")
        self.label = QtWidgets.QLabel(self.tab_messages)
        self.label.setGeometry(QtCore.QRect(130, 20, 31, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.logInput = QtWidgets.QLineEdit(self.tab_messages)
        self.logInput.setEnabled(False)
        self.logInput.setGeometry(QtCore.QRect(20, 120, 511, 20))
        self.logInput.setObjectName("logInput")
        self.logText = QtWidgets.QLabel(self.tab_messages)
        self.logText.setGeometry(QtCore.QRect(30, 100, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.logText.setFont(font)
        self.logText.setObjectName("logText")
        self.msgInput_2 = QtWidgets.QLabel(self.tab_messages)
        self.msgInput_2.setGeometry(QtCore.QRect(30, 150, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.msgInput_2.setFont(font)
        self.msgInput_2.setObjectName("msgInput_2")
        self.posImg = QtWidgets.QLabel(self.tab_messages)
        self.posImg.setGeometry(QtCore.QRect(130, 430, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.posImg.setFont(font)
        self.posImg.setText("")
        self.posImg.setTextFormat(QtCore.Qt.PlainText)
        self.posImg.setPixmap(QtGui.QPixmap(resourcePath("sprites/pos.png")))
        self.posImg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.posImg.setObjectName("posImg")
        self.negImg = QtWidgets.QLabel(self.tab_messages)
        self.negImg.setGeometry(QtCore.QRect(130, 430, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.negImg.setFont(font)
        self.negImg.setText("")
        self.negImg.setTextFormat(QtCore.Qt.PlainText)
        self.negImg.setPixmap(QtGui.QPixmap(resourcePath("sprites/neg.png")))
        self.negImg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.negImg.setObjectName("negImg")
        self.logoImage.raise_()
        self.importKeyBtn.raise_()
        self.importMsgBtn.raise_()
        self.verifyBtn.raise_()
        self.exportKeyBtn.raise_()
        self.exportMsgBtn.raise_()
        self.msgInput.raise_()
        self.label.raise_()
        self.logInput.raise_()
        self.logText.raise_()
        self.msgInput_2.raise_()
        self.posImg.raise_()
        self.negImg.raise_()
        self.notImg.raise_()
        self.tabManager.addTab(self.tab_messages, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.createSignBtn = QtWidgets.QPushButton(self.tab)
        self.createSignBtn.setGeometry(QtCore.QRect(20, 100, 221, 31))
        self.createSignBtn.setObjectName("createSignBtn")
        self.createHashBtn = QtWidgets.QPushButton(self.tab)
        self.createHashBtn.setGeometry(QtCore.QRect(20, 60, 221, 31))
        self.createHashBtn.setObjectName("createHashBtn")
        self.generateKeysBtn = QtWidgets.QPushButton(self.tab)
        self.generateKeysBtn.setGeometry(QtCore.QRect(20, 20, 221, 31))
        self.generateKeysBtn.setObjectName("generateKeysBtn")
        self.tabManager.addTab(self.tab, "")
        self.signatureText = QtWidgets.QLabel(MainWindow)
        self.signatureText.setGeometry(QtCore.QRect(10, 510, 561, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.signatureText.setFont(font)
        self.signatureText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.signatureText.setObjectName("signatureText")

        self.exportMsgBtn.clicked.connect(self.exportMsg)
        self.exportKeyBtn.clicked.connect(self.exportKey)
        self.importMsgBtn.clicked.connect(self.importMsg)
        self.importKeyBtn.clicked.connect(self.importKey)
        self.verifyBtn.clicked.connect(self.verify)
        self.generateKeysBtn.clicked.connect(self.generateKey)
        self.createHashBtn.clicked.connect(self.createHas)
        self.createSignBtn.clicked.connect(self.createSign)
        
        self.retranslateUi(MainWindow)
        self.tabManager.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.generateKey()
        self.alert(2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Murmuro BETA"))
        self.importKeyBtn.setText(_translate("MainWindow", "Import public key"))
        self.importMsgBtn.setText(_translate("MainWindow", "Import message"))
        self.verifyBtn.setText(_translate("MainWindow", "Verify"))
        self.exportKeyBtn.setText(_translate("MainWindow", "Export public key"))
        self.exportMsgBtn.setText(_translate("MainWindow", "Export message"))
        self.logText.setText(_translate("MainWindow", "Logs:"))
        self.msgInput_2.setText(_translate("MainWindow", "Message:"))
        self.tabManager.setTabText(self.tabManager.indexOf(self.tab_messages), _translate("MainWindow", "Messages"))
        self.createSignBtn.setText(_translate("MainWindow", "Create signature"))
        self.createHashBtn.setText(_translate("MainWindow", "Create hash"))
        self.generateKeysBtn.setText(_translate("MainWindow", "Generate keys"))
        self.tabManager.setTabText(self.tabManager.indexOf(self.tab), _translate("MainWindow", "Geeks"))
        self.signatureText.setText(_translate("MainWindow", "Olgierd Rogowicz - 2022 - ro"))
            
#---------------BASIC--------------------------------------
    def exportMsg(self):
        name , check = QFileDialog.getSaveFileName(None, "Export message",
                                               "", "Text Files (*.txt)")
        if check:
            file = open(name,'w')
            file.write(self.msgInput.toPlainText())
            file.close()
            self.createHas()
            self.createSign()
            self.exporSig(name)
            self.logInput.setText("--->Export message [DONE]")
            
    def exporSig(self, name):  
        name = (str(name[:-4] + "_signature"))
        file = open(name, 'wb')
        file.write(self.SIGNATURE)
        file.close()
        self.logInput.setText("--->Export signature [DONE]")
        
    def exportKey(self):
        name , check = QFileDialog.getSaveFileName(None, "Export public key",
                                               "", "Text Files (*.txt)")
        if check:
            file = open(name,'wb')
            file.write(self.PUBLIC_KEY.exportKey('PEM'))
            file.close()
            self.logInput.setText("--->Export key [DONE]")
        
    def importMsg(self):
        name , check = QFileDialog.getOpenFileName(None, "Import message",
                                               "", "Text Files (*.txt)")
        if check:
            file = open(name,'r')
            self.msgInput.setPlainText(file.read())
            file.close()
            self.createHas()
            if self.importSig(name):
                self.alert(2)
                self.logInput.setText("<---Import message [DONE]")
            
    def importSig(self, name):
        name = (str(name[:-4] + "_signature"))
        file = open(name, 'rb')
        try:
            self.SIGNATURE = file.read()
            file.close()
            self.logInput.setText("<---Import signature [DONE]")
            return True
        except:
            file.close()
            self.logInput.setText("<---Signature corrupted [ERROR]")
            return False
        
    def importKey(self):
        name , check = QFileDialog.getOpenFileName(None, "Export public key",
                                               "", "Text Files (*.txt)")
        if check:
            file = open(name,'rb')
            try:
                self.PUBLIC_KEY = RSA.importKey(file.read())
                file.close()
                self.alert(2)
                self.logInput.setText("<---Import key [DONE]")
            except:
                file.close()
                self.logInput.setText("<---Key corrupted [ERROR]")
        
    def verify(self):
        verifier = PKCS115_SigScheme(self.PUBLIC_KEY)        
        try:
            verifier.verify(self.HASH, self.SIGNATURE)
            self.alert(1)
            self.logInput.setText("----Verify [DONE]")
        except:
            self.alert(0)
            self.logInput.setText("----Verify [DONE]")
        
    def generateKey(self):
        random_gen = MadEyeGenerator().getNumbers
        try:
            self.PRIVATE_KEY = RSA.generate(2048, random_gen)
            self.PUBLIC_KEY = self.PRIVATE_KEY.publickey()
            self.logInput.setText("----Generate keys [DONE]")
        except:
            self.logInput.setText("----Problem with taking frame [DONE]")
        
    def createHas(self):
        self.B_MESSAGE = bytes(self.msgInput.toPlainText(), 'utf-8')
        self.HASH = SHA256.new(self.B_MESSAGE)
        self.logInput.setText("----Create hash [DONE]")
        
    def createSign(self):
        signer = PKCS115_SigScheme(self.PRIVATE_KEY)
        self.SIGNATURE = signer.sign(self.HASH)
        self.logInput.setText("----Create signature [DONE]")
        
    def alert(self, mode):
        match(mode):
            case 0:
                self.negImg.setHidden(False)
                self.posImg.setHidden(True)
                self.notImg.setHidden(True)
            case 1:
                self.negImg.setHidden(True)
                self.posImg.setHidden(False)
                self.notImg.setHidden(True)
            case 2:
                self.negImg.setHidden(True)
                self.posImg.setHidden(True)
                self.notImg.setHidden(False)

def initiation():
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    app.exec_()
    
initiation()
