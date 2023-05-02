from typing import Any, List, Tuple
from PyQt6.QtCore import QAbstractListModel, QModelIndex, QUrl, Qt
from PyQt6.QtGui import QColor, QIcon, QPixmap
from tmdbv3api import Discover
from tmdbv3api.as_obj import AsObj
#from .worker import Worker
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest

class TMDBDiscoverListModel(QAbstractListModel):

    def __init__(self,endpoint: str,genreId: int, parent=None,):
        super().__init__(parent)
        self.placeHolderPixmap: QPixmap = QPixmap(600,int(600 * 1.5))
        self.placeHolderPixmap.fill(QColor("#7c859E"))
        self.baseImageUrl = "https://www.themoviedb.org/t/p/w185"
        #self.placeHolderPixmap: QPixmap = QPixmap("film_finder/tmdb/assets/queengambitposter.jpg")
        self.media: List[AsObj] = []
        self.discover = Discover()
        self.networkmanager = QNetworkAccessManager()
        self.endpoint = endpoint
        self.genreId = genreId

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
            if column == 0:
                if hasattr(self.media[row],"name"):
                    return self.media[row].get("name")
                else:
                    return self.media[row].get("title")
            elif column == 1:
                return self.media[row].get("vote_average")
            elif column == 2:
                return self.media[row].get("overview")

            elif column == 3:
                return self.media[row].get("backdrop_path")

        if role == Qt.ItemDataRole.DecorationRole:
            media = self.media[row]
            if hasattr(media,"poster_pixmap"):
                return QIcon(media.get("poster_pixmap"))
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

    def sibling(self, row: int, column: int, idx: QModelIndex) -> QModelIndex:
        if row == idx.row():
            return self.index(row,column)
        return QModelIndex()

    def canFetchMore(self, parent: QModelIndex) -> bool:
        #return False
        if len(self.media ) > 0:
            currentPage = self.discover.page
            totalPages: str = self.discover.total_pages
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
            currentPage = int(self.discover.page)
        param = {}
        param["sort_by"] = "popularity.desc"
        param["with_genres"] = self.genreId 
        param["page"] = currentPage+1
        response = getattr(self.discover, self.endpoint)(param)
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
