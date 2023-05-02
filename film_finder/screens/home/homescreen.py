
from typing import Optional
from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt, pyqtSignal
from PyQt6.QtWidgets import QFrame, QScrollArea,  QVBoxLayout, QWidget,QGridLayout
from film_finder.widgets import Banner, AutoFitView, Row
from film_finder.tmdb import TMDBTVListModel
from film_finder.widgets.sidebar.sidebar import Sidebar

class HomeScreen(QFrame):
    filmClicked: pyqtSignal = pyqtSignal(QModelIndex)
    
    def __init__(self,parent: Optional[QWidget] = None):
        super().__init__(parent=parent)

        banner: Banner = Banner()
        sidebar = Sidebar()

        scrollArea = QScrollArea()
        scrollFrame = QFrame()
        scrollFrame.setObjectName("scrollFrame")
        scrollArea.setWidget(scrollFrame)
        scrollArea.setWidgetResizable(True)
        scrollArea.horizontalScrollBar().setDisabled(True)
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) 
        
        
        tmdbModel: QAbstractListModel = TMDBTVListModel("popular")
        view: AutoFitView = AutoFitView()
        view.setWrapping(False)
        #view.setMinimumIconSize(175,int(175 * 1.5))
        #view.setMinimumIconSize(175,int(175 * 1.5))
        view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) 
        view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) 
        view.setModel(tmdbModel)
        row: Row = Row("Popular TV Shows",view)
 
        tmdbModel2: QAbstractListModel = TMDBTVListModel("airing_today")
        view2: AutoFitView = AutoFitView()
        view2.setWrapping(False)
        #view.setMinimumIconSize(175,int(175 * 1.5))
        #view.setMinimumIconSize(175,int(175 * 1.5))
        view2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) 
        view2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) 
        view2.setModel(tmdbModel2)
        row2: Row = Row("Airing Today",view2)

        view.clicked.connect(self.filmClicked)
        view2.clicked.connect(self.filmClicked)
        sidebar.filmClicked.connect(self.filmClicked)

        homeLayout: QGridLayout = QGridLayout(scrollFrame)
        homeLayout.addWidget(banner,0,0,1,1)
        homeLayout.addWidget(row,1,0,1,1)
        homeLayout.addWidget(row2,2,0,1,1)
        homeLayout.addWidget(sidebar,0,1,-1,1)
        #homeLayout.addWidget(sidebar,0,1,1,-1,Qt.AlignmentFlag.AlignTop)
        #homeLayout.setColumnStretch(0,6)
        #homeLayout.setColumnStretch(1,5)
        homeLayout.setSpacing(30)

        mainframeLayout = QVBoxLayout(self)
        mainframeLayout.addWidget(scrollArea)




