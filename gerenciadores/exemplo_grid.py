import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('250x200')
        self.lbl_login = tk.Label(self.janela, text='Login:')
        self.lbl_login.grid(row=0, column=0)
        self.ent_login = tk.Entry(self.janela, width=20)
        self.ent_login.grid(row=0, column=1)

        self.lbl_senha = tk.Label(self.janela, text='Senha:')
        self.lbl_senha.grid(row=1, column=0)
        self.ent_senha = tk.Entry(self.janela, width=20, show='º')
        self.ent_senha.grid(row=1, column=1)
        self.btn_enviar = tk.Button(self.janela, text='Enviar')
        self.btn_enviar.grid(row=2, column=1, stick='we')
        self.btn_limpar = tk.Button(self.janela, text='Limpar')
        self.btn_limpar.grid(row=2, column=0, stick='we')

gui = tk.Tk()
Tela(gui)
gui.mainloop()