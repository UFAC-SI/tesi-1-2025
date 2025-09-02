import tkinter as tk
from tkinter import messagebox


class Tela:
    def __init__(self, master):
        self.janela = master
        self.btn = tk.Button(self.janela, text='Clicar')
        self.btn.pack()
        self.btn.bind('<Key>', self.clicou)
        self.btn.bind('<Control-c>', self.mensagem)
        self.btn.bind('<Control_L><Shift_L><v>', self.mensagem)

    def clicou(self, event):
        print(f'Vc pressionou a tecla: {event.char} {event.keysym}')

    def mensagem(self, event):
        messagebox.showinfo('Mensagem', f'Tecla pressionada: {event.keysym}')

app = tk.Tk()
Tela(app)
app.mainloop()