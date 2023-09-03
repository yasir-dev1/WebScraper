from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow,QFileDialog
from PyQt5 import uic
from PyQt5.QtCore import QThread,pyqtSignal
import sys,Scraper


app = QApplication(sys.argv)

ui_file = "GUI.ui" 
ui_class, base_class = uic.loadUiType(ui_file)

class Scrap(QThread):
    finished = pyqtSignal(str)
    def __init__(self,CSV,Result,_class,tag):
        super().__init__()
        self.csv = CSV
        self.result = Result
        self._class = _class
        self.tag = tag

    def run(self):
        result = Scraper.Scrap(self.csv,self.result,self.tag,self._class)
        self.finished.emit(result)


class Dialog(QDialog, ui_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.CSV.mousePressEvent = self.csvPath
        self.Result.mousePressEvent = self.resultPath
        self.Start.clicked.connect(self.start)
        self.PB.setVisible(False)


    def csvPath(self,event):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog(self, options=options)
        file_dialog.setNameFilter('CSV files (*.csv);')

        if file_dialog.exec_() == QFileDialog.Accepted:
            self.selected_file = file_dialog.selectedFiles()[0]
            self.CSV.setText(self.selected_file)
    def  resultPath(self,event):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        folder_dialog = QFileDialog.getExistingDirectory(self, "Select Folder", options=options)

        if folder_dialog:
            self.folder_dialog=folder_dialog
            self.Result.setText(self.folder_dialog)
    def start(self):
        self.PB.setVisible(True)
        tag = self.Tag.text()
        _class = self.Class.text()
        self.Scrap = Scrap(self.selected_file,self.folder_dialog,_class,tag)
        self.Scrap.finished.connect(self.ScrapFinish)
        self.Scrap.start()
    def ScrapFinish(self,result):
        self.PB.setVisible(False)
        
        

dialog = Dialog()

# QDialog'u gösterin
dialog.show()

sys.exit(app.exec_())
