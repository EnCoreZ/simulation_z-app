from PySide.QtGui import QGraphicsRectItem, QGraphicsItem



class GraphicItem(QGraphicsRectItem):
    def __init__(self,element):
        QGraphicsRectItem.__init__(self)
        self.setFlag(QGraphicsItem.ItemIsMovable,True)
        self.setFlag(QGraphicsItem.ItemIsSelectable,True)
        self.setRect(50,50,50,50)
        self.setAcceptTouchEvents(True)
        self.setActive(True)
        self.setEnabled(True)
        self.GraphicsElement=element
    def mouseDoubleClickEvent(self,event):
        self.GraphicsElement.prozor.show()