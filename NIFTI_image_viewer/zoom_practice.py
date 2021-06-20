'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyApp(QWidget):

    def __init__(self, *args):
        super().__init__(*args)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.button_zoom_in = QPushButton('Zoom IN', self)
        self.button_zoom_in.clicked.connect(self.on_zoom_in)
        self.layout.addWidget(self.button_zoom_in)

        self.button_zoom_out = QPushButton('Zoom OUT', self) 
        self.button_zoom_out.clicked.connect(self.on_zoom_out)
        self.layout.addWidget(self.button_zoom_out)

        self.pixmap = QPixmap('test.jpg')

        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)
        self.label.setGeometry(QtCore.QRect(460, 10, 350, 350))
        self.layout.addWidget(self.label)

        self.scale = 1

        self.show()

    def on_zoom_in(self, event):
        self.scale *= 2
        self.resize_image()

    def on_zoom_out(self, event):
        self.scale /= 2
        self.resize_image()

    def resize_image(self):
        size = self.pixmap.size()

        scaled_pixmap = self.pixmap.scaled(self.scale * size)

        self.label.setPixmap(scaled_pixmap)
        self.label.setScaledContents(False)

# --- main ---

app = QApplication([])
win = MyApp()
app.exec()
'''
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtGui import QPen, QBrush
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
 
import sys
 
 
 
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.title = "PyQt5 QGraphicView"
        self.top = 200
        self.left = 500
        self.width = 600
        self.height = 500
 
 
        self.InitWindow()
 
 
    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.createGraphicView()
 
        self.show()
 
 
    def createGraphicView(self):
        self.scene  =QGraphicsScene()
        self.greenBrush = QBrush(Qt.green)
        self.grayBrush = QBrush(Qt.gray)
 
        self.pen = QPen(Qt.red)
 
        graphicView = QGraphicsView(self.scene, self)
        graphicView.setGeometry(0,0,600,500)
 
        self.shapes()
 
 
    def shapes(self):
        ellipse = self.scene.addEllipse(20,20, 200,200, self.pen, self.greenBrush)
        rect = self.scene.addRect(-100,-100, 200,200, self.pen, self.grayBrush)
        pixmap = QPixmap('test.jpg')
        image = self.scene.addPixmap(pixmap)
 
        ellipse.setFlag(QGraphicsItem.ItemIsMovable)
        rect.setFlag(QGraphicsItem.ItemIsMovable)
        ellipse.setFlag(QGraphicsItem.ItemIsSelectable)
        image.setFlag(QGraphicsItem.ItemIsMovable)
 
 
 
 
 
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())