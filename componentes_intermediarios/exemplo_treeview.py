import tkinter as tk
from tkinter import ttk
class Tela:
    def __init__(self, master):
        self.janela = master
        colunas = ['nome', 'cpf', 'email']
        self.tvw = ttk.Treeview(self.janela, height=5, columns=colunas, show='headings')
        #Configurar o cabaçalho das colunas
        self.tvw.heading('nome', text='NOME')
        self.tvw.heading('cpf', text='CPF')
        self.tvw.heading('email', text='EMAIL')
        #Preencher a tabela
        self.tvw.insert('', 'end', values=('Limeira', '00000000000', 'limeira@ufac.br'))
        self.tvw.insert('', 'end',
                        values=('Manoel', '00000000000', 'manoel@ufac.br'))
        self.tvw.insert('', 'end',
                        values=('Teste1', '00000000000', '1@ufac.br'))
        self.tvw.insert('', 'end',
                        values=('Teste2', '00000000000', '2@ufac.br'))
        self.tvw.insert('', 'end',
                        values=('Teste3', '00000000000', '3@ufac.br'))
        self.tvw.insert('', 'end',
                        values=('Teste4', '00000000000', '4@ufac.br'))
        self.tvw.insert('', 'end',
                        values=('Teste5', '00000000000', '5@ufac.br'))
        self.tvw.insert('', 'end',
                        values=('Teste6', '00000000000', '6@ufac.br'))
        self.tvw.insert('', 'end',
                        values=('Teste7', '00000000000', '7@ufac.br'))
        self.tvw.grid(row=0, column=0)
        self.brl = ttk.Scrollbar(self.janela, command=self.tvw.yview)
        self.brl.grid(row=0, column=1, sticky='ns')
        self.tvw.configure(yscrollcommand=self.brl.set)

gui = tk.Tk()
principal = Tela(gui)
gui.mainloop()