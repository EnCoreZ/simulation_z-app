
from PySide.QtCore import QObject, Signal

class Node(QObject):

    childInserted = Signal(int)

    def __init__(self, name):

        self.name = name
        self.parent = None
        self.children = []
    
    def setParent(self, parent):

        self.parent = parent
    
    def getParent(self):        

        return self.parent
    
    def setName(self, name):

        self.name = name
    
    def getName(self):

        return self.name
    
    def addChild(self, child):

        self.children.append(child)
        child.setParent(self)
        
    def insertChild(self, position, child):
        if position < 0 or position > len(self.children):
            return False
        
        self.children.insert(position, child)
        child.setParent(self)
        return True
    
    def removeChild(self, position):
        if position < 0 or position > len(self.children)-1:
            return False
        child = self.children.pop(position)
        child.setParent(None)
        
        return True

    def childCount(self):
        return len(self.children)
    
    def childAt(self, row):          
        if row < 0 or row > len(self.children)-1:
            return None
        else:
            return self.children[row]
    
    def getIndex(self):
        if(self.parent is not None):
            return self.parent.children.index(self)