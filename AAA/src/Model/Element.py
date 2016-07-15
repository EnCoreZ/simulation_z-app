from Viewer.GraphicItem import GraphicItem
from Viewer.Prozor import Prozor
class Element():
    def __init__(self):
        self.ime = "element"
        self.grafics = GraphicItem(self)
        self.data = ""
        self.prozor=Prozor(self)
        
    
class PrikazniElement(Element):
    def __init__(self):
        Element.__init__(self)
        
    
class AktivniElement(Element):
    def __init__(self):
        Element.__init__(self)
        
    