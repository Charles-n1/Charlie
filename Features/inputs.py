from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

# --- Settings ---
WIDTH  = 600
HEIGHT = 50
X      = 660
Y      = 200


def speech_bubble():
    """Crée la bulle : une fenêtre, avec le champ de texte en haut"""
    bar = QWidget()
    bar.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
    bar.setGeometry(X, Y, WIDTH, HEIGHT * 2)   # x2 : le champ + la réponse

    field = QLineEdit(bar)                     # dans bar
    field.resize(WIDTH, HEIGHT)
    field.setFocus()

    return bar, field


def key_escape(bar, app):
    """Échap : quitte"""
    QShortcut(QKeySequence("Escape"), bar, app.quit)


def key_enter(bar, action):
    """Entrée : lance action"""
    QShortcut(QKeySequence("Return"), bar, action)
