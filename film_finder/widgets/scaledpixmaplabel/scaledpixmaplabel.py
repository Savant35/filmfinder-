from typing import Optional
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel, QSizePolicy

class ScaledPixmapLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setScaledContents(False)
        self.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.originalPixmap: Optional[QPixmap] = None

        sizePolicy: QSizePolicy = self.sizePolicy()
        sizePolicy.setHorizontalPolicy(QSizePolicy.Policy.Ignored)
        sizePolicy.setHeightForWidth(True)
        sizePolicy.setVerticalPolicy(QSizePolicy.Policy.Fixed)
        self.setSizePolicy(sizePolicy)


    def setPixmap(self, a0: QPixmap) -> None:
        self.originalPixmap = a0
        return super().setPixmap(a0)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        if self.originalPixmap:
            return int(width / self.originalPixmap.width() * self.originalPixmap.height())
        return self.height()

    def resizeEvent(self, event):
        if self.originalPixmap is not None:
            #pixmapCopy: QPixmap = QPixmap(self.originalImage)
            scaledPixmap = self.originalPixmap.scaledToWidth(
                self.width(), Qt.TransformationMode.SmoothTransformation)
            super().setPixmap(scaledPixmap)
        #super().resizeEvent(event)

