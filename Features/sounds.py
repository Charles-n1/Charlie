from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl

# --- Settings ---
SOUND = "Assets/Sound/ABAHATABAh.wav"


def play_sound(parent):
    """FAAAAHHHH"""
    effect = QSoundEffect(parent)   # attaché à parent, sinon supprimé avant de jouer
    effect.setSource(QUrl.fromLocalFile(SOUND))
    effect.play()
