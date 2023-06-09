from typing import Optional
from PyQt6.QtCore import QModelIndex
from PyQt6.QtWidgets import  QAbstractButton, QFrame, QGridLayout,  QMainWindow, QStackedWidget, QWidget
from film_finder.screens.tvshows.tvscreen import TVScreen
from film_finder.widgets import Header
from film_finder.widgets import Sidebar
from ..home import HomeScreen
from ..movie import MovieScreen
from ..detail import DetailScreen

class Window(QMainWindow):

    def __init__(self,parent: Optional[QWidget] = None):
        super().__init__(parent=parent)

        header: Header = Header()
        home: HomeScreen = HomeScreen()
        movie : MovieScreen= MovieScreen()
        tv: TVScreen = TVScreen()
        detail: DetailScreen = DetailScreen()

        self.mainStackWidget: QStackedWidget = QStackedWidget()
        windowFrame: QFrame = QFrame()

        #header.moviesButton.clicked.connect(self.loadHome)
        header.navButtonClicked.connect(self.onNavButtonclick)
        home.filmClicked.connect(detail.onFilmclicked)
        home.filmClicked.connect(self.onFilmclicked)
        movie.filmClicked.connect(detail.onFilmclicked)
        movie.filmClicked.connect(self.onFilmclicked)
        tv.filmClicked.connect(detail.onFilmclicked)
        tv.filmClicked.connect(self.onFilmclicked)
        

        windowFrameLayout: QGridLayout = QGridLayout(windowFrame)
        windowFrameLayout.addWidget(header,0,0,1,1)
        windowFrameLayout.addWidget(self.mainStackWidget,1,0,1,1)
        #windowFrameLayout.setSpacing(30)

        self.mainStackWidget.addWidget(home)
        self.mainStackWidget.addWidget(movie)
        self.mainStackWidget.addWidget(tv)
        self.mainStackWidget.addWidget(detail)
        self.mainStackWidget.setCurrentIndex(0)


        self.setCentralWidget(windowFrame)
        self.setContentsMargins(10,10,10,10)
        self.loadStylesheet()
        self.setWindowTitle("Filmfinder+")

    def onNavButtonclick(self,button: QAbstractButton):
        if button.text().lower() == "home":
            self.mainStackWidget.setCurrentIndex(0)
        elif button.text().lower() == "movies":
            self.mainStackWidget.setCurrentIndex(1)
        else:
            self.mainStackWidget.setCurrentIndex(2)

    def onFilmclicked(self,index: QModelIndex):
        self.mainStackWidget.setCurrentIndex(3)
        
    def loadHome(self):
        self.mainStackWidget.setCurrentIndex(0)

    def loadStylesheet(self):
        with open("film_finder/screens/window/window.qss","r") as f:
            self.setStyleSheet(f.read())
