# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////
from PySide6.QtCore import QAbstractTableModel, Qt

# IMPORT OTHER PACKAGES AND MODULES
# ///////////////////////////////////////////
from past.builtins import unicode
import pandas as pd


# CUSTOM TABLE MODEL FOR PANDAS
# ///////////////////////////////////////////
class CustomizedPandasModel(QAbstractTableModel):
    def __init__(self, data: pd.DataFrame, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data = data

    def data(self, index, role=Qt.DisplayRole):

        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]

            if isinstance(value, float):
                return "%.2f" % value

            if isinstance(value, str):
                return '%s' % value

            return unicode(value)

    def rowCount(self, parent=None):
        return len(self._data.index)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def setData(self, index, value, role=Qt.EditRole):
        index_value = None
        based_columns = [6, 8, 10, 12]
        if role == Qt.EditRole:
            row = index.row()
            column = index.column()
            tmp = str(value)
            if column in based_columns:
                if column == 6 and tmp in self._data.columns.values.tolist():
                    index_no = self._data.columns.get_loc(tmp)
                    self._data.iloc[row, column + 1] = self._data.iloc[row, index_no]
                    self._data.iloc[row, column] = tmp
                elif column in [8, 10, 12]:
                    for x in range(97, 181):
                        if self._data.iloc[row, x] == int(tmp):
                            index_value = x
                            break

                    col_name = self._data.columns[index_value]
                    col_name = col_name.removesuffix('_rank')
                    self._data.iloc[row, column + 1] = col_name
                    self._data.iloc[row, column] = tmp
                self.dataChanged.emit(index, index)
            return True
