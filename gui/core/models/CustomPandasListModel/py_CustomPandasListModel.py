# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////
from PySide6.QtCore import QAbstractTableModel, Qt

# IMPORT OTHER PACKAGES AND MODULES
# ///////////////////////////////////////////
from past.builtins import unicode
import pandas as pd


# CUSTOM LIST MODEL FOR PANDAS
# ///////////////////////////////////////////
class CustomListModel(QAbstractTableModel):
    def __init__(self, data: pd.DataFrame, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data = data

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]

            if isinstance(value, str):
                return '%s' % value

            return unicode(value)
        return None

    def rowCount(self, parent=None):  # skipcq: PYL-W0613
        return self._data.shape[0]

    def columnCount(self, parent=None):  # skipcq: PYL-W0613
        return self._data.shape[1]

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])
        return None

    def flags(self, index):  # skipcq: PYL-W0613 PYL-R0201
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable
