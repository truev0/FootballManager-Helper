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
from PySide6.QtCore import QCoreApplication, QMetaObject, QSize
from PySide6.QtWidgets import QStackedWidget, QVBoxLayout, QWidget


class Ui_LeftColumn(object):

    def setupUi(self, LeftColumn):
        if not LeftColumn.objectName():
            LeftColumn.setObjectName("LeftColumn")
        LeftColumn.resize(240, 600)
        self.main_pages_layout = QVBoxLayout(LeftColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName("main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(LeftColumn)
        self.menus.setObjectName("menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName("menu_1")
        self.vertical_layout_menu_1 = QVBoxLayout(self.menu_1)
        self.vertical_layout_menu_1.setSpacing(5)
        self.vertical_layout_menu_1.setObjectName("vertical_layout_menu_1")
        self.vertical_layout_menu_1.setContentsMargins(5, 5, 5, 5)
        self.btn_1_widget = QWidget(self.menu_1)
        self.btn_1_widget.setObjectName("btn_1_widget")
        self.btn_1_widget.setMinimumSize(QSize(0, 40))
        self.btn_1_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_1_layout = QVBoxLayout(self.btn_1_widget)
        self.btn_1_layout.setSpacing(0)
        self.btn_1_layout.setObjectName("btn_1_layout")
        self.btn_1_layout.setContentsMargins(0, 0, 0, 0)

        self.vertical_layout_menu_1.addWidget(self.btn_1_widget)

        self.btn_2_widget = QWidget(self.menu_1)
        self.btn_2_widget.setObjectName("btn_2_widget")
        self.btn_2_widget.setMinimumSize(QSize(0, 40))
        self.btn_2_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_2_layout = QVBoxLayout(self.btn_2_widget)
        self.btn_2_layout.setSpacing(0)
        self.btn_2_layout.setObjectName("btn_2_layout")
        self.btn_2_layout.setContentsMargins(0, 0, 0, 0)

        self.vertical_layout_menu_1.addWidget(self.btn_2_widget)

        self.btn_3_widget = QWidget(self.menu_1)
        self.btn_3_widget.setObjectName("btn_3_widget")
        self.btn_3_widget.setMinimumSize(QSize(0, 40))
        self.btn_3_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_3_layout = QVBoxLayout(self.btn_3_widget)
        self.btn_3_layout.setSpacing(0)
        self.btn_3_layout.setObjectName("btn_3_layout")
        self.btn_3_layout.setContentsMargins(0, 0, 0, 0)

        self.vertical_layout_menu_1.addWidget(self.btn_3_widget)

        self.menus.addWidget(self.menu_1)
        self.menu_2 = QWidget()
        self.menu_2.setObjectName("menu_2")
        self.vertical_layout_menu_2 = QVBoxLayout(self.menu_2)
        self.vertical_layout_menu_2.setSpacing(5)
        self.vertical_layout_menu_2.setObjectName("vertical_layout_menu_2")
        self.vertical_layout_menu_2.setContentsMargins(5, 5, 5, 5)
        self.btn_4_widget = QWidget(self.menu_2)
        self.btn_4_widget.setObjectName("btn_4_widget")
        self.btn_4_widget.setMinimumSize(QSize(0, 40))
        self.btn_4_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_4_layout = QVBoxLayout(self.btn_4_widget)
        self.btn_4_layout.setSpacing(0)
        self.btn_4_layout.setObjectName("btn_4_layout")
        self.btn_4_layout.setContentsMargins(0, 0, 0, 0)

        self.vertical_layout_menu_2.addWidget(self.btn_4_widget)

        self.btn_5_widget = QWidget(self.menu_2)
        self.btn_5_widget.setObjectName("btn_5_widget")
        self.btn_5_widget.setMinimumSize(QSize(0, 40))
        self.btn_5_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_5_layout = QVBoxLayout(self.btn_5_widget)
        self.btn_5_layout.setSpacing(0)
        self.btn_5_layout.setObjectName("btn_5_layout")
        self.btn_5_layout.setContentsMargins(0, 0, 0, 0)

        self.vertical_layout_menu_2.addWidget(self.btn_5_widget)

        self.menus.addWidget(self.menu_2)

        self.main_pages_layout.addWidget(self.menus)

        self.retranslateUi(LeftColumn)

        self.menus.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(LeftColumn)

    # setupUi

    def retranslateUi(self, LeftColumn):
        LeftColumn.setWindowTitle(
            QCoreApplication.translate("LeftColumn", "Form", None))

    # retranslateUi
