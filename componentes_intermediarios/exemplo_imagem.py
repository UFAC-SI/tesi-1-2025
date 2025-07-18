import tkinter as tk
from tkinter import messagebox
class Tela:
    def __init__(self, master):
        self.janela = master
        self.imagem = tk.PhotoImage(file='Logo-ufac.png')
        self.imagem = self.imagem.subsample(3,3)
        self.lbl = tk.Label(self.janela, image=self.imagem)
        self.lbl.image = self.imagem
        self.lbl.pack()

gui = tk.Tk()
principal = Tela(gui)
gui.mainloop()