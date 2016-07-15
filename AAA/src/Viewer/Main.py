from PySide.QtGui import QMainWindow,QGridLayout,QTabWidget,QGraphicsScene,QGraphicsView,QMessageBox
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
        
        self.menuBar = menuBar.menuBar(self)
        self.setMenuBar(self.menuBar)

        self.mainArea = Layout.layout(self.Editor,self.sceneView)
        self.setCentralWidget(self.mainArea)
        
        self.toolBar = self.mainArea.childAt(1,0)
        
    def exitFile(self):     
        if self.i==0:         
            userInfo =QMessageBox.question(self,self.language.Exit,self.language.RUSURE,QMessageBox.Yes | QMessageBox.No)
            if userInfo == QMessageBox.Yes: 
                self.close()
            else:
                pass
        else:
            userInfo =QMessageBox.question(self,self.language.Exit,self.language.OTab,QMessageBox.Yes | QMessageBox.No)
            if userInfo == QMessageBox.Yes: 
                self.close()
            else:
                pass