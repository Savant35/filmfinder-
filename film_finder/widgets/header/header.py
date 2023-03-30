from typing import Optional
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QAbstractButton, QButtonGroup, QFrame, QHBoxLayout, QPushButton, QSizePolicy, QWidget

class Header(QFrame):
    navButtonClicked: pyqtSignal = pyqtSignal(QAbstractButton)

    def __init__(self,parent: Optional[QWidget] = None):
        super().__init__(parent=parent)

        logoButton: QPushButton = QPushButton("FILMFINDER+")
        logoButton.setObjectName("logoButton")
        newButton: QPushButton = QPushButton("New")
        moviesButton: QPushButton = QPushButton("Movies")
        seriesButton: QPushButton = QPushButton("Series")
        searchButton: QPushButton = QPushButton()
        searchButton.setIcon(QIcon("film_finder/widgets/header/assets/search.png"))

        leftFrame: QFrame = QFrame()
        rightFrame: QFrame = QFrame()

        buttonGroup: QButtonGroup = QButtonGroup()
        buttonGroup.addButton(logoButton)
        buttonGroup.addButton(newButton)
        buttonGroup.addButton(moviesButton)
        buttonGroup.addButton(seriesButton)
        buttonGroup.addButton(searchButton)

        buttonGroup.buttonClicked.connect(self.navButtonClicked)
        leftFrameLayout: QHBoxLayout = QHBoxLayout(leftFrame)
        leftFrameLayout.addWidget(logoButton)
        leftFrameLayout.addWidget(newButton)
        leftFrameLayout.addWidget(moviesButton)
        leftFrameLayout.addWidget(seriesButton)
        leftFrameLayout.setContentsMargins(0,0,0,0)
        leftFrameLayout.setSpacing(10)
        leftFrameLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        rightFrameLayout: QHBoxLayout = QHBoxLayout(rightFrame)
        rightFrameLayout.addWidget(searchButton)
        rightFrameLayout.setAlignment(Qt.AlignmentFlag.AlignRight)
        rightFrameLayout.setContentsMargins(10,0,0,0)
        rightFrameLayout.setSpacing(0)

        headerLayout: QHBoxLayout = QHBoxLayout(self)
        headerLayout.addWidget(leftFrame)
        headerLayout.addWidget(rightFrame)
        headerLayout.setContentsMargins(0,0,0,0)
        headerLayout.setSpacing(0)

        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding,QSizePolicy.Policy.Fixed)

