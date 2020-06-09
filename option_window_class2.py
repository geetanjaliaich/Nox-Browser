# This is the class used for creating the option dialog box.
# An object of the class is created when the option button is invoked




from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self, tab_no):
        super().__init__()

        self.setObjectName("Dialog")


        self.setMinimumSize(QtCore.QSize(740, 478))
        self.setMaximumSize(QtCore.QSize(740, 478))

        self.Incog_btn = QtWidgets.QPushButton(self)
        self.Incog_btn.setGeometry(QtCore.QRect(0, 130, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.Incog_btn.setFont(font)
        self.Incog_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Incog_btn.setObjectName("Incog_btn")
        if tab_no > 1:
            self.Incog_btn.setEnabled(False)




        self.Bookmarks_btn = QtWidgets.QPushButton(self)
        self.Bookmarks_btn.setGeometry(QtCore.QRect(0, 10, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.Bookmarks_btn.setFont(font)
        self.Bookmarks_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Bookmarks_btn.setShortcut("")
        self.Bookmarks_btn.setObjectName("Bookmarks_btn")


        self.Ref_btn = QtWidgets.QPushButton(self)
        self.Ref_btn.setGeometry(QtCore.QRect(0, 190, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.Ref_btn.setFont(font)
        self.Ref_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Ref_btn.setObjectName("Ref_btn")
        if tab_no > 1:
            self.Ref_btn.setEnabled(False)



        self.show_area = QtWidgets.QTextEdit(self)
        self.show_area.setGeometry(QtCore.QRect(240, 10, 491, 461))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(12)
        self.show_area.setFont(font)
        self.show_area.setAutoFillBackground(False)
        self.show_area.setAutoFormatting(QtWidgets.QTextEdit.AutoBulletList)
        self.show_area.setReadOnly(True)
        self.show_area.setCursorWidth(0)
        self.show_area.setPlaceholderText("1.) Bookmarks - Contains links saved\n\n2.) History - Contains history of previous urls visited\n\n3.) Reference - A special feature to record history when this feature is on. On turning it off, it display the recorded history.\n\n4.) Incognito - Search without saving browser history\n\n---[Note]---\nThe feature References and Incognito mode is available only for the first tab that is created after the Home Page and can be operated from only that tab. Closing the tab will result in error")



        self.show_area.setObjectName("show_area")

        self.History_btn = QtWidgets.QPushButton(self)
        self.History_btn.setGeometry(QtCore.QRect(0, 70, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.History_btn.setFont(font)
        self.History_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.History_btn.setObjectName("History_btn")


        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(16, 262, 211, 201))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.show()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Option"))
        self.Incog_btn.setText(_translate("Dialog", "Turn On Incognito"))
        self.Bookmarks_btn.setText(_translate("Dialog", "Bookmarks"))

        self.History_btn.setText(_translate("Dialog", "History"))
        self.label.setText(_translate("Dialog", "Nox Version 1.0.0\nDate: June 2020\nCreator: Geetanjali Aich"))





