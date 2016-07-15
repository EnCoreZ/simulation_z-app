from PySide.QtGui import QMainWindow,QGridLayout,QTabWidget,QGraphicsScene,QGraphicsView
from Viewer import menuBar,Layout
from Model.Editor import Editor
from Viewer.Prozor import Prozor
from Model.Element import Element
class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("SimulationZ")
        self.setMinimumSize(700,500)
        self.workspaceLayout = QGridLayout()
        self.workspace = QTabWidget()
        self.workspace.setTabsClosable(True)
        
        self.graphScene = QGraphicsScene()
        self.sceneView = QGraphicsView()
        self.sceneView.setScene(self.graphScene)
        
        self.Editor = Editor(self.sceneView)
        
        self.menuBar = menuBar.menuBar()
        self.setMenuBar(self.menuBar)

        self.mainArea = Layout.layout(self.Editor,self.sceneView)
        self.setCentralWidget(self.mainArea)
        
        self.toolBar = self.mainArea.childAt(1,0)