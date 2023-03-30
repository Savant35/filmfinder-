from typing import Optional
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import  QFrame, QGridLayout,  QMainWindow, QWidget
from film_finder.widgets import Header
from film_finder.widgets import Sidebar
from ..home import Home


class Window(QMainWindow):

    def __init__(self,parent: Optional[QWidget] = None):
        super().__init__(parent=parent)

        header: Header = Header()
        sidebar: Sidebar = Sidebar()
        home: Home = Home()


        mainFrame: QFrame = QFrame()
        windowFrame: QFrame = QFrame()

        windowFrameLayout: QGridLayout = QGridLayout(windowFrame)
        windowFrameLayout.addWidget(header,0,0,1,1)
        windowFrameLayout.addWidget(home,1,0,1,1,)
        windowFrameLayout.addWidget(sidebar,0,1,-1,1)
        windowFrameLayout.setColumnStretch(0,6)
        windowFrameLayout.setColumnStretch(1,5)
        windowFrameLayout.setSpacing(30)
        
        self.setCentralWidget(windowFrame)
        self.setContentsMargins(10,10,10,10)
        self.loadStylesheet()
        self.setWindowTitle("Filmfinder+")

    def loadStylesheet(self):
        with open("film_finder/screens/window/window.qss","r") as f:
            self.setStyleSheet(f.read())
