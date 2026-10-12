from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from itertools import cycle

# --- Settings ---
BASE     = "Assets/Sprite/Charlie_base.png"
OPEN_MOUTH     = "Assets/Sprite/Charlie_open.png"
THINKING = "Assets/Sprite/Charlie_thinking.png"
SPEED    = 300   # ms entre deux images quand il parle


def render_sprite():
    """Crée la fenêtre de Charlie (sans bordure, transparente, au-dessus)"""
    sprite = QLabel()
    sprite.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
    sprite.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    sprite.setPixmap(QPixmap(BASE))
    return sprite


# --- define_anime ---
def set_image(sprite, image):
    """Affiche une image (BASE, OPEN_MOUTH ou THINKING)"""
    sprite.setPixmap(QPixmap(image))


def talking(sprite, ms):
    """Alterne BASE / OPEN_MOUTH pendant ms, puis revient en BASE"""
    images = cycle([BASE, OPEN_MOUTH])

    timer = QTimer(sprite)
    timer.timeout.connect(lambda: set_image(sprite, next(images)))
    timer.start(SPEED)

    QTimer.singleShot(ms, timer.stop) #Qtimer éxécute les argument, au bout de ms (3s)
    QTimer.singleShot(ms, lambda: set_image(sprite, BASE))


def walk(sprite, x, y, ms):
    """Déplace sprite de x, y pixels en ms millisecondes"""
    anim = QPropertyAnimation(sprite, b"pos", sprite)
    anim.setEndValue(sprite.pos() + QPoint(x, y))
    anim.setDuration(ms)
    anim.start()
