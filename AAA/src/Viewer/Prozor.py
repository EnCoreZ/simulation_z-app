from PySide.QtGui import QWidget, QPushButton, QFormLayout, QTextEdit
from PySide.QtCore import Qt, SIGNAL, SLOT


class Prozor(QWidget):
    def __init__(self,element):
        #kreiramo prozor
        QWidget.__init__(self)
        self.element = element
        #iskljucujemo polja za uvecanje i minimizaciju
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint & ~Qt.WindowMinimizeButtonHint)
        #Podesavamo naslov
        self.setWindowTitle(self.element.ime)
        self.focusWidget()
        #editor teksta
        self.textEditor = QTextEdit()
        #dodajemo dugmad za primenu i odbacivanje promena
        #i povezujemo ih sa odgovarajucim funkcijama
        self.dugmeOk = QPushButton("Potvrdi")
        self.dugmeOtkazi = QPushButton("Otkazi")
        self.connect(self.dugmeOk,SIGNAL('clicked()'),self,SLOT('podesi()'))
        self.connect(self.dugmeOtkazi,SIGNAL('clicked()'),self,SLOT('zatvori()'))
        #formiramo raspored
        raspored = QFormLayout()
        raspored.addRow(self.textEditor)
        raspored.addRow(self.dugmeOtkazi,self.dugmeOk)
        self.setLayout(raspored)
        
    def zatvori(self):
        '''
            Funkcija za dugme otkazi promene, vraca parametre liste na trenutno stanje aplikacije
        '''
        self.textEditor.clear()
        self.textEditor.setText(self.element.data)
        self.hide()
        
    def podesi(self):
        '''
            Funkcija za dugme potvrdi promene, poziva akcije za izmenu jezika i izgleda
        '''
        self.element.data = self.textEditor.toPlainText()
        self.hide()
        
    def closeEvent(self, event):
        self.zatvori()
