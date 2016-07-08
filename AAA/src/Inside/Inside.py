'''
Created on Jun 24, 2016

@author: antis
'''


import sys,time
from PySide.QtGui import QApplication
from Model.Main import mainWindow
if __name__ == "__main__":

    try:
        myApp = QApplication(sys.argv)
        
        #Splashscreen
        #splash = QSplashScreen(QPixmap("Icons/Logo#3_beta.png"))
        #splash.show()
        time.sleep(1)
        Main = mainWindow()
        Main.showMaximized()
        myApp.exec_()
        sys.exit(0)
        
    except NameError:    
        print("Name Error:",sys.exc_info()[1])  
        
    except SystemExit:   
        print("Closing Window...") 
        
    except Exception:    
        print(sys.exc_info()[1])