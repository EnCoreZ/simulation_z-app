from PySide.QtGui import QMenu ,QMenuBar
#from Controler import menuBarActions
class menuBar(QMenuBar):
    def __init__(self):
        #menuBarActions.menuBarActions.mBarActions(self)
        QMenuBar.__init__(self)
        self.fileMenu = QMenu()
        self.fileMenu.setTitle("File")
        self.fileNewMenu = QMenu()
        self.fileNewMenu.setTitle("New")
        #fileNewMenu.addAction(self.newTxtAction)
        self.fileMenu.addMenu(self.fileNewMenu)
        self.fileMenu.addSeparator()
        
        self.addMenu(self.fileMenu)
        