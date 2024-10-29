from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Central widget styling
        self.centralwidget.setStyleSheet("background-color: #f5f5f5;")
        
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 151, 31))
        self.label.setFont(QtGui.QFont("Arial", 24,))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 100, 21))
        self.label_2.setFont(QtGui.QFont("Arial", 12))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 100, 21))
        self.label_3.setFont(QtGui.QFont("Arial", 12))
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 100, 21))
        self.label_4.setFont(QtGui.QFont("Arial", 12))
        self.label_4.setObjectName("label_4")
        
        self.text_adSoyad = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.text_adSoyad.setGeometry(QtCore.QRect(130, 50, 250, 30))
        self.text_adSoyad.setObjectName("text_adSoyad")
        self.text_adSoyad.setStyleSheet("border: 1px solid #ddd; border-radius: 5px; padding: 5px;")
        
        self.text_telefonNo = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.text_telefonNo.setGeometry(QtCore.QRect(130, 80, 250, 30))
        self.text_telefonNo.setObjectName("text_telefonNo")
        self.text_telefonNo.setStyleSheet("border: 1px solid #ddd; border-radius: 5px; padding: 5px;")
        
        self.text_eposta = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.text_eposta.setGeometry(QtCore.QRect(130, 110, 250, 30))
        self.text_eposta.setObjectName("text_eposta")
        self.text_eposta.setStyleSheet("border: 1px solid #ddd; border-radius: 5px; padding: 5px;")
        
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 200, 150, 31))
        self.label_5.setFont(QtGui.QFont("Arial", 24, ))
        self.label_5.setObjectName("label_5")
        
        self.tablo_liste = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tablo_liste.setGeometry(QtCore.QRect(20, 240, 760, 300))
        self.tablo_liste.setObjectName("tablo_liste")
        self.tablo_liste.setColumnCount(4)
        self.tablo_liste.setHorizontalHeaderLabels(["No", "Ad Soyad", "Telefon", "E-posta"])
        self.tablo_liste.setStyleSheet("QHeaderView::section { background-color: #f0f0f0; font-size: 12pt; }"
                                       "QTableWidget { border: 1px solid #ddd; border-radius: 5px; }"
                                       "QTableWidget::item { padding: 5px; }")
        
        self.btn_kaydet = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_kaydet.setGeometry(QtCore.QRect(200, 550, 100, 40))
        self.btn_kaydet.setObjectName("btn_kaydet")
        self.btn_kaydet.setStyleSheet("background-color: #4CAF50; color: white; border: none; border-radius: 5px;")
        
        self.btn_temizle = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_temizle.setGeometry(QtCore.QRect(320, 550, 100, 40))
        self.btn_temizle.setObjectName("btn_temizle")
        self.btn_temizle.setStyleSheet("background-color: #2196F3; color: white; border: none; border-radius: 5px;")
        
        self.btn_cikis = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_cikis.setGeometry(QtCore.QRect(440, 550, 100, 40))
        self.btn_cikis.setObjectName("btn_cikis")
        self.btn_cikis.setStyleSheet("background-color: #f44336; color: white; border: none; border-radius: 5px;")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuDosya = QtWidgets.QMenu(parent=self.menubar)
        self.menuDosya.setObjectName("menuDosya")
        self.menuKapat = QtWidgets.QMenu(parent=self.menuDosya)
        self.menuKapat.setObjectName("menuKapat")
        self.menuD_ZEN = QtWidgets.QMenu(parent=self.menubar)
        self.menuD_ZEN.setObjectName("menuD_ZEN")
        self.menuG_r_nt_le = QtWidgets.QMenu(parent=self.menubar)
        self.menuG_r_nt_le.setObjectName("menuG_r_nt_le")
        self.menuYard_m = QtWidgets.QMenu(parent=self.menubar)
        self.menuYard_m.setObjectName("menuYard_m")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionYeni = QtGui.QAction(parent=MainWindow)
        self.actionYeni.setObjectName("actionYeni")
        self.actionSil = QtGui.QAction(parent=MainWindow)
        self.actionSil.setObjectName("actionSil")
        self.actionT_m_n_Kapat = QtGui.QAction(parent=MainWindow)
        self.actionT_m_n_Kapat.setObjectName("actionT_m_n_Kapat")
        
        self.menuKapat.addAction(self.actionT_m_n_Kapat)
        self.menuDosya.addAction(self.actionYeni)
        self.menuDosya.addAction(self.actionSil)
        self.menuDosya.addAction(self.menuKapat.menuAction())
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menuD_ZEN.menuAction())
        self.menubar.addAction(self.menuG_r_nt_le.menuAction())
        self.menubar.addAction(self.menuYard_m.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Telefon Rehberi"))
        self.label.setText(_translate("MainWindow", "KAYIT"))
        self.label_2.setText(_translate("MainWindow", "Ad ve Soyad :"))
        self.label_3.setText(_translate("MainWindow", "Telefon No :"))
        self.label_4.setText(_translate("MainWindow", "E-posta :"))
        self.label_5.setText(_translate("MainWindow", "LİSTE"))
        self.btn_kaydet.setText(_translate("MainWindow", "KAYDET"))
        self.btn_temizle.setText(_translate("MainWindow", "LİSTELE"))
        self.btn_cikis.setText(_translate("MainWindow", "ÇIKIŞ"))
        self.menuDosya.setTitle(_translate("MainWindow", "Dosya"))
        self.menuKapat.setTitle(_translate("MainWindow", "Kapat"))
        self.menuD_ZEN.setTitle(_translate("MainWindow", "Düzen"))
        self.menuG_r_nt_le.setTitle(_translate("MainWindow", "Görüntüle"))
        self.menuYard_m.setTitle(_translate("MainWindow", "Yardım"))
        self.actionYeni.setText(_translate("MainWindow", "Yeni"))
        self.actionSil.setText(_translate("MainWindow", "Sil"))
        self.actionT_m_n_Kapat.setText(_translate("MainWindow", "Tümünü Kapat"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
