
from typing import Optional
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame,  QVBoxLayout, QWidget
from film_finder.widgets import Banner, AutoFitView, Row
from film_finder.tmdb import TMDBListModel

class Home(QFrame):
    
    def __init__(self,parent: Optional[QWidget] = None):
        super().__init__(parent=parent)

        banner: Banner = Banner()
        tmdbModel: TMDBListModel = TMDBListModel()
        view: AutoFitView = AutoFitView()
        view.setWrapping(False)
        view.setMinimumIconSize(175,int(175 * 1.5))
        view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) 
        view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) 
        view.setModel(tmdbModel)
        row: Row = Row("Popular on Netflix",view)

        homeLayout: QVBoxLayout = QVBoxLayout(self)
        homeLayout.addWidget(banner,6)
        homeLayout.addWidget(row,4)
        homeLayout.setContentsMargins(0,0,0,0)
        homeLayout.setSpacing(20)




