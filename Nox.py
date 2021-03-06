import os
import sys
import datetime
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, Qt
from PyQt5.QtCore import (Qt, pyqtSignal,QUrl, QSize)
from PyQt5.QtWebEngineWidgets import *
from option_window_class2 import *

#first installation of PyQt5, QWebEngine, datetime, os, sys is required

#This class is used for creating the tab of the browser

class TabPage(QMainWindow):

    def __init__(self,urlview,t_no):
        super().__init__()
        # First, initialize the tab page with the url it is going to open and the tab number.
        # and set the incognito and reference mode flags down
        self.tab_no=t_no

        self.incog_flag = 0
        self.ref_flag = 0


        # The Tab Page contains three section :
        # 1. The Toolbar section
        # 2. The webview section called the pageview
        # 3. The status bar

        self.url = urlview

        # Setting up the webview section

        self.pagewindow = QWebEngineView()

        self.pagewindow.setUrl(QUrl(urlview))


        # This signal is generated when the url has changed in the current tab page object
        self.pagewindow.urlChanged.connect(self.update_urlbar)
        # This signal is generated when the loading the current url has finished
        self.pagewindow.loadFinished.connect(self.update_title)


        self.setCentralWidget(self.pagewindow)

        # setting up the status bar

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        # setting up the toolbar

        self.navtb = QToolBar("Navigation")
        self.navtb.setIconSize(QSize(32, 32))
        self.addToolBar(self.navtb)

        self.back_btn = QAction(QIcon(os.path.join('images', 'images/back.png')), "Back", self)
        self.back_btn.setStatusTip("Back to previous page")
        self.back_btn.triggered.connect(self.pagewindow.back)
        self.back_btn.setIcon(QtGui.QIcon('images/back.png'))
        self.navtb.addAction(self.back_btn)

        self.next_btn = QAction(QIcon(os.path.join('images', 'images/forward.png')), "Forward", self)
        self.next_btn.setStatusTip("Forward to next page")
        self.next_btn.triggered.connect(self.pagewindow.forward)
        self.next_btn.setIcon(QtGui.QIcon('images/forward.png'))
        self.navtb.addAction(self.next_btn)

        self.reload_btn = QAction(QIcon(os.path.join('images', 'images/refresh.png')), "Reload", self)
        self.reload_btn.setStatusTip("Reload page")
        self.reload_btn.triggered.connect(self.pagewindow.reload)
        self.reload_btn.setIcon(QtGui.QIcon('images/refresh.png'))
        self.navtb.addAction(self.reload_btn)

        self.home_btn = QAction(QIcon(os.path.join('images', 'images/home.png')), "Home", self)
        self.home_btn.setStatusTip("Go home")
        self.home_btn.triggered.connect(self.navigate_home)
        self.home_btn.setIcon(QtGui.QIcon('images/google.png'))
        self.navtb.addAction(self.home_btn)

        self.navtb.addSeparator()

        self.placeholderspace = QLabel()
        self.navtb.addWidget(self.placeholderspace)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        self.navtb.addWidget(self.urlbar)


        self.placeholderspace2 = QLabel()
        self.navtb.addWidget(self.placeholderspace2)


        self.navtb.addSeparator()

        self.book_btn = QAction(QIcon(os.path.join('images', 'images/stop.png')), "Bookmark This Page", self)
        self.book_btn.setStatusTip("Bookmark current page")
        self.book_btn.triggered.connect(self.bookmarkSaver)
        self.book_btn.setIcon(QtGui.QIcon('images/bookmark.png'))
        self.navtb.addAction(self.book_btn)

        self.stop_btn = QAction(QIcon(os.path.join('images', 'images/stop.png')), "Stop", self)
        self.stop_btn.setStatusTip("Stop loading current page")
        self.stop_btn.triggered.connect(self.pagewindow.stop)
        self.stop_btn.setIcon(QtGui.QIcon('images/stop.png'))
        self.navtb.addAction(self.stop_btn)

        self.option_btn = QAction(QIcon(os.path.join('images', 'images/stop.png')), "Options", self)
        self.option_btn.setStatusTip("Options")
        self.option_btn.triggered.connect(self.option)
        self.option_btn.setIcon(QtGui.QIcon('images/option.png'))
        self.navtb.addAction(self.option_btn)

        self.show()

    def navigate_home(self):
        '''
        This function is triggered when the home button is clicked.
        '''
        self.pagewindow.setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):
        '''
        Useful for setting the url of the pagewindow.
        '''
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.pagewindow.setUrl(q)

    def update_title(self):
        '''
        Updates the title of the tab
        '''
        self.title = self.pagewindow.page().title()

    def update_urlbar(self, q):
        '''
        This function, updates the urlbar with q and at the same time records
        history if incognito is off or reference mode is on. While updating it
        is necessary to check if the page has been bookmarked. If it has been
        bookmarked, then the bookmark button needs to be turned blue(Which is obtained from the images).
        :param q: URL of the page
        :return:
        '''

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

        if self.incog_flag == 0:
            self.history_writer = open("History.txt", "a")
            now = datetime.datetime.now()
            n=now.strftime("%Y-%m-%d %H:%M:%S")
            self.historyElement="  [ "+n+" ]  "+q.toString()+"\n\n" # Finds the history
            self.history_writer.write(self.historyElement)
            self.history_writer.close()
        if self.ref_flag == 1:
            self.historyElement = q.toString() + "\n\n"
            self.ref_file.write(self.historyElement)

        bm=open("Bookmarks.txt", "r")
        b=bm.readlines()
        l=q.toString()+'\n'
        if l in b:
            self.book_btn.setIcon(QtGui.QIcon('images/bookmark_done.png'))

        else:
            self.book_btn.setIcon(QtGui.QIcon('images/bookmark.png'))
        bm.close()

    def option(self):
        '''
        This function is triggered when the options button is clicked.
        It opens up a options_window_class2 object for the current page.
        :return:
        '''
        self.dlg=Ui_Dialog(self.tab_no)

        #This logic is used for toggling of the incognito and reference button

        if self.ref_flag == 0:
            self.dlg.Ref_btn.setText("Turn ON Reference")
        else:
            self.dlg.Ref_btn.setText("Turn OFF Reference")

        if self.incog_flag == 0:
            self.dlg.Incog_btn.setText("Turn ON Incognito")
        else:
            self.dlg.Incog_btn.setText("Turn OFF Incognito")

        # If any of the buttons are clicked, then appropriate constant will be passed to the
        # WriteOnShowArea function. Accordingly, the necessary text files will be displayed.

        self.dlg.Incog_btn.clicked.connect(lambda: self.WriteOnShowArea("i"))
        self.dlg.Bookmarks_btn.clicked.connect(lambda: self.WriteOnShowArea("b"))
        self.dlg.Ref_btn.clicked.connect(lambda: self.WriteOnShowArea("r"))
        self.dlg.History_btn.clicked.connect(lambda: self.WriteOnShowArea("h"))

        self.dlg.exec_()

    def WriteOnShowArea(self, option):
        '''
        This function will show necessary text files onto the show area.
        :param option: may be h,b,i or r as per the button which is clicked
        :return:
        '''
        self.dlg.show_area.clear()
        if option=="h":
            t = open("History.txt", "r")
            self.dlg.show_area.setText(t.read())
            t.close()
        elif option=="b":
            t = open("Bookmarks.txt", "r")
            self.dlg.show_area.setText(t.read())
            t.close()
        elif option=="i":
            if self.incog_flag == 0:
                self.dlg.show_area.setText('Incognito is now ON\nSearch History will not be stored')
                self.incog_flag = 1
                self.dlg.Incog_btn.setText("Turn OFF Incognito")

            else:
                self.dlg.show_area.setText('Incognito is now OFF')
                self.incog_flag = 0
                self.dlg.Incog_btn.setText("Turn ON Incognito")

        elif option=="r":


            if self.ref_flag == 0:
                self.dlg.show_area.setText('Reference has been turned on')
                self.ref_file=open("References.txt","w")
                self.ref_file.write('\n--------------------------------\n')
                self.dlg.Ref_btn.setText("Turn OFF Reference")
                self.ref_flag = 1
            elif self.ref_flag == 1:
                self.ref_file.close()
                self.ref_file = open("References.txt","r")
                self.dlg.show_area.setText('References:\n'+self.ref_file.read())
                self.ref_file.close()
                os.remove("References.txt")
                self.dlg.Ref_btn.setText("Turn ON Reference")
                self.ref_flag=0

    def bookmarkSaver(self):
        '''
        This function is useful for writing on the bookmark.txt file
        :return:
        '''

        link = self.urlbar.text() + "\n"
        self.book = open("Bookmarks.txt", "r")
        links=self.book.readlines()
        #print(links)
        self.book.close()

        findflag=0
        for l in links:
            if l == link:
                findflag=1
                break

        if findflag == 0:
            self.book_write = open("Bookmarks.txt", "a")
            self.book_write.write(link)
            self.book_write.close()

        self.book_btn.setIcon(QtGui.QIcon('images/bookmark_done.png'))

