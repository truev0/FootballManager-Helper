# IMPORT PYSIDE CORE
# ///////////////////////////////////////////
import numpy as np

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////
from past.builtins import unicode

from pyside_core import *


# CUSTOM TABLE MODEL FOR PANDAS
# ///////////////////////////////////////////
class CustomizedNumpyModel(QAbstractTableModel):

    def __init__(self, data, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data = np.array(data.values)
        self._cols = data.columns
        self.r, self.c = np.shape(self._data)

    def data(self, index, role=Qt.DisplayRole):

        if role == Qt.DisplayRole:
            value = self._data[index.row(), index.column()]

            if isinstance(value, float):
                return "%.2f" % value

            if isinstance(value, str):
                return "%s" % value

            return unicode(value)

    def rowCount(self, parent=None):
        return self.r

    def columnCount(self, parent=None):
        return self.c

    def headerData(self, p_int, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._cols[p_int])

            if orientation == Qt.Vertical:
                return p_int
        return None

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def setData(self, index, value, role=Qt.EditRole):
        index_value = None
        based_columns = [6, 8, 10, 12]
        if role == Qt.EditRole:
            row = index.row()
            column = index.column()
            tmp = str(value)
            if tmp != "":
                if column in based_columns:
                    if column == 6 and tmp in self._cols:
                        index_no = np.where(self._cols == tmp)[0][0]
                        self._data[row, column + 1] = self._data[row, index_no]
                        self._data[row, column] = tmp
                    elif column in [8, 10, 12]:
                        for x in range(97, 181):
                            if self._data[row, x] == int(tmp):
                                index_value = x
                                break

                        col_name = self._cols[index_value]
                        col_name = col_name.removesuffix("_rank")
                        self._data[row, column + 1] = col_name
                        self._data[row, column] = tmp
                    self.dataChanged.emit(index, index)
                return True
        return False
