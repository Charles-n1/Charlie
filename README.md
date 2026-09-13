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


Windows:
1) Installer ollama et Python
```powershell
winget install Ollama.Ollama
winget install Python.Python.3.13
```

2) Le modèle
```powershell
ollama pull qwen3.5:0.8b
ollama list #to confirm
```

3) Installer de quoi l'éxécuter en code.
```bash
python -m venv .venv
.venv\Scripts\activate
pip install PyQt6 ollama
```