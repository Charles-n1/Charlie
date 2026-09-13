from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from itertools import cycle

# --- Settings ---
TALKING_SHEET     = ["Sprite/Charlie_base.png", "Sprite/Charlie_open.png"]
THINKING_SHEET     = "Sprite/Charlie_thinking.png"
BASE_SHEET     = "Sprite/Charlie_base.png"
FRAMELESS   = Qt.WindowType.FramelessWindowHint
TRANSPARENT = Qt.WidgetAttribute.WA_TranslucentBackground
SPEED = 300

def define_sprite():
    """Create the sprite"""
    sprite = QLabel()

    sprite.setWindowFlags(FRAMELESS)
    sprite.setAttribute(TRANSPARENT)
    image = QPixmap("Sprite/Charlie_base.png")   # 1. je charge le fichier
    sprite.setPixmap(image)                      # 2. je le colle dans le label

    return sprite

def next_image(sprite, images):                       # 2. vraie fonction (à la place du lambda)
    sprite.setPixmap(QPixmap(next(images)))

def talking_animation(sprite):
    """Set talking animation"""
    images = cycle(TALKING_SHEET)                 # 1. base, open, base, open...
    timer = QTimer(sprite)                  # 3. commence le chrono
    timer.start(SPEED)                      # 5. tic toutes les 300 ms

    timer.timeout.connect(lambda: next_image(sprite, images))       # 4. à chaque tic -> next_image


def base_animation(sprite):
    """Set base animation"""
    sprite.setPixmap(QPixmap(BASE_SHEET))

def thinking_animation(sprite):
    """Set thinking animation"""
    sprite.setPixmap(QPixmap(THINKING_SHEET))

def main():
    app = QApplication([])

    sprite = define_sprite()
    # QShortcut(QKeySequence("Escape"), sprite, app.quit)   # Escape -> quitte le programme
    base_animation(sprite)
    thinking_animation(sprite)
    talking_animation(sprite)
    sprite.show()

    app.exec()


# if __name__ == "__main__":
#     main()