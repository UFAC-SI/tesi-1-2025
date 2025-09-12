import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Tela:
    def __init__(self, master):
        self.janela = master
        self.lbl = ttk.Label(self.janela, text='Bem vindo ao ttkboostrap')
        self.lbl.pack()
        self.ent = ttk.Entry(self.janela).pack()
        self.btn = ttk.Button(self.janela, text='Enviar',
                              bootstyle=DARK
                              ).pack()

app = ttk.Window(themename='litera')#tk.Tk()
Tela(app)
app.mainloop()