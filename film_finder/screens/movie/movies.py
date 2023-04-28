from typing import Optional
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import  QFrame, QGridLayout,  QMainWindow, QWidget
from film_finder.widgets import Header
from film_finder.widgets import Sidebar
from film_finder.widgets.autofitview.autofitview import AutoFitView
from film_finder.widgets.row.row import Row
from ..home import Home



class Movie(QFrame):
    def __init__(self, parent: Optional[QWidget]= None):
        super().__init__(parent=parent)

        header = Header()
        view = AutoFitView()
        row1 = Row("popular Movies",view)
        row2 = Row("Comedy",view)
        row3 = Row("Action Movies",view)


        movieLayout = QGridLayout()
        movieLayout.addWidget(header,0,0,0,0)
        movieLayout.addWidget(row1,1,1,1,1)


