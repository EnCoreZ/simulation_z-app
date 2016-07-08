
from PySide.QtGui import QGridLayout,QWidget,QToolBar,QGraphicsScene
from Viewer import hierarchy_tree_model,hierarchy_tree_view,toolBar
from Model import hierarchy_node
class layout(QWidget):
    
    '''
    Podesavanje layouta
    '''
    
    def __init__(self):
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
        self.tBar=QToolBar()
        #radna povrsina(zameniti kasnije)
        self.root2 = hierarchy_node.Node("EDITOR")
        self.treeModel2 = hierarchy_tree_model.HierarchyTreeModel(self.root2)
        self.tree2 = hierarchy_tree_view.HierarchyTreeView()
        self.tree2.setModel(self.treeModel2)
        #radna povrs
        self.workspaceLayout = QGridLayout()
        
        self.workspaceLayout.addWidget(self.tree,0,0,2,2,0)
        self.workspaceLayout.addWidget(self.tBar,0,3,1,1,0)
        self.workspaceLayout.addWidget(self.tree2,1,3,1,1,0)
        
        self.setLayout(self.workspaceLayout)
        
        