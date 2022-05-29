# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceGGhVUy.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

from gui\widgets\py_window\py_window import PyWindow
from pycredits import PyCredits
from pyleftcolumn import PyLeftColumn
from pyleftmenu import PyLeftMenu
from pypopupnotification import PyPopupNotification
from pytitlebar import PyTitleBar

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(923, 637)
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget_layout = QVBoxLayout(self.central_widget)
        self.central_widget_layout.setObjectName(u"central_widget_layout")
        self.window = PyWindow(self.central_widget)
        self.window.setObjectName(u"window")
        self.window.setFrameShape(QFrame.StyledPanel)
        self.window.setFrameShadow(QFrame.Raised)
        self.left_menu_frame = QFrame(self.window)
        self.left_menu_frame.setObjectName(u"left_menu_frame")
        self.left_menu_frame.setGeometry(QRect(20, 19, 181, 551))
        self.left_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_frame.setFrameShadow(QFrame.Raised)
        self.left_menu_layout = QHBoxLayout(self.left_menu_frame)
        self.left_menu_layout.setObjectName(u"left_menu_layout")
        self.left_menu = PyLeftMenu(self.left_menu_frame)
        self.left_menu.setObjectName(u"left_menu")

        self.left_menu_layout.addWidget(self.left_menu)

        self.left_column_frame = QFrame(self.window)
        self.left_column_frame.setObjectName(u"left_column_frame")
        self.left_column_frame.setGeometry(QRect(219, 29, 20, 30))
        self.left_column_frame.setFrameShape(QFrame.StyledPanel)
        self.left_column_frame.setFrameShadow(QFrame.Raised)
        self.left_column_layout = QVBoxLayout(self.left_column_frame)
        self.left_column_layout.setObjectName(u"left_column_layout")
        self.left_column = PyLeftColumn(self.left_column_frame)
        self.left_column.setObjectName(u"left_column")

        self.left_column_layout.addWidget(self.left_column)

        self.right_app_frame = QFrame(self.window)
        self.right_app_frame.setObjectName(u"right_app_frame")
        self.right_app_frame.setGeometry(QRect(479, 29, 331, 571))
        self.right_app_frame.setFrameShape(QFrame.StyledPanel)
        self.right_app_frame.setFrameShadow(QFrame.Raised)
        self.right_app_layout = QVBoxLayout(self.right_app_frame)
        self.right_app_layout.setObjectName(u"right_app_layout")
        self.right_app_layout.setContentsMargins(-1, -1, -1, 50)
        self.title_bar_frame = QFrame(self.right_app_frame)
        self.title_bar_frame.setObjectName(u"title_bar_frame")
        self.title_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.title_bar_frame.setFrameShadow(QFrame.Raised)
        self.title_bar_layout = QVBoxLayout(self.title_bar_frame)
        self.title_bar_layout.setObjectName(u"title_bar_layout")
        self.title_bar = PyTitleBar(self.title_bar_frame)
        self.title_bar.setObjectName(u"title_bar")

        self.title_bar_layout.addWidget(self.title_bar)


        self.right_app_layout.addWidget(self.title_bar_frame)

        self.content_area_frame = QFrame(self.right_app_frame)
        self.content_area_frame.setObjectName(u"content_area_frame")
        self.content_area_frame.setFrameShape(QFrame.StyledPanel)
        self.content_area_frame.setFrameShadow(QFrame.Raised)
        self.content_area_layout = QHBoxLayout(self.content_area_frame)
        self.content_area_layout.setObjectName(u"content_area_layout")
        self.right_column_frame = QFrame(self.content_area_frame)
        self.right_column_frame.setObjectName(u"right_column_frame")
        self.right_column_frame.setFrameShape(QFrame.StyledPanel)
        self.right_column_frame.setFrameShadow(QFrame.Raised)
        self.content_area_right_layout = QVBoxLayout(self.right_column_frame)
        self.content_area_right_layout.setObjectName(u"content_area_right_layout")
        self.content_area_right_bg_frame = QFrame(self.right_column_frame)
        self.content_area_right_bg_frame.setObjectName(u"content_area_right_bg_frame")
        self.content_area_right_bg_frame.setFrameShape(QFrame.StyledPanel)
        self.content_area_right_bg_frame.setFrameShadow(QFrame.Raised)

        self.content_area_right_layout.addWidget(self.content_area_right_bg_frame)


        self.content_area_layout.addWidget(self.right_column_frame)

        self.content_area_left_frame = QFrame(self.content_area_frame)
        self.content_area_left_frame.setObjectName(u"content_area_left_frame")
        self.content_area_left_frame.setFrameShape(QFrame.StyledPanel)
        self.content_area_left_frame.setFrameShadow(QFrame.Raised)

        self.content_area_layout.addWidget(self.content_area_left_frame)


        self.right_app_layout.addWidget(self.content_area_frame)

        self.credits_frame = QFrame(self.right_app_frame)
        self.credits_frame.setObjectName(u"credits_frame")
        self.credits_frame.setFrameShape(QFrame.StyledPanel)
        self.credits_frame.setFrameShadow(QFrame.Raised)
        self.credits_layout = QVBoxLayout(self.credits_frame)
        self.credits_layout.setObjectName(u"credits_layout")
        self.credits = PyCredits(self.credits_frame)
        self.credits.setObjectName(u"credits")

        self.credits_layout.addWidget(self.credits)


        self.right_app_layout.addWidget(self.credits_frame)

        self.popup_notification_container = PyPopupNotification(self.right_app_frame)
        self.popup_notification_container.setObjectName(u"popup_notification_container")
        self.popup_notification_container.setStyleSheet(u"#popup_notification_container{\n"
"	background-color: rgb(85, 0, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"#popup_notification_subcontainer{\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        self.popup_notification_container_layout = QVBoxLayout(self.popup_notification_container)
        self.popup_notification_container_layout.setObjectName(u"popup_notification_container_layout")
        self.popup_notification_subcontainer = QWidget(self.popup_notification_container)
        self.popup_notification_subcontainer.setObjectName(u"popup_notification_subcontainer")
        self.popup_notification_subcontainer_layout = QVBoxLayout(self.popup_notification_subcontainer)
        self.popup_notification_subcontainer_layout.setObjectName(u"popup_notification_subcontainer_layout")
        self.list_notification_frame = QFrame(self.popup_notification_subcontainer)
        self.list_notification_frame.setObjectName(u"list_notification_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_notification_frame.sizePolicy().hasHeightForWidth())
        self.list_notification_frame.setSizePolicy(sizePolicy)
        self.list_notification_frame.setFrameShape(QFrame.StyledPanel)
        self.list_notification_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.list_notification_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title_notification = QLabel(self.list_notification_frame)
        self.title_notification.setObjectName(u"title_notification")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title_notification.sizePolicy().hasHeightForWidth())
        self.title_notification.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setBold(True)
        self.title_notification.setFont(font)
        self.title_notification.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.title_notification)

        self.btn_close_notification = QPushButton(self.list_notification_frame)
        self.btn_close_notification.setObjectName(u"btn_close_notification")
        self.btn_close_notification.setMinimumSize(QSize(24, 24))
        self.btn_close_notification.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_close_notification, 0, Qt.AlignRight)


        self.popup_notification_subcontainer_layout.addWidget(self.list_notification_frame)

        self.label_list = QLabel(self.popup_notification_subcontainer)
        self.label_list.setObjectName(u"label_list")
        self.label_list.setFont(font)

        self.popup_notification_subcontainer_layout.addWidget(self.label_list)


        self.popup_notification_container_layout.addWidget(self.popup_notification_subcontainer)


        self.right_app_layout.addWidget(self.popup_notification_container)


        self.central_widget_layout.addWidget(self.window)

        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_notification.setText(QCoreApplication.translate("MainWindow", u"Titulo", None))
        self.btn_close_notification.setText("")
        self.label_list.setText(QCoreApplication.translate("MainWindow", u"Lista lista", None))
    # retranslateUi

