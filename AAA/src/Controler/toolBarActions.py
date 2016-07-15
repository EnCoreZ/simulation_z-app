from PySide.QtGui import QAction,QIcon
class toolBarAction():
    def tBarActions(self):
        self.iKolo=QAction(QIcon('..//Resursi/IKOLO.png'),"I Kolo",self,shortcut="CTRL+T",statusTip="Kreiranje novog elementa",triggered=self.Editor.Simulacija.dodajElement)