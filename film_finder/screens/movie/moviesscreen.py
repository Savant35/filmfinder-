from typing import Optional
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import  QFrame, QGridLayout, QVBoxLayout, QWidget
from film_finder import tmdb
from film_finder.tmdb import TMDBDiscoverListModel
from film_finder.widgets import row
from film_finder.widgets.autofitview.autofitview import AutoFitView
from film_finder.widgets.banner.banner import Banner
from film_finder.widgets.row.row import Row



class MovieScreen(QFrame): 
    def __init__(self,parent: Optional [QWidget] = None):
        super().__init__(parent=parent)

        view = AutoFitView()
        banner = Banner()
        tmdbmodel = TMDBDiscoverListModel("discover_movies",18)
        popularView: AutoFitView = AutoFitView()
        popularView.setWrapping(False)
        popularView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        popularView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        popularView.setModel(tmdbmodel)
        #popularView.setMinimumIconSize(140,int(140 * 1.5))
        popularRow: Row = Row("Popular Movies", popularView)



        movieLayout = QVBoxLayout(self)
        movieLayout.addWidget(banner)
        movieLayout.addWidget(popularRow)




