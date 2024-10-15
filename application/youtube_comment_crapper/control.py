from yt import YtCommentScrapper
from PyQt5.QtWidgets import QFileDialog
import os 

class YtControl:
    
    YtWin = None
    folder = ''
    
    @staticmethod
    def activate():
        
        YtControl.YtWin.saveButton.clicked.connect(lambda: YtControl.save())
        YtControl.YtWin.browseButton.clicked.connect(lambda : YtControl.getFolder())
        YtControl.srapper = YtCommentScrapper()
        
    @staticmethod        
    def getFolder():
        folder = QFileDialog.getExistingDirectory(YtControl.YtWin, 'Select Folder')
        YtControl.YtWin.folder.setText(folder)
        YtControl.folder = folder
        
        
    @staticmethod
    def save():
        YtControl.YtWin.errorLabel.setText('')
        YtControl.YtWin.donne.setText('')
        if YtControl.checkEmptyEdit():
            YtControl.srapper.apiKey = YtControl.YtWin.apiKey.text()
            YtControl.srapper.connect()
            
            YtControl.srapper.videoId = YtControl.YtWin.videoId.text()
            YtControl.srapper.maxResults = YtControl.YtWin.maxResults.text()
            
            YtControl.srapper.makeRequest()
            
            name = YtControl.YtWin.fileName.text()
            
            YtControl.srapper.saveAsCsv(os.path.join(YtControl.folder, name))
            
            YtControl.YtWin.donne.setText('Donne')
        else:
            YtControl.YtWin.errorLabel.setText('An Empty Field')
    
    @staticmethod
    def checkEmptyEdit():
        w = YtControl.YtWin
        
        if (w.apiKey.text() == '' or w.videoId.text() == ''
            or w.fileName.text() == '' or w.maxResults.text() == '' 
            or w.folder == ''):
            return False
         
        return True 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        