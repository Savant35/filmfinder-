from typing import Optional
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFrame, QHBoxLayout, QPushButton, QLabel, QSizePolicy, QStackedLayout, QVBoxLayout, QWidget
from ..scaledpixmaplabel import ScaledPixmapLabel

class Banner(QFrame):

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent=parent)

        self.bannerBackgroundLabel: ScaledPixmapLabel = ScaledPixmapLabel()
        pixmap = QPixmap("film_finder/widgets/banner/assets/queengambit.jpg")
        self.bannerBackgroundLabel.setPixmap(pixmap)
        self.bannerBackgroundLabel.setObjectName("bannerLabel")
        #bannerBackgroundLabel.setScaledContents(True)
        titleLabel: QLabel = QLabel("The Queen's Gambit")

        watchNowButton: QPushButton = QPushButton("Watch now")
        watchNowButton.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)

        frontFrame: QFrame = QFrame()
        frontFrame.setObjectName("frontFrame")
        backFrame: QFrame = QFrame()

        frontFrameLayout: QVBoxLayout = QVBoxLayout(frontFrame)
        frontFrameLayout.addWidget(titleLabel)
        frontFrameLayout.addWidget(watchNowButton)
        frontFrameLayout.setContentsMargins(20,0,0,20)
        frontFrameLayout.setSpacing(20)
        frontFrameLayout.setAlignment(Qt.AlignmentFlag.AlignBottom)

        backFrameLayout: QHBoxLayout = QHBoxLayout(backFrame)
        backFrameLayout.addWidget(self.bannerBackgroundLabel)
        backFrameLayout.setContentsMargins(0,0,0,0)
        backFrameLayout.setSpacing(0)

        bannerLayout: QStackedLayout = QStackedLayout(self)
        bannerLayout.addWidget(frontFrame)
        bannerLayout.addWidget(backFrame)
        bannerLayout.setStackingMode(QStackedLayout.StackingMode.StackAll)

        #self.setMinimumWidth(400)

        sizePolicy: QSizePolicy = self.sizePolicy()
        sizePolicy.setHeightForWidth(True)
        sizePolicy.setVerticalPolicy(QSizePolicy.Policy.Fixed)
        self.setSizePolicy(sizePolicy)
    def hasHeightForWidth(self):
        return False

    def heightForWidth(self, width):
        #if self.bannerBackgroundLabel and self.bannerBackgroundLabel.pixmap() is not None:
        #    pass
            #return self.bannerBackgroundLabel.heightForWidth(width)
        return self.height()

