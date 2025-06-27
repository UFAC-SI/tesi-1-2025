import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('200x200')
        self.lbl_login = tk.Label(self.janela, text='Login:').pack()
        self.ent_login = tk.Entry(self.janela, width=20).pack()

        self.lbl_senha = tk.Label(self.janela, text='Senha:').pack()
        self.ent_senha = tk.Entry(self.janela, width=20, show='º')
        self.ent_senha.pack()

        self.btn_enviar = tk.Button(self.janela, text='Enviar', command=self.verificar_senha).pack()

        self.lbl_mostrar = tk.Label(self.janela)
        self.lbl_mostrar.pack()

    def verificar_senha(self):
        senha = self.ent_senha.get()
        #self.lbl_mostrar.config(text=senha) #1ª forma de alterar uma opção do componente
        self.lbl_mostrar['text'] = senha #2ª forma de alterar
        #if senha == '123':

gui = tk.Tk()
Tela(gui)
gui.mainloop()