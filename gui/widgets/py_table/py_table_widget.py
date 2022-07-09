# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtWidgets import QTableView

# IMPORT STYLE
# ///////////////////////////////////////////////////////////////
from .style import style


# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyTableWidget(QTableView):
    """It's a QTableView that can be populated with a list of lists"""

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
        """
        `__init__` is a function that takes in a bunch of arguments and sets them as attributes of the class

        :param radius: The radius of the corners of the table, defaults to 8 (optional)
        :param color: The color of the text in the table, defaults to #FFF (optional)
        :param bg_color: The background color of the table, defaults to #444 (optional)
        :param selection_color: The color of the selected row, defaults to #FFF (optional)
        :param header_horizontal_color: The color of the horizontal header, defaults to #333 (optional)
        :param header_vertical_color: The color of the vertical header, defaults to #444 (optional)
        :param bottom_line_color: The color of the bottom line of the table, defaults to #555 (optional)
        :param grid_line_color: The color of the grid lines, defaults to #555 (optional)
        :param scroll_bar_bg_color: The background color of the scroll bar, defaults to #FFF (optional)
        :param scroll_bar_btn_color: The color of the scroll bar button, defaults to #3333 (optional)
        :param context_color: The color of the context menu, defaults to #00ABE8 (optional)
        """
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
        """
        It sets the stylesheet for the table.

        :param radius: the radius of the corners of the table
        :param color: The color of the text in the table
        :param bg_color: background color of the table
        :param header_horizontal_color: The color of the horizontal header
        :param header_vertical_color: The color of the vertical header
        :param selection_color: The color of the selected cell
        :param bottom_line_color: The color of the bottom line of the table
        :param grid_line_color: The color of the grid lines
        :param scroll_bar_bg_color: The background color of the scroll bar
        :param scroll_bar_btn_color: The color of the scroll bar button
        :param context_color: The color of the context menu
        """
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
