from PyQt6.QtWidgets import *
from Features.inputs import WIDTH, HEIGHT
import ollama

# --- Settings ---
IA = "qwen3.5:0.8b"


def output_bar(bar):
    """Crée la zone de réponse, sous le champ de texte"""
    label = QLabel(bar)
    label.setGeometry(0, HEIGHT, WIDTH, HEIGHT)
    return label


def ask_ia(prompt):
    """Demande à l'IA, renvoie sa réponse"""
    return ollama.generate(model=IA, prompt=prompt, think=False)["response"]
