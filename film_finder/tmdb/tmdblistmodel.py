from typing import List
from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt
from PyQt6.QtGui import QColor, QIcon, QPixmap

class TMDBListModel(QAbstractListModel):

    def __init__(self,tmdb =  None,batch: int = 30, parent=None,):
        super().__init__(parent)
        #self.placeHolderPixmap: QPixmap = QPixmap(600,int(600 * 1.5))
        #self.placeHolderPixmap.fill(QColor("#7c859E"))
        self.placeHolderPixmap: QPixmap = QPixmap("film_finder/tmdb/assets/queengambitposter.jpg")

        self.media: List = []


    def rowCount(self, parent=QModelIndex()) -> int:
        #return len(self.media)
        return 10

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole) -> bool: 
        if value is None:
            return False
        if not index.isValid():
            return False
        
        row: int = index.row()

        if row >= len(self.media) or row < 0:
            return False

        if role == Qt.ItemDataRole.DecorationRole: 
            pass

        return False

    def index(self, row: int, column: int, parent: QModelIndex = QModelIndex()) -> QModelIndex:
        if parent.isValid() or row < 0 or row >= len(self.media):
            pass
            #return QModelIndex()
        return self.createIndex(row, column)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole) -> object: 
        if not index.isValid():
            return None
        row: int = index.row()

        if row >= len(self.media) or row < 0:
            pass
            #return None

        if role == Qt.ItemDataRole.DisplayRole: 
            return "The Queen Gambit"

        if role == Qt.ItemDataRole.DecorationRole: 
            return QIcon(self.placeHolderPixmap)

        return None

    def canFetchMore(self, index: QModelIndex) -> bool:
        return False


    def fetchMore(self, index: QModelIndex) -> None:
        pass

    def __appendFilms(self,films):
        if len(films) > 0:
            startRow: int = len(self.media)
            endRow: int = startRow + len(films) -1
            self.beginInsertRows(QModelIndex(), startRow,endRow)
            self.media.extend(films)
            self.endInsertRows()

    def clear(self):
        self.beginResetModel()
        self.media.clear()
        self.endResetModel()

