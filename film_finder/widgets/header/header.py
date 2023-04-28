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
        self.homeButton: QPushButton = QPushButton("Home")
        self.moviesButton: QPushButton = QPushButton("Movies")
        self.seriesButton: QPushButton = QPushButton("Series")

        leftFrame: QFrame = QFrame()
        rightFrame: QFrame = QFrame()

        buttonGroup: QButtonGroup = QButtonGroup()
        buttonGroup.addButton(logoButton)
        buttonGroup.addButton(self.homeButton)
        buttonGroup.addButton(self.moviesButton)
        buttonGroup.addButton(self.seriesButton)

        buttonGroup.buttonClicked.connect(self.navButtonClicked)
        leftFrameLayout: QHBoxLayout = QHBoxLayout(leftFrame)
        leftFrameLayout.addWidget(logoButton)
        leftFrameLayout.addWidget(self.homeButton)
        leftFrameLayout.addWidget(self.moviesButton)
        leftFrameLayout.addWidget(self.seriesButton)
        leftFrameLayout.setContentsMargins(0,0,0,0)
        leftFrameLayout.setSpacing(10)
        leftFrameLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        rightFrameLayout: QHBoxLayout = QHBoxLayout(rightFrame)
        rightFrameLayout.setAlignment(Qt.AlignmentFlag.AlignRight)
        rightFrameLayout.setContentsMargins(10,0,0,0)
        rightFrameLayout.setSpacing(0)

        headerLayout: QHBoxLayout = QHBoxLayout(self)
        headerLayout.addWidget(leftFrame)
        headerLayout.addWidget(rightFrame)
        headerLayout.setContentsMargins(0,0,0,0)
        headerLayout.setSpacing(0)

        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding,QSizePolicy.Policy.Fixed)

