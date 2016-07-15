
from PySide.QtGui import QMainWindow,QGridLayout,QTabWidget
from Viewer import menuBar,Layout,toolBar
class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("SimulationZ")
        self.setMinimumSize(700,500)
        self.workspaceLayout = QGridLayout()
        self.workspace = QTabWidget()
        self.workspace.setTabsClosable(True)
        
        self.menuBar = menuBar.menuBar()
        self.setMenuBar(self.menuBar)
        self.mainArea = Layout.layout()
        self.setCentralWidget(self.mainArea)
        
        toolBar.toolBar.tBar(self)
        toolBar.toolBar.toolBarComponents(self)
        print('ughtstser')