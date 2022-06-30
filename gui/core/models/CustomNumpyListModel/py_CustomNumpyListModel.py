# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////
from PySide6.QtCore import QAbstractTableModel, Qt

# IMPORT OTHER PACKAGES AND MODULES
# ///////////////////////////////////////////
from past.builtins import unicode
import numpy as np


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
                return '%s' % value

            return unicode(value)

    def rowCount(self, parent=None):  # skipcq: PYL-W0613
        return self.r

    def columnCount(self, parent=None):  # skipcq: PYL-W0613
        return self.c

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._cols[section])

            if orientation == Qt.Vertical:
                return section
        return None

    def flags(self, index):  # skipcq: PYL-W0613
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled
