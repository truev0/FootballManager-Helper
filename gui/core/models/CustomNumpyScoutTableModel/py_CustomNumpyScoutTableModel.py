# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////
from PySide6.QtCore import QAbstractTableModel, Qt

# IMPORT OTHER PACKAGES AND MODULES
# ///////////////////////////////////////////
from past.builtins import unicode
import numpy as np


# CUSTOM TABLE MODEL FOR PANDAS
# ///////////////////////////////////////////
class CustomizedNumpyScoutModel(QAbstractTableModel):
    """It's a subclass of QAbstractTableModel that provides a model for a table view"""

    def __init__(self, data, parent=None):
        """
        The function takes a pandas dataframe as input, converts it to a numpy array, and stores the array and
        the column names as class attributes

        :param data: This is the data that will be displayed in the table
        :param parent: The parent of the model
        """
        QAbstractTableModel.__init__(self, parent)
        self._data = np.array(data.values)
        self._cols = data.columns
        self.insensitive = data.columns.values
        self.r, self.c = np.shape(self._data)

    def data(self, index, role=Qt.DisplayRole):
        """
        If the role is DisplayRole, then return the value of the data at the given index, formatted as a string

        :param index: The index of the item to return data for
        :param role: The role of the data to be displayed
        :return: The data is being returned.
        """
        if role == Qt.DisplayRole:
            value = self._data[index.row(), index.column()]

            if isinstance(value, float):
                return f'{value:.2f}'

            if isinstance(value, str):
                return f'{value}'

            return unicode(value)
        return None

    def rowCount(self, parent=None):  # skipcq: PYL-W0613
        """
        `rowCount` returns the number of rows in the model

        :param parent: The parent of the item
        :return: The number of rows in the table.
        """
        return self.r

    def columnCount(self, parent=None):  # skipcq: PYL-W0613
        """
        `columnCount` returns the number of columns in the model

        :param parent: The parent of the model index
        :return: The number of columns in the table.
        """
        return self.c

    def headerData(self, p_int, orientation, role):
        """
        If the role is DisplayRole and the orientation is Horizontal, return the column name. If the orientation is
        Vertical, return the row number

        :param p_int: The index of the column or row
        :param orientation: Qt.Horizontal or Qt.Vertical
        :param role: The role is used to indicate what kind of data is being requested
        :return: The data is being returned.
        """
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._cols[p_int])

            if orientation == Qt.Vertical:
                return p_int
        return None

    def flags(self, index):  # skipcq: PYL-W0613, PYL-R0201
        """
        "Return a set of flags that indicate how the user can interact with the item."

        The flags() function is called by the view whenever it needs to determine how the user can interact with an item in
        the model. The view uses the information to enable or disable user interaction

        :param index: The index of the item to return the flags for
        :return: The flags method returns the item flags for the given index.
        """
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def setData(self, index, value, role=Qt.EditRole):
        """
        If the user enters a value in the table, the function checks if the value is in the list of columns, and if
        it is, it replaces the value in the next column with the name of the column

        :param index: The index of the item being changed
        :param value: The value to be set
        :param role: The role of the data being set
        :return: The return value is a boolean value.
        """
        index_value = None
        based_columns = [6, 8, 10, 12]
        index_no = None
        if role == Qt.EditRole:
            row = index.row()
            column = index.column()
            tmp = str(value)
            if tmp != '':
                if column in based_columns:
                    if column == 6 and tmp.casefold() in [x.casefold() for x in self.insensitive]:
                        for i, element in enumerate([x.casefold() for x in self.insensitive]):
                            if element == tmp.casefold():
                                index_no = i
                                break
                        self._data[row, column + 1] = self._data[row, index_no]
                        self._data[row, column] = self._cols[index_no]
                    elif column in [8, 10, 12]:
                        for x in range(183, 266):
                            if self._data[row, x] == int(tmp):
                                index_value = x
                                break

                        col_name = self._cols[index_value]
                        col_name = col_name.removesuffix('_rank')
                        self._data[row, column + 1] = col_name
                        self._data[row, column] = tmp
                    self.dataChanged.emit(index, index)
                return True
        return False

    def get_dataframe(self):
        """
        It returns the dataframe that is stored in the object
        :return: The dataframe is being returned.
        """
        return self._data
