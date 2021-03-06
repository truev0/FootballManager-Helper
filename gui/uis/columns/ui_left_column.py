# ///////////////////////////////////////////////////////////////
#
# BY: VICTOR CAICEDO
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import QSize, QCoreApplication, QMetaObject

from PySide6.QtWidgets import QVBoxLayout, QWidget, QStackedWidget, QSizePolicy, \
    QSpacerItem


class UiLeftColumn:
    """This class is used to create the left column of the main window"""

    def __init__(self):
        self.btn_8_layout = None
        self.btn_8_widget = None
        self.btn_7_layout = None
        self.btn_7_widget = None
        self.btn_6_layout = None
        self.btn_6_widget = None
        self.menu_2_spacer = None
        self.btn_5_layout = None
        self.btn_5_widget = None
        self.btn_4_layout = None
        self.btn_4_widget = None
        self.vertical_layout_menu_2 = None
        self.menu_2 = None
        self.menu_1_spacer = None
        self.btn_3_layout = None
        self.btn_3_widget = None
        self.btn_2_layout = None
        self.btn_2_widget = None
        self.btn_1_layout = None
        self.btn_1_widget = None
        self.vertical_layout_menu_1 = None
        self.menu_1 = None
        self.menus = None
        self.main_pages_layout = None

    def setupUi(self, LeftColumn):
        """
        Set interface for left column widget

        :param LeftColumn: The name of the widget that will be created
        """
        if not LeftColumn.objectName():
            LeftColumn.setObjectName(u"LeftColumn")
        LeftColumn.resize(240, 600)
        self.main_pages_layout = QVBoxLayout(LeftColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(LeftColumn)
        self.menus.setObjectName(u"menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.vertical_layout_menu_1 = QVBoxLayout(self.menu_1)
        self.vertical_layout_menu_1.setSpacing(5)
        self.vertical_layout_menu_1.setObjectName(u"vertical_layout_menu_1")
        self.vertical_layout_menu_1.setContentsMargins(5, 5, 5, 5)
        self.btn_1_widget = QWidget(self.menu_1)
        self.btn_1_widget.setObjectName(u"btn_1_widget")
        self.btn_1_widget.setMinimumSize(QSize(0, 40))
        self.btn_1_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_1_layout = QVBoxLayout(self.btn_1_widget)
        self.btn_1_layout.setSpacing(0)
        self.btn_1_layout.setObjectName(u"btn_1_layout")
        self.btn_1_layout.setContentsMargins(0, 0, 0, 0)

        self.vertical_layout_menu_1.addWidget(self.btn_1_widget)

        self.btn_2_widget = QWidget(self.menu_1)
        self.btn_2_widget.setObjectName(u"btn_2_widget")
        self.btn_2_widget.setMinimumSize(QSize(0, 40))
        self.btn_2_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_2_layout = QVBoxLayout(self.btn_2_widget)
        self.btn_2_layout.setSpacing(0)
        self.btn_2_layout.setObjectName(u"btn_2_layout")
        self.btn_2_layout.setContentsMargins(0, 0, 0, 0)

        self.vertical_layout_menu_1.addWidget(self.btn_2_widget)

        self.btn_3_widget = QWidget(self.menu_1)
        self.btn_3_widget.setObjectName(u"btn_3_widget")
        self.btn_3_widget.setMinimumSize(QSize(0, 40))
        self.btn_3_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_3_layout = QVBoxLayout(self.btn_3_widget)
        self.btn_3_layout.setSpacing(0)
        self.btn_3_layout.setObjectName(u"btn_3_layout")
        self.btn_3_layout.setContentsMargins(0, 0, 0, 0)

        self.vertical_layout_menu_1.addWidget(self.btn_3_widget)

        self.menu_1_spacer = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vertical_layout_menu_1.addItem(self.menu_1_spacer)

        self.btn_6_widget = QWidget(self.menu_1)
        self.btn_6_widget.setObjectName(u"btn_6_widget")
        self.btn_6_widget.setMinimumSize(QSize(0, 40))
        self.btn_6_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_6_layout = QVBoxLayout(self.btn_6_widget)
        self.btn_6_layout.setSpacing(0)
        self.btn_6_layout.setObjectName(u"btn_6_layout")
        self.btn_6_layout.setContentsMargins(0, 0, 0, 0)

        self.vertical_layout_menu_1.addWidget(self.btn_6_widget)

        self.btn_7_widget = QWidget(self.menu_1)
        self.btn_7_widget.setObjectName(u"btn_7_widget")
        self.btn_7_widget.setMinimumSize(QSize(0, 40))
        self.btn_7_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_7_layout = QVBoxLayout(self.btn_7_widget)
        self.btn_7_layout.setSpacing(0)
        self.btn_7_layout.setObjectName(u"btn_7_layout")
        self.btn_7_layout.setContentsMargins(0, 0, 0, 0)

        self.vertical_layout_menu_1.addWidget(self.btn_7_widget)
        self.btn_8_widget = QWidget(self.menu_1)
        self.btn_8_widget.setObjectName(u"btn_8_widget")
        self.btn_8_widget.setMinimumSize(QSize(0, 40))
        self.btn_8_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_8_layout = QVBoxLayout(self.btn_8_widget)
        self.btn_8_layout.setSpacing(0)
        self.btn_8_layout.setObjectName(u"btn_8_layout")
        self.btn_8_layout.setContentsMargins(0, 0, 0, 0)

        self.vertical_layout_menu_1.addWidget(self.btn_8_widget)

        self.menus.addWidget(self.menu_1)
        self.menu_2 = QWidget()
        self.menu_2.setObjectName(u"menu_2")
        self.vertical_layout_menu_2 = QVBoxLayout(self.menu_2)
        self.vertical_layout_menu_2.setSpacing(5)
        self.vertical_layout_menu_2.setObjectName(u"vertical_layout_menu_2")
        self.vertical_layout_menu_2.setContentsMargins(5, 5, 5, 5)
        self.btn_4_widget = QWidget(self.menu_2)
        self.btn_4_widget.setObjectName(u"btn_4_widget")
        self.btn_4_widget.setMinimumSize(QSize(0, 40))
        self.btn_4_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_4_layout = QVBoxLayout(self.btn_4_widget)
        self.btn_4_layout.setSpacing(0)
        self.btn_4_layout.setObjectName(u"btn_4_layout")
        self.btn_4_layout.setContentsMargins(0, 0, 0, 0)

        self.vertical_layout_menu_2.addWidget(self.btn_4_widget)

        self.btn_5_widget = QWidget(self.menu_2)
        self.btn_5_widget.setObjectName(u"btn_5_widget")
        self.btn_5_widget.setMinimumSize(QSize(0, 40))
        self.btn_5_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_5_layout = QVBoxLayout(self.btn_5_widget)
        self.btn_5_layout.setSpacing(0)
        self.btn_5_layout.setObjectName(u"btn_5_layout")
        self.btn_5_layout.setContentsMargins(0, 0, 0, 0)

        self.vertical_layout_menu_2.addWidget(self.btn_5_widget)

        self.menu_2_spacer = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vertical_layout_menu_2.addItem(self.menu_2_spacer)

        self.menus.addWidget(self.menu_2)

        self.main_pages_layout.addWidget(self.menus)

        self.retranslateUi(LeftColumn)

        self.menus.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(LeftColumn)

    @staticmethod
    def retranslateUi(LeftColumn):
        """
        It sets the window title of the LeftColumn object to the translation of the string "Form" in the context
        "LeftColumn".

        :param LeftColumn: The name of the class that is being created
        """
        LeftColumn.setWindowTitle(QCoreApplication.translate("LeftColumn", u"Form", None))
