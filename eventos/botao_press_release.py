import tkinter as tk
from tkinter import messagebox


class Tela:
    def __init__(self, master):
        self.janela = master
        self.btn = tk.Button(self.janela, text='Pressione a tecla x')
        self.btn.pack()
        self.btn.focus()
        self.btn.bind('<KeyPress-x>', self.press)
        self.btn.bind('<KeyRelease-x>', self.release)
        self.btn.bind('<Button-1>', self.press)
        self.btn.bind('<ButtonRelease-1>', self.release)
        self.janela.bind('<Button-3>', self.mensagem)


    def mensagem(self, envent):
        messagebox.showinfo('Mensagem', 'Vc clicou com o botão direito')

    def press(self, event):
        self.btn.config(text='Pressionou a tecla x')

    def release(self, event):
        self.btn.config(text='Pressione a tecla x')


app = tk.Tk()
Tela(app)
app.mainloop()