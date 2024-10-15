from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys
from control import YtControl


class YoutubeCommentCrapper(QMainWindow):
    def __init__(self):
        super(YoutubeCommentCrapper, self).__init__()
        uic.loadUi('mainwindow.ui', self)
        YtControl.YtWin = self
        
        YtControl.activate()
        
        # initUi :
        self.initUi()
        
    def initUi(self):
        self.resize(372, 534)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    win = YoutubeCommentCrapper()
    win.show()
    
    sys.exit(app.exec())