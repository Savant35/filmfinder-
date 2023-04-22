from typing import List
from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt
from PyQt6.QtGui import QColor, QIcon, QPixmap
from tmdbv3api import TV, Discover, Movie, TMDb, Trending

class TMDBListModel(QAbstractListModel):

    def __init__(self,tmdb =  None,batch: int = 30, parent=None,):
        super().__init__(parent)
        #self.placeHolderPixmap: QPixmap = QPixmap(600,int(600 * 1.5))
        #self.placeHolderPixmap.fill(QColor("#7c859E"))
        self.placeHolderPixmap: QPixmap = QPixmap("film_finder/tmdb/assets/queengambitposter.jpg")
        self.media: List = []

    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self.media)

    def index(self, row: int, column: int, parent: QModelIndex = QModelIndex()) -> QModelIndex:
        if  row < 0 or row >= len(self.media):
            return QModelIndex()
        return self.createIndex(row, column)

    def clear(self):
        self.beginResetModel()
        self.media.clear()
        self.endResetModel()

