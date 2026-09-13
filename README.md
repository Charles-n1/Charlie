# Charlie
Un assistant en tant réel sur le pc

## How to use ?
```bash
python3 Conversation.py
```

## How to install ?:

Ubuntu:
1) Installer ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
2) Le modèle
```bash
ollama pull qwen3.5:0.8b
ollama list #to confirm
```

3) Installer de quoi l'éxécuter en code.
```bash
sudo apt install python3 #If not installed
python3 -m venv .venv
source .venv/bin/activate
pip install ollama
pip install PyQt6
```

Ou

```bash
curl -fsSL https://ollama.com/install.sh | sh && \
ollama pull qwen3.5:0.8b && \
sudo apt install -y python3 python3-venv && \
python3 -m venv .venv && \
source .venv/bin/activate && \
pip install ollama PyQt6
```

Windows:

0) Requierement
Télécharger le repo et l'avoir extrait le fichier et y être dedans (pour les trois prochaines commandes).

1) Copier coller (puis redémarrer powershell)
```powershell
winget install Ollama.Ollama; winget install Python.Python.3.13; Write-Host "n===========> Now, reload powershell to continue the second script (charles-n1) <===========n" -ForegroundColor Green
```

2) Copier coller
```powershell
ollama pull qwen3.5:0.8b; python -m venv .venv; ..venv\Scripts\Activate.ps1; pip install PyQt6 ollama; Write-Host "n===========> everything was successfully installed                        <===========" -ForegroundColor Green; Write-Host "===========> run 'python main.py' to execute                              <===========" -ForegroundColor Green; Write-Host "===========> (ts: c normal si y'a deux lignes d'erreurs en rouge en haut) <===========n" -ForegroundColor Green
```

3) Démarrer (tjrs ds le dossier)
```powershell
python main.py
```
