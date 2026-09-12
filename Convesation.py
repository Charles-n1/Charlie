import tkinter as tk
import ollama

# --- Settings ---
WIDTH = 600
HEIGHT = 50
Y = 200
CURSOR_COLOR = "#007FFF"
IA = "qwen3.5:0.8b"

def ask_ia(prompt):
    ia_output = ollama.generate(model=IA, prompt=prompt)
    return ia_output["response"]


def define_bar():
    """Create a bar"""
    bar = tk.Tk()

    bar.attributes("-topmost", True)    # always above other windows
    bar.attributes("-type", "splash")   # Enlève les bordures d'une windows dégeulasse
    # Coordonates position of the bar:
    x = (bar.winfo_screenwidth() - WIDTH) // 2
    bar.geometry(f"{WIDTH}x{HEIGHT}+{x}+{Y}")

    return bar


def define_cursor(bar):
    """Create text's input field"""
    cursor = tk.Entry(bar, insertbackground=CURSOR_COLOR)

    cursor.pack(fill="both", expand=True) # Length cursor can travel

    cursor.focus_force()
    return cursor


def post_input(bar_input):
    """Read the typed text, then empty the field"""
    text = bar_input.get()         # récupère
    bar_input.delete(0, tk.END)    # vide tout
    return text


def output(event, bar_output):
    """Configure IA output"""
    text = post_input(event.widget)

    # Create a textzone for display
    ia_output(bar_output, ask_ia(text))

def ia_output(text_area, text):
    return text_area.config(text=text)

def define_bar_output(bar):
    """Create output bar"""
    label = tk.Label(bar)

    label.pack()

    return label

def main():
    bar = define_bar()
    bar_cursor = define_cursor(bar)
    bar_output = define_bar_output(bar)

    # Keybind
    bar.bind("<Return>", lambda event : output(event, bar_output)) # (Return == Enter)
    bar.bind("<Escape>", lambda event : bar.destroy()) # lambda event + () pour limiter les fonctions à plus dd'1 truc de merde
    bar.mainloop()


if __name__ == "__main__":
    main()

