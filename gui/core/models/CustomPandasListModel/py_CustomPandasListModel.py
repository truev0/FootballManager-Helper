# IMPORT PSYIDE CORE
# ///////////////////////////////////////////
from pyside_core import *

# IMPORT PACKAGES AND MODULES
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

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable