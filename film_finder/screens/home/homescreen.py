
from typing import Optional
from PyQt6.QtCore import QAbstractListModel, Qt
from PyQt6.QtWidgets import QFrame,  QVBoxLayout, QWidget,QGridLayout
from film_finder.widgets import Banner, AutoFitView, Row, sidebar
#from film_finder.tmdb import TMDBListModel
from film_finder.tmdb import TMDBTVListModel
from film_finder.widgets.sidebar.sidebar import Sidebar

class HomeScreen(QFrame):
    
    def __init__(self,parent: Optional[QWidget] = None):
        super().__init__(parent=parent)

        banner: Banner = Banner()
        sidebar = Sidebar()
        
        tmdbModel: QAbstractListModel = TMDBTVListModel()
        view: AutoFitView = AutoFitView()
        view.setWrapping(False)
        #view.setMinimumIconSize(175,int(175 * 1.5))
        #view.setMinimumIconSize(175,int(175 * 1.5))
        view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) 
        view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) 
        view.setModel(tmdbModel)
        row: Row = Row("Popular on Netflix",view)

        homeLayout: QGridLayout = QGridLayout(self)
        homeLayout.addWidget(banner,0,0,1,1)
        homeLayout.addWidget(row,1,0,1,1)
        homeLayout.addWidget(sidebar,0,1,-1,1)
        #homeLayout.addWidget(sidebar,0,1,1,-1,Qt.AlignmentFlag.AlignTop)
        #homeLayout.setColumnStretch(0,6)
        #homeLayout.setColumnStretch(1,5)
        homeLayout.setSpacing(30)



