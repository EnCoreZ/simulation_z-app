
from PySide.QtCore import QAbstractItemModel, QModelIndex
from PySide import QtCore
from PySide.QtGui import QIcon



class HierarchyTreeModel(QAbstractItemModel):

    def __init__(self, root):

        super(HierarchyTreeModel, self).__init__()
        self.root = root
        
    def rowCount(self, parent):

        if not parent.isValid():
            parentNode = self.root
        else:
            parentNode = parent.internalPointer()
        
        return parentNode.childCount()
    
    def columnCount(self, parent):

        return 1
    
    def data(self, index, role):

        if not index.isValid():
            return None
        
        node = index.internalPointer()
        
        if role == QtCore.Qt.DisplayRole:
            return node.getName()
        
        if role == QtCore.Qt.DecorationRole:
            return QIcon("../folder.png")
    
    def headerData(self, section, orientation, role):

        if role == QtCore.Qt.DisplayRole:
            return "Package Explorer" 
    
    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable 
    
    def index(self, row, column, parent):

        if not parent.isValid():
            parentNode = self.root
        else:
            parentNode = parent.internalPointer()
            
        childItem = parentNode.childAt(row)
        if (childItem):
            return self.createIndex(row, 0, childItem)
        else:
            return QModelIndex()
    
    def parent(self, index):

        node = index.internalPointer()
        parentNode = node.getParent()
        
        if (parentNode == self.root):
            return QModelIndex()
         
        return self.createIndex(parentNode.getIndex(), 0, parentNode)
    
    def insertRow(self, position, row, parent = QModelIndex()):

        if parent.isValid():
            parentNode = parent.internalPointer()
        else:
            parentNode = self.root
        
        self.beginInsertRows(parent, position, position)
        
        success = parentNode.insertChild(position, row)
        
        self.endInsertRows()
        
        return success
    
    def removeRow(self, position, parent = QModelIndex()):

        if parent.isValid():
            parentNode = parent.internalPointer()
        else:
            parentNode = self.root
        
        self.beginRemoveRows(parent, position, position)
        
        success = parentNode.removeChild(position)
        
        self.endRemoveRows()
        
        return success