import tkinter as tk

class Tela:
    def clicou(self):
        if self.var_cbt1.get() == 1 and self.var_cbt2.get() == 1:
            self.lbl.config(text='Empatou')
        elif self.var_cbt2.get() == 1:
            self.lbl.config(text='Vitória do Bayern')
        elif self.var_cbt1.get() == 1:
            self.lbl['text'] = 'Vitória do Flamengo'
        else:
            self.lbl.config(text='Aposte!!!')


    def __init__(self, master):
        self.janela = master
        self.janela.geometry('300x300')
        self.var_cbt1 = tk.IntVar()
        self.var_cbt2 = tk.IntVar()
        self.cbt1 = tk.Checkbutton(self.janela, text='Flamengo',
                                   variable=self.var_cbt1)
        self.cbt1.pack()

        self.cbt2 = tk.Checkbutton(self.janela,
                                   variable=self.var_cbt2,
                                   text='Bayern')
        self.cbt2.pack()

        self.btn = tk.Button(self.janela, text='Confirmar', command=self.clicou)
        self.btn.pack()

        self.lbl = tk.Label(self.janela)
        self.lbl.pack()


gui = tk.Tk()
Tela(gui)
gui.mainloop()