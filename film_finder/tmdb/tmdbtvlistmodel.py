from pickle import TUPLE
from typing import Any, List, Tuple
from PyQt6.QtCore import QAbstractListModel, QModelIndex, QUrl, Qt
from PyQt6.QtGui import QColor, QIcon, QPixmap
from tmdbv3api import TV
from tmdbv3api.as_obj import AsObj
#from .worker import Worker
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest

class TMDBTVListModel(QAbstractListModel):

    def __init__(self,category = "popular", parent=None,):
        super().__init__(parent)
        self.placeHolderPixmap: QPixmap = QPixmap(600,int(600 * 1.5))
        self.placeHolderPixmap.fill(QColor("#7c859E"))
        self.baseImageUrl = "https://www.themoviedb.org/t/p/w185"
        self.category = category
        #self.placeHolderPixmap: QPixmap = QPixmap("film_finder/tmdb/assets/queengambitposter.jpg")
        self.media: List[AsObj] = []
        self.tv = TV()
        self.networkmanager = QNetworkAccessManager()

    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self.media)

    def data(self, index: QModelIndex, role: int = ...) -> Any:
        row = index.row()
        column = index.column()
        if not index.isValid():
            return None
        if row < 0 or row >= self.rowCount():
            return None
        if role == Qt.ItemDataRole.DisplayRole:
            return self.media[row].get("name")
        if role == Qt.ItemDataRole.DecorationRole:
            media = self.media[row]
            if hasattr(media,"poster_pixmap"):
                return media.get("poster_pixmap")
            else:
                poster_path = media.get("poster_path")
                url = self.baseImageUrl 
                if isinstance(poster_path,str):
                    url +=poster_path
                request = QNetworkRequest(QUrl(url))
                reply = self.networkmanager.get(request)
                reply.setProperty("row",row)
                reply.finished.connect(self.imageLoaded)

            return QIcon(self.placeHolderPixmap)
        return None

    def index(self, row: int, column: int, parent: QModelIndex = QModelIndex()) -> QModelIndex:
        if  row < 0 or row >= len(self.media):
            return QModelIndex()
        return self.createIndex(row, column)

    def canFetchMore(self, parent: QModelIndex) -> bool:
        if len(self.media ) > 0:
            currentPage = self.tv.page
            totalPages: str = self.tv.total_pages
            if int(currentPage) < int(totalPages):
                return True
            else:
                return False
        return True

        
    def imageLoaded(self):
        reply = self.sender()
        if isinstance(reply,QNetworkReply):
            if reply.error() == QNetworkReply.NetworkError.NoError:
                data = reply.readAll()
                pixmap = QPixmap()
                pixmap.loadFromData(data) #pyright: ignore
                row: int = reply.property("row")
                media = self.media[row]
                setattr(media,"poster_pixmap",pixmap)
                index = self.index(row,0)
                self.dataChanged.emit(index,index,[Qt.ItemDataRole.DecorationRole])

    def fetchMore(self, parent: QModelIndex) -> None:
        currentPage = 0
        if len(self.media ) > 0:
            currentPage = int(self.tv.page)
        if self.category == "popular":
            response = self.tv.popular(currentPage + 1)
            first = self.rowCount()
            last  = first
            if isinstance(response,list):
                last = len(response) -1 + first
                self.beginInsertRows(parent,first,last)
                self.media.extend(response)
                self.endInsertRows()
            else:
                self.beginInsertRows(parent,first,last)
                self.media.append(response)
                self.endInsertRows()

    def clear(self):
        self.beginResetModel()
        self.media.clear()
        self.endResetModel()

