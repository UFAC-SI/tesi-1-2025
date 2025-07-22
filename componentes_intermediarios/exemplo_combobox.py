import tkinter as tk
from tkinter import ttk, messagebox

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('400x400')
        self.dia = tk.StringVar()
        valores = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
        self.cbx_semana = ttk.Combobox(self.janela, values=valores,
                                       textvariable=self.dia,
                                       state='read')
        self.cbx_semana.current(0)
        self.cbx_semana.pack()
        btn = ttk.Button(self.janela, text='Enviar', command=self.enviar)
        btn.pack()
    def enviar(self):
        messagebox.showinfo('Informação', 'A prova vai ser na: '+self.dia.get())

gui = tk.Tk()
principal = Tela(gui)
gui.mainloop()