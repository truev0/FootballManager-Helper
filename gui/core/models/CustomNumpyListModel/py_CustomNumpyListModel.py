# IMPORT PSYIDE CORE
# ///////////////////////////////////////////
import numpy as np

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////
from past.builtins import unicode

from pyside_core import *


# CUSTOM LIST MODEL FOR PANDAS
# ///////////////////////////////////////////
class CustomizedNumpyListModel(QAbstractTableModel):

    def __init__(self, data, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data = np.array(data.values)
        self._cols = data.columns
        self.r, self.c = np.shape(self._data)

    def data(self, index, role=Qt.DisplayRole):

        if role == Qt.DisplayRole:
            value = self._data[index.row(), index.column()]

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
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled
