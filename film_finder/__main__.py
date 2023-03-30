from PyQt6.QtWidgets import QApplication
from film_finder.screens import Window
import sys


def __film_finder__():
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    __film_finder__()

