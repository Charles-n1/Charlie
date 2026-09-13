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
    """Create a bar"""
    bar = QWidget()

    bar.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint) #frameless + onthetopalways
    # Coordonates position of the bar:
    bar.setGeometry(X, Y, WIDTH, HEIGHT *2)

    return bar


def define_cursor(bar):
    """Create text's input field"""
    cursor = QLineEdit(bar) #crée une entrée

    cursor.resize(WIDTH, HEIGHT) #expand la size de l'entrée

    cursor.setFocus()
    return cursor


def post_input(bar_input):
    """Read the typed text, then empty the field"""
    text = bar_input.text()         # récupère
    bar_input.clear()    # vide tout
    return text


def output(cursor, bar_output):
    """Configure IA output"""
    text = post_input(cursor)

    # Create a textzone for display
    ia_output(bar_output, ask_ia(text))

def ia_output(text_area, text):
    return text_area.setText(text) #transforme le tecte de l'ia en texte sur la fenête

def define_bar_output(bar):
    """Create output bar"""
    label = QLabel(bar)

    label.setGeometry(0, HEIGHT, WIDTH, HEIGHT)

    return label

def main():
    app = QApplication([])
    bar = define_bar()
    bar_cursor = define_cursor(bar)
    bar_output = define_bar_output(bar)

    # Keybind
    QShortcut(QKeySequence("Return"), bar, lambda: output(bar_cursor, bar_output)) # (Return == Enter)
    QShortcut(QKeySequence("Escape"), bar, app.quit) # lambda event + () pour limiter les fonctions à plus dd'1 truc de merde

    bar.show()
    app.exec()

if __name__ == "__main__":
    main()