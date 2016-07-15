from PySide.QtGui import QAction,QIcon
class toolBarAction():
    def tBarActions(self):
        self.element=QAction(QIcon('..//Resursi/ELEMENT.png'),"Element",self,triggered=self.Editor.Simulacija.dodajElement)
        self.iKolo=QAction(QIcon('..//Resursi/IKOLO.png'),"I Kolo",self,triggered=self.Editor.Simulacija.dodajIKolo)
        self.iliKolo=QAction(QIcon('..//Resursi/ILIKOLO.png'),"Ili Kolo",self,triggered=self.Editor.Simulacija.dodajIliKolo)