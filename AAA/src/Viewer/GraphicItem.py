from PySide.QtGui import QGraphicsRectItem


class GraphicItem(QGraphicsRectItem):
    def __init__(self,element):
        QGraphicsRectItem.__init__(self)
        self.setFlag(self.ItemIsMovable,True)
        self.setFlag(self.ItemIsSelectable,True)
        self.setRect(50,50,50,50)
        self.GraphicsElement=element
