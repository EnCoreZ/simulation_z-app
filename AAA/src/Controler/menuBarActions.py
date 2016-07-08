from PySide.QtGui import QAction,QIcon

class menuBarActions():
    def mBarActions(self):
        self.newFileAction = QAction(QIcon('Icons/new.png'),"New",self)
        self.openFileAction = QAction(QIcon('Icons/new.png'),"Open",self)
        self.saveAction = QAction(QIcon('Icons/new.png'),"Save",self)
        self.saveAsAction = QAction(QIcon('Icons/new.png'),"Save As",self)
        self.exitProgramAction = QAction(QIcon('Icons/new.png'),"Exit",self)
        
        self.undoAction = QAction(QIcon('Icons/new.png'),"Undo",self)
        self.redoAction = QAction(QIcon('Icons/new.png'),"Redo",self)
        self.cutAction = QAction(QIcon('Icons/new.png'),"Cut",self)
        self.copyAction = QAction(QIcon('Icons/new.png'),"Copy",self)
        self.pasteAction = QAction(QIcon('Icons/new.png'),"Paste",self)
        
        self.optionsAction = QAction(QIcon('Icons/new.png'),"Options",self)