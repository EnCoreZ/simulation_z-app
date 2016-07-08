
from PySide.QtGui import QMainWindow,QGridLayout,QTabWidget
from Viewer import menuBar,Layout,toolBar
class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Inside")
        self.setMinimumSize(700,500)
        self.workspaceLayout = QGridLayout()
        self.workspace = QTabWidget()
        self.workspace.setTabsClosable(True)
        
        menuBar.menuBar.mBar(self)
        Layout.layout.setLayout(self)
        
        toolBar.toolBar.tBar(self)
        toolBar.toolBar.toolBarComponents(self)
        