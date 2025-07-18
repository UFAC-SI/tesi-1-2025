import tkinter as tk
from tkinter import messagebox
class Tela:
    def __init__(self, master):
        self.janela = master
        self.btn = tk.Button(self.janela, text='Abrir', command=self.mensagem)
        self.btn.pack()
    def mensagem(self):
        retorno = messagebox.showerror('Aviso', 'Cuidado!')
        print(retorno)
        retorno2 = messagebox.askquestion('Confirmação', 'Confirma?')
        if retorno2 == 'yes':
            print('Confirmou')
        else:
            print('Ficou com medo.')

gui = tk.Tk()
principal = Tela(gui)
gui.mainloop()