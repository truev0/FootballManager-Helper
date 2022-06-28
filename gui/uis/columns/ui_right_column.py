# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtWidgets import QVBoxLayout, QFrame, QStackedWidget, QWidget, QHBoxLayout, \
    QSizePolicy, QSpacerItem, QScrollArea

from PySide6.QtCore import QSize, Qt, QMetaObject, QCoreApplication


class Ui_RightColumn(object):
    def setupUi(self, RightColumn):
        if not RightColumn.objectName():
            RightColumn.setObjectName(u"RightColumn")
        RightColumn.resize(240, 600)
        self.main_pages_layout = QVBoxLayout(RightColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(RightColumn)
        self.menus.setObjectName(u"menus")
        self.menus.setStyleSheet(
            '''
            QScrollBar::vertical {
            border: none;
            background-color: #2c313c;
            width: 8px;
            margin: 21px 0 21px 0;
            border-radius: 0px;
            }
            QScrollBar::handle:vertical {
            background: #568af2;
            min-height: 25px;
            border-radius: 4px
            }
            QScrollBar::add-line:vertical {
            border: none;
            background: #272c36;
            height: 20px;
            border-bottom-left-radius: 4px;
            border-bottom-right-radius: 4px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
            }
            QScrollBar::sub-line:vertical {
            border: none;
            background: #272c36;
            height: 20px;
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
            subcontrol-position: top;
            subcontrol-origin: margin;
            }
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
            background: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
            }
            '''
        )
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.verticalLayout = QVBoxLayout(self.menu_1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"vertical_layout_menu_1")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)

        self.btn_1_frame = QFrame(self.menu_1)
        self.btn_1_frame.setObjectName(u"btn_1_frame")
        self.btn_1_frame.setMinimumSize(QSize(0, 40))
        self.btn_1_frame.setMaximumSize(QSize(16777215, 40))
        self.btn_1_frame.setFrameShape(QFrame.NoFrame)
        self.btn_1_frame.setFrameShadow(QFrame.Raised)
        self.btn_1_menu_1_layout = QVBoxLayout(self.btn_1_frame)
        self.btn_1_menu_1_layout.setSpacing(0)
        self.btn_1_menu_1_layout.setObjectName(u"btn_1_menu_1_layout")
        self.btn_1_menu_1_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.btn_1_frame)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)
        self.scroll_area_1 = QScrollArea()

        self.scroll_area_1.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_1.setWidgetResizable(True)
        self.scroll_area_1.setStyleSheet("background-color: #2c313c; border-style: none; border-top-left-radius: 8px; border-bottom-left-radius: 8px;")

        self.verticalLayout.addWidget(self.scroll_area_1)

        self.menus.addWidget(self.menu_1)
        self.menu_2 = QWidget()
        self.menu_2.setObjectName(u"menu_2")
        self.verticalLayout_2 = QVBoxLayout(self.menu_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)

        self.btn_2_frame = QFrame(self.menu_2)
        self.btn_2_frame.setObjectName(u"btn_2_frame")
        self.btn_2_frame.setMinimumSize(QSize(0, 40))
        self.btn_2_frame.setMaximumSize(QSize(16777215, 40))
        self.btn_2_frame.setFrameShape(QFrame.NoFrame)
        self.btn_2_frame.setFrameShadow(QFrame.Raised)
        self.btn_1_menu_2_layout = QVBoxLayout(self.btn_2_frame)
        self.btn_1_menu_2_layout.setSpacing(0)
        self.btn_1_menu_2_layout.setObjectName(u"btn_1_menu_2_layout")
        self.btn_1_menu_2_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.btn_2_frame)

        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.scroll_area_2 = QScrollArea()
        self.scroll_area_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_2.setWidgetResizable(True)
        self.scroll_area_2.setStyleSheet("background-color: #2c313c; border-style: none; border-top-right-radius: 8px; border-bottom-right-radius: 8px;")

        self.verticalLayout_2.addWidget(self.scroll_area_2)

        self.menus.addWidget(self.menu_2)

        self.main_pages_layout.addWidget(self.menus)

        self.filter_data_btn_frame = QFrame(RightColumn)
        self.filter_data_btn_frame.setObjectName(u"filter_data_btn_frame")
        self.filter_data_btn_frame.setMinimumSize(QSize(0, 40))
        self.filter_data_btn_frame.setMaximumSize(QSize(16777215, 40))
        self.filter_data_btn_layout = QHBoxLayout(self.filter_data_btn_frame)
        self.filter_data_btn_layout.setSpacing(0)
        self.filter_data_btn_layout.setObjectName(u"filter_data_btn_layout")
        self.filter_data_btn_layout.setContentsMargins(0, 0, 0, 0)

        self.main_pages_layout.addWidget(self.filter_data_btn_frame)


        self.retranslateUi(RightColumn)

        self.menus.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(RightColumn)
    # setupUi

    def retranslateUi(self, RightColumn):
        RightColumn.setWindowTitle(QCoreApplication.translate("RightColumn", u"Form", None))
    # retranslateUi

