
from PySide.QtGui import QGridLayout,QWidget
from Viewer import hierarchy_tree_model,hierarchy_tree_view
from Model import hierarchy_node
from Viewer.toolBar import toolBar
class layout(QWidget):
    
    '''
    Podesavanje layouta
    '''
    
    def __init__(self,Editor,sceneView):
        '''
        Sluzi za podesavanje layouta
        '''
        QWidget.__init__(self)
        #stablo
        self.root = hierarchy_node.Node("Workspace")
        self.treeModel = hierarchy_tree_model.HierarchyTreeModel(self.root)
        self.tree = hierarchy_tree_view.HierarchyTreeView()
        self.tree.setModel(self.treeModel)
        #toolbar
        self.tBar=toolBar(Editor)
        #radna povrsina(zameniti kasnije)
        self.sceneView=sceneView
        #radna povrs
        self.workspaceLayout = QGridLayout()
        
        self.workspaceLayout.addWidget(self.tree,0,0,2,2,0)
        self.workspaceLayout.addWidget(self.tBar,0,3,1,1,0)
        self.workspaceLayout.addWidget(self.sceneView,1,3,1,1,0)
        
        self.setLayout(self.workspaceLayout)
        
        