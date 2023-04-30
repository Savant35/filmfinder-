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



class TVScreen(QFrame): 
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

    
        
        tmdbmodel = TMDBDiscoverListModel("discover_tv_shows",10759)
        actionView: AutoFitView = AutoFitView()
        actionView.setWrapping(False)
        actionView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        actionView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        actionView.setModel(tmdbmodel)
        #popularView.setMinimumIconSize(140,int(140 * 1.5))
        actionRow: Row = Row("Action and Adventure", actionView)
 
        tmdbmodel = TMDBDiscoverListModel("discover_tv_shows",16)
        animationView: AutoFitView = AutoFitView()
        animationView.setWrapping(False)
        animationView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        animationView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        animationView.setModel(tmdbmodel)
        #popularView.setMinimumIconSize(140,int(140 * 1.5))
        animationRow: Row = Row("Animation", animationView)

        tmdbmodel2 = TMDBDiscoverListModel("discover_tv_shows",35)
        comedyView: AutoFitView = AutoFitView()
        comedyView.setWrapping(False)
        comedyView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        comedyView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        comedyView.setModel(tmdbmodel2)
        #popularView.setMinimumIconSize(140,int(140 * 1.5))
        comedyRow: Row = Row("comedy", comedyView)

        tmdbmodel3 = TMDBDiscoverListModel("discover_tv_shows",10765)
        fantasyView: AutoFitView = AutoFitView()
        fantasyView.setWrapping(False)
        fantasyView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        fantasyView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        fantasyView.setModel(tmdbmodel3)
        #popularView.setMinimumIconSize(140,int(140 * 1.5))
        fantasyRow = Row("Fantasy",fantasyView)

        tmdbmodel4 = TMDBDiscoverListModel("discover_tv_shows",18)
        dramaView: AutoFitView = AutoFitView()
        dramaView.setWrapping(False)
        dramaView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        dramaView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        dramaView.setModel(tmdbmodel4)
        #popularView.setMinimumIconSize(140,int(140 * 1.5))
        dramaRow= Row("Drama",dramaView)


        tmdbmodel5 = TMDBDiscoverListModel("discover_tv_shows",10764)
        realityView: AutoFitView = AutoFitView()
        realityView.setWrapping(False)
        realityView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        realityView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        realityView.setModel(tmdbmodel5)
        #popularView.setMinimumIconSize(140,int(140 * 1.5))
        realityRow= Row("Reality",realityView)
        

        scrollAreaFrameLayout = QVBoxLayout(scrollFrame)
        scrollAreaFrameLayout.addWidget(banner)
        scrollAreaFrameLayout.addWidget(actionRow)
        scrollAreaFrameLayout.addWidget(comedyRow)
        scrollAreaFrameLayout.addWidget(animationRow)
        scrollAreaFrameLayout.addWidget(fantasyRow)
        scrollAreaFrameLayout.addWidget(dramaRow)
        #scrollAreaFrameLayout.addWidget(realityRow)

        mainframeLayout = QVBoxLayout(self)
        mainframeLayout.addWidget(scrollArea)





