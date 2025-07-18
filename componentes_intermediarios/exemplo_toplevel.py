import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.btn = tk.Button(self.janela, text='Abrir Toplevel', command=self.abrir)
        self.btn.pack()
    def abrir(self):
        self.janela.withdraw()#iconify()
        self.segunda_janela = tk.Toplevel(self.janela)
        self.segunda_janela.grab_set() # Impede a interação com a janela principal Tk()
        btn_fechar = tk.Button(self.segunda_janela, text='Fechar', command=self.fechar)
        btn_fechar.pack()
    def fechar(self):
        self.segunda_janela.destroy()
        self.janela.deiconify()


gui = tk.Tk()
principal = Tela(gui)
gui.mainloop()