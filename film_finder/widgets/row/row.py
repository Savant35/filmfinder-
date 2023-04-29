
from typing import Optional
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QVBoxLayout, QWidget
from ..autofitview import AutoFitView

class Row(QFrame):

    def __init__(self,title: str,view: AutoFitView,parent: Optional[QWidget] = None):
        super().__init__(parent=parent)

        rowFrame: QFrame = QFrame()

        tileLabel: QLabel = QLabel(title)

        navFrame: QFrame = QFrame()
        #navFrame.setFrameStyle(QFrame.NoFrame) #pyright: ignore

        leftNavButton: QPushButton = QPushButton()
        leftNavButton.setIcon(QIcon("film_finder/widgets/row/assets/back.png"))
        leftNavButton.setIconSize(QSize(24,24))
        leftNavButton.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)


        righNavButton: QPushButton = QPushButton()
        righNavButton.setIcon(QIcon("film_finder/widgets/row/assets/back-rotated.png"))
        righNavButton.setIconSize(QSize(24,24))
        righNavButton.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)

        righNavButton.clicked.connect(view.scrollRight)
        leftNavButton.clicked.connect(view.scrollLeft)

        navFrameLayout: QHBoxLayout = QHBoxLayout(navFrame)
        navFrameLayout.addWidget(tileLabel)
        navFrameLayout.addWidget(leftNavButton,Qt.AlignmentFlag.AlignRight)
        navFrameLayout.addWidget(righNavButton,Qt.AlignmentFlag.AlignRight)
        navFrameLayout.setContentsMargins(0,0,0,0)
        navFrameLayout.setSpacing(0)

        rowFrameLayout: QVBoxLayout = QVBoxLayout(rowFrame)
        rowFrameLayout.addWidget(navFrame)
        rowFrameLayout.addWidget(view)
        rowFrameLayout.setContentsMargins(0,0,0,0)
        rowFrameLayout.setSpacing(20)

        rowLayout: QHBoxLayout = QHBoxLayout(self)
        rowLayout.setContentsMargins(0,0,0,0)
        rowLayout.setSpacing(0)
        rowLayout.addWidget(rowFrame)