#This HomeTabWindow object is created when the application is executed

class HomeTabWindow(QWidget):

    def __init__(self):
        super().__init__()

        # This is used for taking care of the tabs
        self.tabcount = 0
        self.tablist = list()

        # Setting up the user interface of the Home Tab
        self.UI = QTabWidget()

        # Setting the size of window
        self.UI.setTabsClosable(True)
        self.UI.setMovable(True)
        self.UI.setTabPosition(QTabWidget.North)
        self.UI.setWindowIcon(QtGui.QIcon('images/nox.png'))
        self.UI.setMinimumSize(1100,900)
        self.UI.setWindowTitle("Nox")

        # Setting Layout of the home page
        self.setUILayout()
        self.UI.tabCloseRequested.connect(self.tabdestructor)

    def setUILayout(self):
        '''
        Used for setting up the entire hometab user interface
        :return:
        '''

        buttonlayout = QGridLayout()
        buttonlayout.setColumnMinimumWidth(0, 100)
        buttonlayout.setColumnMinimumWidth(1, 100)
        buttonlayout.setColumnMinimumWidth(2, 100)

        buttonlayout.setRowMinimumHeight(0, 100)
        buttonlayout.setRowMinimumHeight(1, 100)
        buttonlayout.setRowMinimumHeight(2, 100)

        self.UI.Google = QPushButton(self)
        self.UI.Google.setMaximumSize(200, 200)
        self.UI.Google.setMinimumSize(200, 200)
        self.UI.Google.setObjectName("Google")
        self.UI.Google.setIcon(QtGui.QIcon('images/google.png'))
        self.UI.Google.setIconSize(QtCore.QSize(200, 200))
        self.UI.Google.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.UI.Google.clicked.connect(lambda: self.createTab("https://google.com/"))
        buttonlayout.addWidget(self.UI.Google, 0, 0)

        self.UI.LinkedIn = QPushButton(self)
        self.UI.LinkedIn.setMaximumSize(200, 200)
        self.UI.LinkedIn.setMinimumSize(200, 200)
        self.UI.LinkedIn.setObjectName("LinkedIn")
        self.UI.LinkedIn.setIcon(QtGui.QIcon('images/linkedin.png'))
        self.UI.LinkedIn.setIconSize(QtCore.QSize(200, 200))
        self.UI.LinkedIn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.UI.LinkedIn.clicked.connect(lambda: self.createTab("https://linkedin.com/"))
        buttonlayout.addWidget(self.UI.LinkedIn, 0, 1)

        self.UI.ResearchGate = QPushButton(self)
        self.UI.ResearchGate.setMaximumSize(200, 200)
        self.UI.ResearchGate.setMinimumSize(200, 200)
        self.UI.ResearchGate.setObjectName("ResearchGate")
        self.UI.ResearchGate.setIcon(QtGui.QIcon('images/researchgate.png'))
        self.UI.ResearchGate.setIconSize(QtCore.QSize(200, 200))
        self.UI.ResearchGate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.UI.ResearchGate.clicked.connect(lambda: self.createTab("https://researchgate.net/"))
        buttonlayout.addWidget(self.UI.ResearchGate, 0, 2)

        self.UI.Youtube = QPushButton(self)
        self.UI.Youtube.setMaximumSize(200, 200)
        self.UI.Youtube.setMinimumSize(200, 200)
        self.UI.Youtube.setObjectName("Youtube")
        self.UI.Youtube.setIcon(QtGui.QIcon('images/youtube.png'))
        self.UI.Youtube.setIconSize(QtCore.QSize(200, 200))
        self.UI.Youtube.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.UI.Youtube.clicked.connect(lambda: self.createTab("https://youtube.com/"))
        buttonlayout.addWidget(self.UI.Youtube, 1, 0)

        self.UI.IEEEXplore = QPushButton(self)
        self.UI.IEEEXplore.setMaximumSize(200, 200)
        self.UI.IEEEXplore.setMinimumSize(200, 200)
        self.UI.IEEEXplore.setObjectName("IEEEXplore")
        self.UI.IEEEXplore.setIcon(QtGui.QIcon('images/ieeexplore.png'))
        self.UI.IEEEXplore.setIconSize(QtCore.QSize(200, 200))
        self.UI.IEEEXplore.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.UI.IEEEXplore.clicked.connect(lambda: self.createTab("https://ieeexplore.ieee.org/"))
        buttonlayout.addWidget(self.UI.IEEEXplore, 1, 1)

        self.UI.Search = QPushButton(self)
        self.UI.Search.setMaximumSize(200, 200)
        self.UI.Search.setMinimumSize(200, 200)
        self.UI.Search.setObjectName("Search")
        self.UI.Search.setIcon(QtGui.QIcon('images/search.png'))
        self.UI.Search.setIconSize(QtCore.QSize(200, 200))
        self.UI.Search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        buttonlayout.addWidget(self.UI.Search, 1, 2)
        self.UI.Search.clicked.connect(lambda: self.createTab())

        buttonplaceholder = QWidget()
        buttonplaceholder.setLayout(buttonlayout)

        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignCenter)

        self.UI.label = QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.UI.label.setFont(font)
        self.UI.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.UI.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.UI.label.setText("Getting Started with\nNox\n")

        placeholdertop = QLabel(self)
        placeholdertop.setText("\n\n")

        vbox.addWidget(placeholdertop)
        vbox.addWidget(self.UI.label)
        vbox.addWidget(buttonplaceholder)

        Home = QWidget()
        Home.setLayout(vbox)

        self.UI.addTab(Home, "Home")

        self.UI.show()

    def createTab(self,starttaburl="http://google.com"):
        '''
        This function created a tab page by passing on the url of the tab to be
        created and the count of the tab.i.e, which tab it is.
        :param starttaburl:
        :return:
        '''

        self.tabcount = self.tabcount + 1

        self.UI.tab = TabPage(starttaburl, len(self.tablist)+1)
        self.tablist.insert(self.tabcount-1, self.UI.tab)
        self.UI.addTab(self.tablist[self.tabcount-1],"Loading...")
        self.UI.setCurrentIndex(self.tabcount)
        self.tablist[self.tabcount-1].pagewindow.loadFinished.connect(self.printer)
        self.UI.setTabText(self.tabcount,"Loading...")
        # If a download request is encountered while tab creation, the dialog box is opened.
        self.UI.tab.pagewindow.page().profile().downloadRequested.connect(self.on_downloadRequested)

    @QtCore.pyqtSlot("QWebEngineDownloadItem*")
    def on_downloadRequested(self, download):

        old_path = download.url().path()  # download.path()
        suffix = QtCore.QFileInfo(old_path).suffix()
        path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save File", old_path, "*." + suffix
        )
        if path:
            download.setPath(path)
            download.accept()
            download.finished.connect(self.foo)

    def foo(self):
        '''
        This function prints finish on the console when download is completed
        :return:
        '''
        print("finished")

    def tabdestructor(self, index):
        '''
        This method is useful for deleting a tab. Since, one needs to unsubscribe while closing
        a youtube tab, a logic has been added to handle youtube pages. If it is a
        youtube page, then first set the url of the page to google (this will stop the sound)
        and then close it. If the tab is the home tab, then the application is closed.
        :param index:
        :return:
        '''

        if index != 0:
            self.UI.setCurrentIndex(index)

            self.tabcount =self.tabcount-1

            if "youtube" in self.tablist[index-1].url:
                self.tablist[index-1].pagewindow.setUrl(QUrl("https://google.com"))

            self.tablist.pop(index-1)
            self.UI.removeTab(index)
            self.UI.setCurrentIndex(index-1)

        else:
            sys.exit()

    def printer(self):
        '''
        Used to set the tab title once data has been retrieved
        :return:
        '''
        if self.tabcount != 0:
            self.UI.setTabText(self.tabcount,self.UI.tab.title)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    oMainwindow = HomeTabWindow()

    sys.exit(app.exec_())





