from PySide.QtGui import QMenu ,QMenuBar
from Controler import menuBarActions
class menuBar(QMenuBar):
    def __init__(self):
        
        QMenuBar.__init__(self)
        
        menuBarActions.menuBarActions.mBarActions(self)
        #File
        self.fileMenu = QMenu()
        self.fileMenu.setTitle("File")
        self.fileMenu.addAction(self.newFileAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.openFileAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.saveAsAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitProgramAction)
        self.addMenu(self.fileMenu)
        #Edit
        self.editMenu=QMenu()
        self.editMenu.setTitle("Edit")
        self.editMenu.addAction(self.undoAction)
        self.fileMenu.addSeparator()
        self.editMenu.addAction(self.redoAction)
        self.fileMenu.addSeparator()
        self.editMenu.addAction(self.cutAction)
        self.fileMenu.addSeparator()
        self.editMenu.addAction(self.copyAction)
        self.fileMenu.addSeparator()
        self.editMenu.addAction(self.pasteAction)
        self.fileMenu.addSeparator()
        self.addMenu(self.editMenu)

        self.addAction(self.optionsAction)