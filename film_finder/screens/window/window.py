from typing import Optional
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import  QFrame, QGridLayout,  QMainWindow, QStackedLayout, QWidget
from tmdbv3api import Movie
from film_finder.widgets import Header
from film_finder.widgets import Sidebar
from ..home import Home


class Window(QMainWindow):

    def __init__(self,parent: Optional[QWidget] = None):
        super().__init__(parent=parent)

        header: Header = Header()
        sidebar: Sidebar = Sidebar()
        home: Home = Home()
        movie = Movie()



        mainFrame: QFrame = QFrame()
        windowFrame: QFrame = QFrame()

        header.moviesButton.clicked.connect(self.loadHome)

        windowFrameLayout: QGridLayout = QGridLayout(windowFrame)
        windowFrameLayout.addWidget(header,0,0,1,1)
        windowFrameLayout.addWidget(home,1,0,1,1,)
        windowFrameLayout.addWidget(sidebar,0,1,-1,1)
        windowFrameLayout.setColumnStretch(0,6)
        windowFrameLayout.setColumnStretch(1,5)
        windowFrameLayout.setSpacing(30)

        self.mainFrameLayout = QStackedLayout()
        self.mainFrameLayout.addWidget(windowFrame)
        #self.mainFrameLayout.addWidget()
        #self.mainFrameLayout.addWidget(series)
        self.mainFrameLayout.setCurrentIndex(0)
        mainFrame.setLayout(self.mainFrameLayout)


        self.setCentralWidget(mainFrame)
        self.setContentsMargins(10,10,10,10)
        self.loadStylesheet()
        self.setWindowTitle("Filmfinder+")

    def loadHome(self):
        self.mainFrameLayout.setCurrentIndex(1)

    def loadStylesheet(self):
        with open("film_finder/screens/window/window.qss","r") as f:
            self.setStyleSheet(f.read())
