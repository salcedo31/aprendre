import tkinter as tk
from tkinter import messagebox
import random

class WordGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Juego de Traducciones")

        # Diccionario de palabras en inglés y sus traducciones en español
        self.words = {
            "apple": "manzana",
            "banana": "plátano",
            "orange": "naranja",
            "grape": "uva",
            "strawberry": "fresa",
            "peach": "durazno",
            "melon": "melón",
            "kiwi": "kiwi",
            "watermelon": "sandía",
            "cherry": "cereza"
        }

        self.current_word = None
        self.label = tk.Label(master, text="Traduce la palabra:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        self.check_button = tk.Button(master, text="Comprobar", command=self.check_translation)
        self.check_button.pack(pady=10)

        self.next_word()

    def next_word(self):
        self.current_word = random.choice(list(self.words.keys()))
        self.label.config(text=f"Traduce la palabra: {self.current_word}")

    def check_translation(self):
        user_input = self.entry.get()
        correct_translation = self.words[self.current_word]
        if user_input.lower() == correct_translation:
            messagebox.showinfo("Resultado", "Correcto!")
        else:
            messagebox.showerror("Resultado", f"Incorrecto! La respuesta correcta es: {correct_translation}")
        self.entry.delete(0, tk.END)  # Limpiar la entrada
        self.next_word()  # Ir a la siguiente palabra

if __name__ == "__main__":
    root = tk.Tk()
    game = WordGame(root)
    root.mainloop()
