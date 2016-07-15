from Model.Element import Element
from PySide.QtGui import QPen
class Simulacija():
    def __init__(self,sceneView):
        self.Elementi=[]
        self.Scene=sceneView
        self.br_elemenata=0
        self.ime_simulacije="Nova_simulacija1"
        self.lokacija=""
    def snimanjeSimulacije(self):
        pass
    def brisanjeSimulacije(self):
        pass
    def oslobadjanjeMemorije(self):
        pass
    def fillModel(self):
        pass
    def dodajElement(self):
        self.br_elemenata+=1
        self.newElement=Element()
        
        self.Scene.scene().addRect(self.newElement.grafics.rect(),pen=QPen())
        
        self.Elementi.append(self.newElement)
        