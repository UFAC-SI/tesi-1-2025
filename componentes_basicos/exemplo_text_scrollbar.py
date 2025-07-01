import tkinter as tk
from tkinter.scrolledtext import ScrolledText
class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('400x90')
        self.scb = tk.Scrollbar(self.janela)
        self.scb.pack(side=tk.RIGHT, fill=tk.Y)
        linhas = '''
        Linha 1
        linha 2
        linha 3
        ...
        ...
        ...
        linha n
        '''
        teste = 'teste'
        self.txt = tk.Text(self.janela ,height=5, yscrollcommand=self.scb.set)
        self.txt.insert(tk.END, linhas)
        self.txt.pack(side='left')
        self.scb.config(command=self.txt.yview)
        self.stx = ScrolledText(self.janela)
        self.stx.pack()

gui = tk.Tk()
Tela(gui)
gui.mainloop()