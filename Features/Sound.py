from PyQt6.QtMultimedia import *
from PyQt6.QtCore import *

def playsound(sprite):
    """FAAAAHHHH"""
    effect = QSoundEffect(sprite)                     # le lecteur (attaché à sprite, sinon supprimé)
    effect.setSource(QUrl.fromLocalFile("Assets/Sound/ABAHATABAh.wav"))
    effect.play()
