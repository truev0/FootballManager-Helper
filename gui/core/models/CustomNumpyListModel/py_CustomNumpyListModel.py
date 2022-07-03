# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////
from PySide6.QtCore import QAbstractTableModel, Qt

# IMPORT OTHER PACKAGES AND MODULES
# ///////////////////////////////////////////
from past.builtins import unicode
import numpy as np


# CUSTOM LIST MODEL FOR PANDAS
# ///////////////////////////////////////////
# It's a model that can be used to display a list of numpy arrays in a QTableView
class CustomizedNumpyListModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        """
        The function takes a pandas dataframe as input, converts it to a numpy array, and stores the array and the column
        names as class attributes

        :param data: This is the data that will be displayed in the table
        :param parent: The parent of the model
        """
        QAbstractTableModel.__init__(self, parent)
        self._data = np.array(data.values)
        self._cols = data.columns
        self.r, self.c = np.shape(self._data)

    def data(self, index, role=Qt.DisplayRole):
        """
        If the role is DisplayRole, then return the value of the data at the given index

        :param index: The index of the item to return data for
        :param role: The role being requested
        :return: The value of the cell.
        """
        if role == Qt.DisplayRole:
            value = self._data[index.row(), index.column()]

            if isinstance(value, str):
                return '%s' % value

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

    def headerData(self, section, orientation, role):
        """
        If the role is DisplayRole, and the orientation is horizontal, return the column name. If the orientation is
        vertical, return the row number

        :param section: The column or row number
        :param orientation: Qt.Horizontal or Qt.Vertical
        :param role: The role is used to indicate what kind of data is requested
        :return: The data is being returned.
        """
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._cols[section])

            if orientation == Qt.Vertical:
                return section
        return None

    def flags(self, index):  # skipcq: PYL-W0613 PYL-R0201
        """
        "Return a set of flags that indicate how the user can interact with the item."

        The flags() function is called by the view to determine how the user can interact with the item. The flags()
        function is called for each item in the model

        :param index: The index of the item in the model
        :return: The flags method returns the item flags for the given index.
        """
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled
