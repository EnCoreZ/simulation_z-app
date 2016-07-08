from PySide.QtGui import QMenu ,QMenuBar
#from Controler import menuBarActions
class menuBar():
    def mBar(self):
        #menuBarActions.menuBarActions.mBarActions(self)
        menu = QMenuBar()
        fileMenu = QMenu()
        fileMenu.setTitle("File")
        fileNewMenu = QMenu()
        fileNewMenu.setTitle("New")
        #fileNewMenu.addAction(self.newTxtAction)
        fileMenu.addMenu(fileNewMenu)
        fileMenu.addSeparator()
        
        menu.addMenu(fileMenu)
        self.setMenuBar(menu)