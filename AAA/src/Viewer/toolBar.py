
from PySide.QtGui import QToolBar
from Controler.toolBarActions import toolBarAction
class toolBar(QToolBar):
    
    def __init__(self,Editor):
        QToolBar.__init__(self)
        self.Editor=Editor
        self.toolBarAkcije=toolBarAction.tBarActions(self)
        self.addAction(self.iKolo)
        self.addAction(self.iliKolo)
        self.addAction(self.element)