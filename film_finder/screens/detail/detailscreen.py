from typing import Optional
from PyQt6.QtCore import QModelIndex, QUrl, Qt, pyqtSignal
from PyQt6.QtGui import QColor, QIcon, QPixmap
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from PyQt6.QtWidgets import QFrame, QHBoxLayout, QPushButton, QLabel, QSizePolicy, QStackedLayout, QVBoxLayout, QWidget

class DetailScreen(QFrame):
    abort: pyqtSignal = pyqtSignal()

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent=parent)

        self.networkManger: QNetworkAccessManager = QNetworkAccessManager()
        #self.baseBackdropUrl: str = "https://www.themoviedb.org/t/p/w1920_and_h800_multi_faces"
        self.baseBackdropUrl: str = "https://www.themoviedb.org/t/p/original"
        self.placeHolderPixmap: QPixmap = QPixmap(1920,1080)
        self.placeHolderPixmap.fill(QColor("#7c859E"))
        self.backdropLabel: QLabel = QLabel()
        self.backdropLabel.setPixmap(self.placeHolderPixmap)
        self.backdropLabel.setSizePolicy(QSizePolicy.Policy.Ignored,QSizePolicy.Policy.Ignored)
        self.backdropLabel.setObjectName("backdropLabel")
        self.titleLabel: QLabel = QLabel()
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.titleLabel.setObjectName("titleLabel")
        self.overViewLabel: QLabel = QLabel()
        self.overViewLabel.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        self.overViewLabel.setMaximumHeight(40)
        self.overViewLabel.setWordWrap(True)
        self.overViewLabel.setObjectName("overviewLabel")
        self.ratingButton: QPushButton = QPushButton()
        ratingPixmap: QPixmap = QPixmap("film_finder/screens/detail/assets/star.png")
        ratingPixmap = ratingPixmap.scaled(24,24)
        self.ratingButton.setIcon(QIcon(ratingPixmap))
        self.ratingButton.setObjectName("ratingButton")


        trailerButton: QPushButton = QPushButton("Trailer")
        trailerButton.setObjectName("trailerButton")
        trailerButton.setIcon(QIcon("film_finder/screens/detail/assets/play.png"))
        trailerButton.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)

        frontFrame: QFrame = QFrame()
        frontFrame.setObjectName("frontFrame")
        backFrame: QFrame = QFrame()

        frontFrameLayout: QVBoxLayout = QVBoxLayout(frontFrame)
        frontFrameLayout.addWidget(self.titleLabel)
        frontFrameLayout.addWidget(self.ratingButton)
        frontFrameLayout.addWidget(self.overViewLabel)
        frontFrameLayout.addWidget(trailerButton)
        frontFrameLayout.setContentsMargins(20,0,0,20)
        frontFrameLayout.setSpacing(20)
        frontFrameLayout.setAlignment(Qt.AlignmentFlag.AlignBottom)

        backFrameLayout: QHBoxLayout = QHBoxLayout(backFrame)
        backFrameLayout.addWidget(self.backdropLabel)
        backFrameLayout.setContentsMargins(0,0,0,0)
        backFrameLayout.setSpacing(0)

        bannerLayout: QStackedLayout = QStackedLayout(self)
        bannerLayout.addWidget(frontFrame)
        bannerLayout.addWidget(backFrame)
        bannerLayout.setStackingMode(QStackedLayout.StackingMode.StackAll)
        self.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
    def onFilmclicked(self,index: QModelIndex):
        title: Optional[str] = index.data()
        rating: Optional[str] = index.siblingAtColumn(1).data()
        overview: Optional[str] = index.siblingAtColumn(2).data()
        backdropUrl: Optional[str] = index.siblingAtColumn(3).data()

        if title is not None:
            self.titleLabel.setText(title)
        if rating is not None:
            self.ratingButton.setText(str(rating))
        if overview is not None:
            self.overViewLabel.setText(overview)
        if backdropUrl is not None:
            self.abort.emit()
            url: str = self.baseBackdropUrl + backdropUrl
            request: QNetworkRequest = QNetworkRequest(QUrl(url))
            reply: QNetworkReply = self.networkManger.get(request)
            reply.finished.connect(self.onBackdropReplyFinished)
            self.abort.connect(reply.abort)

    def onBackdropReplyFinished(self):
        reply = self.sender()
        if isinstance(reply, QNetworkReply):
            if reply.error() == QNetworkReply.NetworkError.NoError:
                data = reply.readAll()
                pixmap = QPixmap()
                pixmap.loadFromData(data) #pyright: ignore
                pixmap = pixmap.scaled(1920,1080)
                self.backdropLabel.setPixmap(pixmap)



