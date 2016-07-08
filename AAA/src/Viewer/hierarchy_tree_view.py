
from PySide.QtCore import Qt, QModelIndex
from PySide.QtGui import QTreeView, QMenu, QAction, QAbstractItemView

from Model.hierarchy_node import Node


class HierarchyTreeView(QTreeView):


    def __init__(self):
        super(HierarchyTreeView, self).__init__()
        
        #ukljucuje kontekstni meni
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.openMenu)
        
    
    def openMenu(self, position):
        self.contextMenu = QMenu()
        newMenu = QMenu("New") 
        self.contextMenu.addMenu(newMenu)
        
        actionNewProj = QAction("NewProject", None)
        actionNewProj.triggered.connect(self.addNode)
        
        actionRename = QAction("Rename", None)
        actionRename.triggered.connect(self.renameNode)
        
        actionRemProj = QAction("Delete", None)
        actionRemProj.triggered.connect(self.removeNode)
        
        newMenu.addAction(actionNewProj)
        self.contextMenu.addAction(actionRename)
        self.contextMenu.addAction(actionRemProj)
        
        #prikaz kontekstnog menija
        self.contextMenu.exec_(self.viewport().mapToGlobal(position))
        
    def addNode(self):
        model = self.model()
        
        node = Node("NoviCvor")
        
        
        
        if not self.currentIndex().isValid():
            model.insertRow(model.rowCount(self.currentIndex()), node)
        else:
            model.insertRow(model.rowCount(self.currentIndex()), node, self.currentIndex())
        self.expand(self.currentIndex())
    
    def removeNode(self):
        model = self.model()
        model.removeRow(self.currentIndex().internalPointer().getIndex(), self.currentIndex().parent())    
        
    def renameNode(self):
        self.currentIndex().internalPointer().setName("NOVO")
    
    
    def mousePressEvent(self, event)
        if(self.selectionMode() == QAbstractItemView.SingleSelection):
            self.clearSelection()
            self.setCurrentIndex(QModelIndex())
        super(HierarchyTreeView, self).mousePressEvent(event)