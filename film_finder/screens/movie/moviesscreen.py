from typing import Optional
from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import  QFrame, QGridLayout, QScrollArea, QSizePolicy, QVBoxLayout, QWidget
from film_finder import tmdb
from film_finder.tmdb import TMDBDiscoverListModel
from film_finder.widgets import row
from film_finder.widgets.autofitview.autofitview import AutoFitView
from film_finder.widgets.banner.banner import Banner
from film_finder.widgets.row.row import Row



class MovieScreen(QFrame): 
    def __init__(self,parent: Optional [QWidget] = None):
        super().__init__(parent=parent)

        #view = AutoFitView()
        banner = Banner()
        banner.setMaximumHeight(400)

        scrollFrame = QFrame()
        scrollArea = QScrollArea()
        scrollArea.setWidget(scrollFrame)
        scrollArea.setWidgetResizable(True)
        scrollFrame.setObjectName("scrollFrame")


        
        tmdbmodel = TMDBDiscoverListModel("discover_movies",18)
        actionView: AutoFitView = AutoFitView()
        actionView.setWrapping(False)
        actionView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        actionView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        actionView.setModel(tmdbmodel)
        #popularView.setMinimumIconSize(140,int(140 * 1.5))
        actionRow: Row = Row("Action", actionView)

        tmdbmodel2 = TMDBDiscoverListModel("discover_movies",35)
        comedyView: AutoFitView = AutoFitView()
        comedyView.setWrapping(False)
        comedyView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        comedyView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        comedyView.setModel(tmdbmodel2)
        #popularView.setMinimumIconSize(140,int(140 * 1.5))
        comedyRow: Row = Row("comedy", comedyView)

        tmdbmodel3 = TMDBDiscoverListModel("discover_movies",14)
        fantasyView: AutoFitView = AutoFitView()
        fantasyView.setWrapping(False)
        fantasyView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        fantasyView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        fantasyView.setModel(tmdbmodel3)
        #popularView.setMinimumIconSize(140,int(140 * 1.5))
        fantasyRow = Row("Fantasy",fantasyView)

        tmdbmodel4 = TMDBDiscoverListModel("discover_movies",12)
        adventureView: AutoFitView = AutoFitView()
        adventureView.setWrapping(False)
        adventureView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        adventureView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        adventureView.setModel(tmdbmodel4)
        #popularView.setMinimumIconSize(140,int(140 * 1.5))
        adventureRow= Row("Adventure",adventureView)


        tmdbmodel5 = TMDBDiscoverListModel("discover_movies",27)
        horrorview: AutoFitView = AutoFitView()
        horrorview.setWrapping(False)
        horrorview.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        horrorview.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        horrorview.setModel(tmdbmodel5)
        #popularView.setMinimumIconSize(140,int(140 * 1.5))
        horrorRow= Row("Horror",horrorview)

        scrollFrameLayout = QVBoxLayout(scrollFrame)
        scrollFrameLayout.addWidget(banner)
        scrollFrameLayout.addWidget(actionRow)
        scrollFrameLayout.addWidget(comedyRow)
        scrollFrameLayout.addWidget(fantasyRow)
        scrollFrameLayout.addWidget(adventureRow)
        scrollFrameLayout.addWidget(horrorRow)

        mainframeLayout = QVBoxLayout(self)
        mainframeLayout.addWidget(scrollArea)





