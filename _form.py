from PyQt6.QtWidgets import *
from form import Ui_MainWindow
import sys
#veritabanı için önemli kütüphaneler
import os
import sqlite3

class FormWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.anaForm = Ui_MainWindow()
        self.anaForm.setupUi(self)
        
        
        self.adSoyad = self.anaForm.text_adSoyad
        self.telefon = self.anaForm.text_telefonNo
        self.eposta = self.anaForm.text_eposta
        self.liste = self.anaForm.tablo_liste
        
        
        self.anaForm.btn_kaydet.clicked.connect(self.kaydet)
        self.anaForm.btn_temizle.clicked.connect(self.listele)
        self.anaForm.btn_cikis.clicked.connect(self.cikis)

    def baglan(self): 
        sqlFile = os.path.join(os.path.dirname(__file__),"TelefonRehberi.db")
        with sqlite3.connect(sqlFile) as baglanti:
            return baglanti
     
    def kaydet(self):
            try:
                from random import randint
                kayitNo=str(randint(1111,9999))
                baglanti = self.baglan()
                sorgu = baglanti.cursor()
                sorgu.execute(f"insert into icerik values('{kayitNo}','{self.adSoyad.text()}','{self.telefon.text()}','{self.eposta.text()}')")
                baglanti.commit()
                self.temizle()
                self.liste.setFocus()
                QMessageBox.information(self,"Bildirim","Kayıt Başarılı")
            
            except Exception as hata:
                QMessageBox.critical(self, "Hata", f"Hata Oluştu:\n{hata}")

    
    def listele(self):
        # baslıkları ekledim
        try:
            self.liste.clear()
            sutunlar=["No","Ad Soyad","Telefon","E-pota"]
            self.liste.setColumnCount(len(sutunlar))
            self.liste.setHorizontalHeaderLabels(sutunlar)
            baglanti = self.baglan()
            sorgu = baglanti.cursor()
            sorgu.execute("select*from icerik")
            kayitlar = sorgu.fetchall()
            if kayitlar:
                self.liste.setRowCount(len(kayitlar))
                kayitSay = 0
                for kayit in kayitlar:
                    for i in range(len(sutunlar)):
                        self.liste.setItem(kayitSay,i,QTableWidgetItem(str(kayit[i])))
                    kayitSay +=1
            else:
                QMessageBox.warning(self,"Uyarı","Kayıt Bulunamadı")            
        except Exception as hata:
             QMessageBox.critical(self, "Hata", f"Hata Oluştu:\n{hata}")

    
        
    def temizle(self):
            self.adSoyad.clear()
            self.telefon.clear()
            self.eposta.clear()
            


        
    def cikis(self):
            sys.exit()
        
        