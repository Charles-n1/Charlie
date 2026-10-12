from Features.inputs import *
from Features.output import *
from Features.sprites import *
from Features.sounds import *


def on_enter(sprite, field, label):
    """Entrée : thinking, l'IA répond, puis talking 3 s"""
    set_image(sprite, THINKING)
    sprite.repaint()                  # affiche thinking tout de suite (l'IA bloque après)

    label.setText(ask_ia(field.text()))
    field.clear()
    talking(sprite, 3000)


def app():
    qt_app = QApplication([])

    sprite = render_sprite()
    bar, field = speech_bubble()
    label = output_bar(bar)

    key_enter(bar, lambda: on_enter(sprite, field, label))
    key_escape(bar, qt_app)

    sprite.show()
    bar.show()
    qt_app.exec()


if __name__ == "__main__":
    app()
