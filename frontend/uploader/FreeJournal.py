import sys
from PyQt4 import QtCore, QtGui
import FJ_Desktop_UI.FreeJournal_UI as FreeJournal_UI
import FJ_Desktop_UI.NewCollection_UI as NewCollection_UI
import FJ_Desktop_UI.About_UI as About_UI
import FJ_Desktop_UI.Add_Comment_UI as Add_Comment_UI
import FJ_Desktop_UI.Preferences_UI as Preferences_UI
import webbrowser
import freejournal_cli as CLI
from os.path import isfile
import os.path

class StartQT4(QtGui.QMainWindow):
 
    model = QtGui.QDirModel()
    index = QtCore.QModelIndex()
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = FreeJournal_UI.Ui_FJ_Main_Window()
        self.ui.setupUi(self)

        self.model = QtGui.QDirModel()
        self.model.setReadOnly(False)
        self.ui.treeViewLocal.setModel(self.model)
        self.model.setSorting(QtCore.QDir.DirsFirst | QtCore.QDir.IgnoreCase | QtCore.QDir.Name)
        self.index = QtCore.QModelIndex()
        self.index = self.model.index(os.path.expanduser('~/Documents'))
        self.ui.treeViewLocal.expand(self.index)
        self.ui.treeViewLocal.scrollTo(self.index)
        self.ui.treeViewLocal.setCurrentIndex(self.index)
        self.ui.treeViewLocal.resizeColumnToContents(0)
        
        #connect "New" button with NewCollection UI
        self.ui.pushButtonNew.clicked.connect(self.NewCollecWindowOpen)
        self.ui.actionNew_Collection.triggered.connect(self.NewCollecWindowOpen)
        self.ui.pushButtonDownload.clicked.connect(self.DownloadToDirectory)
        self.ui.pushButtonAdd_Comment.clicked.connect(self.NewAdd_CommentWindowOpen)
        self.ui.actionAbout_Free_Journal.triggered.connect(self.NewAboutWindowOpen)
        self.ui.actionPrefernces.triggered.connect(self.NewPrefWindowOpen)
        self.ui.actionFree_Journal_Website.triggered.connect(self.FJWeb)
        self.ui.actionGitHub_Source.triggered.connect(self.FJSource)
        self.ui.actionView_Documentation.triggered.connect(self.FJDocs)
        self.ui.pushButtonDelete.clicked.connect(self.DeleteStuff)
        self.ui.pushButtonDonate.clicked.connect(self.FJDonate)
        self.ui.pushButtonPublish.clicked.connect(self.Publish)
        self.ui.pushButtonRebroadcast.clicked.connect(self.Rebroadcast)
        
    def FJSource(self):
        webbrowser.open('https://www.github.com/FreeJournal/freejournal', new=0, autoraise=True)
    def FJDocs(self):
        webbrowser.open('https://www.github.com/FreeJournal/freejournal/wiki', new=0, autoraise=True)    
    def FJWeb(self):
        webbrowser.open('http://www.freejournal.org', new=0, autoraise=True)
    def FJDonate(self):
        webbrowser.open('http://www.freejournal.org/donate', new=0, autoraise=True)

    def Publish(self, checked=None):
        if checked==None: return
        self.index = self.ui.treeViewLocal.currentIndex()        

    def Rebroadcast(self, checked=None):
        if checked==None: return
        self.index = self.ui.treeViewLocal.currentIndex()

    def DeleteStuff(self, checked=None):
        if checked==None: return
        self.index = self.ui.treeViewLocal.currentIndex()
        if not self.index.isValid(): return
        if self.model.fileInfo(self.index).isDir():
            self.model.rmdir(self.index)
        else:
            self.model.remove(self.index)
    
    def NewAdd_CommentWindowOpen(self, checked=None):
        if checked==None: return
        AddCommentDialog = NewAdd_CommentWindow(self)
        AddCommentDialog.show()
 
    def NewAboutWindowOpen(self, checked=None):
        if checked==None: return
        NewAbout = QtGui.QDialog()
        NewAbout.ui = About_UI.Ui_Form()
        NewAbout.ui.setupUi(NewAbout)
        NewAbout.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        NewAbout.exec_() 
 
    def NewPrefWindowOpen(self, checked=None):
        if checked==None: return
        PrefDialog = NewPrefWindow(self)
        PrefDialog.show()
        
    def DownloadToDirectory(self):
        fd = QtGui.QFileDialog(self)
        self.filename = fd.getSaveFileName(caption="Save Collection of Documents", directory='')
        CLI.get_doc_file('sample', self.filename)

    def NewCollecWindowOpen(self, checked=None):
        if checked==None: return
        self.index = self.ui.treeViewLocal.currentIndex()
        if not self.index.isValid(): return
        dialogObject = NewCollecWindow(self)
        dialogObject.show()
        
class NewPrefWindow(QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Preferences_UI.Ui_DialogPreferences()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)      

class NewAdd_CommentWindow(QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Add_Comment_UI.Ui_DialogAddComment()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.ui.buttonBoxAddComment.accepted.connect(self.PostComment)
              
    def PostComment(self):
        comment = self.ui.plainTextEditAddComment.toPlainText()
        print(comment)

class NewCollecWindow(QtGui.QDialog):
      def __init__(self, parent):
        global main_UI 
        main_UI = parent
        QtGui.QDialog.__init__(self, parent)
        self.ui = NewCollection_UI.Ui_DialogNewCollection()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)   
        global filepath
        self.filepath = ''
        self.title = ''
        self.ui.toolButtonAddDirectory.clicked.connect(self.AddDirectory)
        self.ui.buttonBoxConfirm.accepted.connect(self.PutDoc)

      def AddDirectory(self):
         fd = QtGui.QFileDialog(self)
         self.filename = fd.getOpenFileName(caption='Open File', directory='')
         if isfile(self.filename):
             text = self.filename
             self.ui.lineEditAddDirectory.setText(text)
             self.filepath = self.filename
         else:
             message = QtGui.QMessageBox(self)
             message.setText("Not a valid file.")
             message.setWindowTitle("Error")
             message.setIcon(QtGui.QMessageBox.Warning)
             message.addButton("OK", QtGui.QMessageBox.AcceptRole)
             message.exec_()
             
      def PutDoc(self):
          self.filepath = self.ui.lineEditAddDirectory.text()
          self.title = self.ui.lineEditCollectionName.text()
          if isfile(self.filepath):
             self.filepath = self.ui.lineEditAddDirectory.text()
             if not self.title == '':
                 main_UI.model.mkdir(main_UI.index, self.title)
             CLI.put_document(self.filepath)
          else:
             message = QtGui.QMessageBox(self)
             message.setText("Please enter a vaild directory path.")
             message.setWindowTitle("Error")
             message.setIcon(QtGui.QMessageBox.Warning)
             message.addButton("OK", QtGui.QMessageBox.AcceptRole)
             message.exec_() 

def run():
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())

            
if __name__ == "__main__":
    run()
