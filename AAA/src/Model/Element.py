from Viewer.GraphicItem import GraphicItem

class Element():
    def __init__(self):
        self.grafics = GraphicItem(self)

    
class PrikazniElement(Element):
    def __init__(self):
        Element.__init__(self)
        
    
class AktivniElement(Element):
    def __init__(self):
        Element.__init__(self)
        
    