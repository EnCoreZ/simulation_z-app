from Viewer.GraphicItem import GraphicItem
from Viewer.prozor import prozor
class Element():
    def __init__(self):
        self.grafics = GraphicItem(self)
        self.prozor=prozor()
    
class PrikazniElement(Element):
    def __init__(self):
        Element.__init__(self)
        
    
class AktivniElement(Element):
    def __init__(self):
        Element.__init__(self)
        
    