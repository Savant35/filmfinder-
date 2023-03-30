
from typing import Optional
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QSizePolicy, QVBoxLayout, QWidget

from ..row import Row
from ..autofitview import AutoFitView
from film_finder.tmdb import TMDBListModel


class Sidebar(QFrame):
    def __init__(self, parent: Optional[QWidget]= None):
        super().__init__(parent=parent)


        episodeTmdbModel: TMDBListModel = TMDBListModel()
        episodeView: AutoFitView = AutoFitView()
        episodeView.setWrapping(False)
        episodeView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) 
        episodeView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) 
        episodeView.setModel(episodeTmdbModel)
        episodeView.setMinimumIconSize(140,int(140 * 1.5))
        episodeRow: Row = Row("New episodes", episodeView)

        continueWatchingTmdbModel: TMDBListModel = TMDBListModel()
        continueWatchingView: AutoFitView = AutoFitView()
        continueWatchingView.setWrapping(False)
        continueWatchingView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) 
        continueWatchingView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) 
        continueWatchingView.setModel(continueWatchingTmdbModel)
        continueWatchingView.setMinimumIconSize(140,int(140 * 1.5))
        continueWatchingRow: Row = Row("Continue watching", continueWatchingView)

        friendsWatchingTmdbModel: TMDBListModel = TMDBListModel()
        friendsWatchingView: AutoFitView = AutoFitView()
        friendsWatchingView.setWrapping(False)
        friendsWatchingView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) 
        friendsWatchingView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) 
        friendsWatchingView.setModel(friendsWatchingTmdbModel)
        friendsWatchingView.setMinimumIconSize(140,int(140 * 1.5))
        friendsWatchingRow: Row = Row("Friends watching", friendsWatchingView)

        sidebarLayout: QVBoxLayout = QVBoxLayout(self)
        sidebarLayout.addWidget(episodeRow)
        sidebarLayout.addWidget(continueWatchingRow)
        sidebarLayout.addWidget(friendsWatchingRow)

        self.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
