from Viewer.GraphicItem import GraphicItem
from Viewer.iKolo import iKolo
from Viewer.Prozor import Prozor
from Viewer.iliKolo import iliKolo
class Element():
    def __init__(self):
        self.ime = "element"
        self.grafics = GraphicItem(self)
        self.data = ""
        self.prozor=Prozor(self)
        
class eleIKolo(Element):
    def __init__(self):
        Element.__init__(self)
        self.ime="I kolo"
        self.grafick=iKolo(self)
        self.data= "I KOLO"
        self.prozor=Prozor(self)
        self.prozor.textEditor.setReadOnly(True)
        
class eleIliKolo(Element):
    def __init__(self):
        Element.__init__(self)
        self.ime="Ili kolo"
        self.grafick= iliKolo(self)
        self.data= "ILI KOLO"
        self.prozor=Prozor(self)
        self.prozor.textEditor.setReadOnly(True)      
        
class PrikazniElement(Element):
    def __init__(self):
        Element.__init__(self)
        
    
class AktivniElement(Element):
    def __init__(self):
        Element.__init__(self)
        
    
