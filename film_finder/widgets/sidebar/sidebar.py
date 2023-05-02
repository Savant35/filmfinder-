
from typing import Optional
from PyQt6.QtCore import QModelIndex, Qt, pyqtSignal
from PyQt6.QtWidgets import QFrame, QSizePolicy, QVBoxLayout, QWidget
from film_finder.tmdb.tmdbmovielistmodel import TMDBMovieListModel
from ..row import Row
from ..autofitview import AutoFitView

class Sidebar(QFrame):
    filmClicked: pyqtSignal = pyqtSignal(QModelIndex)

    def __init__(self, parent: Optional[QWidget]= None):
        super().__init__(parent=parent)


        popularTmdbModel = TMDBMovieListModel("popular")
        popularView: AutoFitView = AutoFitView()
        popularView.setWrapping(False)
        popularView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) 
        popularView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) 
        popularView.setModel(popularTmdbModel)
        #popularView.setMinimumIconSize(140,int(140 * 1.5))
        popularRow: Row = Row("Popular Movies", popularView)

        tmdbmodel2 = TMDBMovieListModel("top_rated")
        topratedView: AutoFitView = AutoFitView()
        topratedView.setWrapping(False)
        topratedView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) 
        topratedView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) 
        topratedView.setModel(tmdbmodel2)
        #topratedView.setMinimumIconSize(140,int(140 * 1.5))
        topratedRow: Row = Row("Top Rated Movies", topratedView)

        tmdbmodel3 = TMDBMovieListModel("now_playing")
        nowplayingView: AutoFitView = AutoFitView()
        nowplayingView.setWrapping(False)
        nowplayingView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) 
        nowplayingView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) 
        nowplayingView.setModel(tmdbmodel3)
        #nowplayingView.setMinimumIconSize(140,int(140 * 1.5))
        nowplayingRow: Row = Row("Movies In Theter", nowplayingView)

        popularView.clicked.connect(self.filmClicked)
        topratedView.clicked.connect(self.filmClicked)
        nowplayingView.clicked.connect(self.filmClicked)

        sidebarLayout: QVBoxLayout = QVBoxLayout(self)
        sidebarLayout.addWidget(topratedRow)
        sidebarLayout.addWidget(popularRow)
        sidebarLayout.addWidget(nowplayingRow)
        
