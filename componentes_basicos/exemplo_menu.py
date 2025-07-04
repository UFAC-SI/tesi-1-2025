import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('400x400')
        self.mnu_barra = tk.Menu(self.janela)
        self.mnu_item_arq = tk.Menu(self.mnu_barra, tearoff=0)
        self.mnu_barra.add_cascade(label='Arquivo', menu=self.mnu_item_arq)
        self.mnu_item_arq.add_command(label='Abrir', command=None)
        self.mnu_item_arq.add_command(label='Salvar', command=None)
        self.mnu_item_arq.add_separator()
        self.mnu_item_arq.add_command(label='Sair', command=self.janela.destroy)

        self.mnu_item_fer = tk.Menu(self.mnu_barra, tearoff=0)
        self.mnu_barra.add_cascade(label='Ferramentas', menu=self.mnu_item_fer)
        self.mnu_item_fer.add_command(label='Procurar texto...')
        self.mnu_item_fer.add_command(label='Substituir')

        self.spb = tk.Spinbox(self.janela, from_=1, to=10)
        self.spb.pack()
        self.var_escala = tk.IntVar()
        self.scl = tk.Scale(self.janela, from_=1, to=100,
                            orient='horizontal', variable=self.var_escala)
        self.scl.pack()

        self.janela.config(menu=self.mnu_barra)


gui = tk.Tk()
Tela(gui)
gui.mainloop()