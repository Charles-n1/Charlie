from Features.Animation import *
from Features.Talking_bubble import *

def define():
    """Définit le sprite et la barre"""
    sprite = define_sprite()
    bar = define_bar()
    bar_input = define_input(bar)
    bar_output = define_output(bar)

    return sprite, bar, bar_input, bar_output

def show(sprite, bar):
    """Autorise l'affichage de sprite et de bar (une fois, définitif)"""
    sprite.show()
    bar.show()

def on_enter(sprite, bar_input, bar_output):
    """Animation quand on entre"""
    thinking_animation(sprite)            # 1. Charlie réfléchit
    sprite.repaint()                      # 2. force l'affichage tout de suite
    output(bar_input, bar_output)         # 3. lit l'input, demande à l'IA, affiche la réponse
    talking_animation(sprite, 3000)

def default(sprite, bar_input, bar_output):
    base_animation(sprite)

def main():
    app = QApplication([])

    sprite, bar, bar_input, bar_output = define()

    default(sprite, bar_input, bar_output)
    QShortcut(QKeySequence("Return"), bar, lambda: on_enter(sprite, bar_input, bar_output))
    QShortcut(QKeySequence("Escape"), bar, app.quit)

    show(sprite, bar)
    app.exec() #exec éxécute infiniment toutes les fonctons qui commencent par Q même après la fin de l'éxécution du main

if __name__ == "__main__":
    main()
