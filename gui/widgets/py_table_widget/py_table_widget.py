

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from pyside_core import *

# IMPORT STYLE
# ///////////////////////////////////////////////////////////////
from .style import style


# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyTableWidget(QTableView):
    def __init__(
        self, 
        radius=8,
        color="#FFF",
        bg_color="#444",
        selection_color="#FFF",
        header_horizontal_color="#333",
        header_vertical_color="#444",
        bottom_line_color="#555",
        grid_line_color="#555",
        scroll_bar_bg_color="#FFF",
        scroll_bar_btn_color="#3333",
        context_color="#00ABE8"
    ):
        super().__init__()
        self.setDragEnabled(True)


        self.set_stylesheet(
            radius,
            color,
            bg_color,
            header_horizontal_color,
            header_vertical_color,
            selection_color,
            bottom_line_color,
            grid_line_color,
            scroll_bar_bg_color,
            scroll_bar_btn_color,
            context_color
        )

    # SET STYLESHEET
    def set_stylesheet(
            self,
            radius,
            color,
            bg_color,
            header_horizontal_color,
            header_vertical_color,
            selection_color,
            bottom_line_color,
            grid_line_color,
            scroll_bar_bg_color,
            scroll_bar_btn_color,
            context_color
    ):
        style_format = style.format(
            _radius=radius,
            _color=color,
            _bg_color=bg_color,
            _header_horizontal_color=header_horizontal_color,
            _header_vertical_color=header_vertical_color,
            _selection_color=selection_color,
            _bottom_line_color=bottom_line_color,
            _grid_line_color=grid_line_color,
            _scroll_bar_bg_color=scroll_bar_bg_color,
            _scroll_bar_btn_color=scroll_bar_btn_color,
            _context_color=context_color
        )
        self.setStyleSheet(style_format)

    def onLeftClick(self, index):
        print('onClick index.row: %s, index.col: %s' % (index.row(), index.column()))

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            index = self.clicked.connect(self.onLeftClick)
            print('onClick index.row: %s, index.col: %s' % (index.row(), index.column()))

# TODO continuar en sacar la info de la tabla