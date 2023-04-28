from typing import Optional
from PyQt6.QtCore import  QEasingCurve, QEvent, QPropertyAnimation, QSize, Qt
from PyQt6.QtWidgets import  QListView, QWidget, QAbstractScrollArea

class AutoFitView(QListView):

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent=parent)


        self.iconSizeRatio: float = 1.5
        self.minimumIconSize: QSize = QSize(120,int(120 * 1.5))
        self.animation: QPropertyAnimation = QPropertyAnimation(self.horizontalScrollBar(), b"value") #pyright: ignore
        self.animation.setDuration(300)
        #self.animation.setEasingCurve(QEasingCurve.OutQuad) #pyright: ignore

        self.setLayoutMode(QListView.LayoutMode.Batched)
        self.setViewMode(QListView.ViewMode.IconMode)
        self.setResizeMode(QListView.ResizeMode.Adjust)
        self.setFlow(QListView.Flow.LeftToRight)
        self.setUniformItemSizes(True)
        self.setIconSize(self.minimumIconSize)
        self.setSpacing(5)
        self.setTextElideMode(Qt.TextElideMode.ElideLeft)
        self.setContentsMargins(0,0,0,0)
        self.setWordWrap(True)
        self.viewport().installEventFilter(self)
        self.currentIconSize: QSize = self.iconSize()
        self.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents) #pyright: ignore
        self.resize(QSize(0,0))

    def setMinimumIconSize(self,width: int, height: int):
        self.minimumIconSize.setWidth(width)
        self.minimumIconSize.setHeight(height)

    def setShowAll(self,showAll: bool):
        self.showAll = showAll

    def setIconRatio(self,ratio: float):
        self.iconSizeRatio = ratio

    def sizeHint(self) -> QSize:
        size: QSize = super().sizeHint()
        fontHeight: int = self.fontMetrics().height() * 2
        size.setHeight(self.iconSize().height() + self.frameWidth() * 2 +  fontHeight + self.spacing() + 10) 
        return size

    def minimumSizeHint(self) -> QSize:
            return self.sizeHint()
    def scrollRight(self):
        currentPos = self.horizontalScrollBar().value()
        pageSize = self.horizontalScrollBar().pageStep()
        scrollPos = currentPos + pageSize

        self.animation.stop()
        self.animation.setStartValue(currentPos)
        self.animation.setEndValue(scrollPos)
        self.animation.start()

    def scrollLeft(self):
        currentPos = self.horizontalScrollBar().value()
        pageSize = self.horizontalScrollBar().pageStep()
        scrollPos = currentPos - pageSize

        self.animation.stop()
        self.animation.setStartValue(currentPos)
        self.animation.setEndValue(scrollPos)
        self.animation.start()

    def eventFilter(self, obj, event):
        if obj is self.viewport() and event.type() == QEvent.Type.Resize: #pyright: ignore
            viewport_width = self.viewport().width()
            frameWidth = self.frameWidth()
            itemSpacing = self.spacing() 
            availableWidth = viewport_width - (frameWidth * 2) - (itemSpacing * 2) - self.horizontalScrollBar().width()
            maxItemPerRow = availableWidth // self.minimumIconSize.width() 
            if maxItemPerRow > 1:
                iconWidth = (availableWidth // maxItemPerRow ) - ( itemSpacing) - (frameWidth * 4) 
            else:
                iconWidth = self.minimumIconSize.width() - (itemSpacing ) - (frameWidth * 4) 
            iconHeight = int(iconWidth * self.iconSizeRatio)
            iconSize = QSize(iconWidth,iconHeight) 
            if abs(self.iconSize().width() - iconWidth) > 0:
                self.setIconSize(iconSize)
            return True

        return super().eventFilter(obj, event)
