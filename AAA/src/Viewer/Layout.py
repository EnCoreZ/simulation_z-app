
from PySide.QtGui import QGridLayout,QTreeView, QFileSystemModel,QWidget
from PySide.QtCore import QDir
class layout():
    
    '''
    Podesavanje layouta
    '''
    
    def setLayout(self):
        '''
        Sluzi za podesavanje layouta
        '''
        mainLayout = QGridLayout()
        explorerLayout = QGridLayout()
            #Kreiranje explorera
        pretrazivac = QFileSystemModel()
        pretrazivac.setRootPath(QDir.homePath())
        stablo =  QTreeView()
        stablo.setModel(pretrazivac)
            #Dodavanje stabla za pretragu i za projekte u explorerLayouta

            
            
            #Dodavanje radne povrsine u workspaceLayout
        self.workspaceLayout.addWidget(self.workspace,0,0)
            #Spajanje explorerLayouta i workspaceLayouta u mainLayout
        mainLayout.addLayout(explorerLayout,0,0,0,4)
        mainLayout.addLayout(self.workspaceLayout,0,4)
        mainWindow = QWidget()
        mainWindow.setLayout(mainLayout)
        self.setCentralWidget(mainWindow)
