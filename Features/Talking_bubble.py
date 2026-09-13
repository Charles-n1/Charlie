from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import ollama

# --- Settings ---
WIDTH = 600
HEIGHT = 50
Y = 200
X = 660
CURSOR_COLOR = "#007FFF"
IA = "qwen3.5:0.8b"

def ask_ia(prompt):
    ia_output = ollama.generate(model=IA, prompt=prompt)
    return ia_output["response"]


def define_bar():
    """Create the main bar"""
    bar = QWidget() #crée une barre

    bar.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint) # frameless + onthetopalways
    bar.setGeometry(X, Y, WIDTH, HEIGHT *2)     # Coordonates position of the bar:

    return bar


def define_input(bar):
    """Create text's input field"""
    cursor = QLineEdit(bar) # Barre transparent d'input (rattaché littéralement dans le parent)

    cursor.resize(WIDTH, HEIGHT) # Expand pour faire genre deux barres c'est qu'une

    cursor.setFocus()
    return cursor


def post_input(bar_input):
    """Récupère, et efface le contenu de la barre"""
    text = bar_input.text()         # récupère

    bar_input.clear()               # vide tout
    return text


def output(bar_input, bar_output):
    """Put IA output into bar_output (pour faire genre c'est une seule bar)"""
    txt = post_input(bar_input)

    ia_output(bar_output, ask_ia(txt)) # Put ia output into the bar

def ia_output(text_area, text):
    return text_area.setText(text) #transforme le tecte de l'ia en texte sur la fenête

def define_output(bar):
    """Create output bar"""
    label = QLabel(bar) # une barre d'output (on peut pas écrire)

    label.setGeometry(0, HEIGHT, WIDTH, HEIGHT)

    return label

# def talking_bubble(): #Example main (executable normally)
#     app = QApplication([])
#     bar = define_bar()
#     bar_input = define_input(bar)
#     bar_output = define_output(bar)

#     # Keybind
#     QShortcut(QKeySequence("Return"), bar, lambda: output(bar_input, bar_output)) # (Return == Enter)
#     # QShortcut(QKeySequence("Escape"), bar, app.quit) # lambda event + () pour limiter les fonctions à plus dd'1 truc de merde

#     bar.show()
#     app.exec()

# # if __name__ == "__main__":
# #     main()