import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Tela:
    def __init__(self, master):
        self.janela = master
        self.lbl = ttk.Label(self.janela, text='Bem vindo ao ttkboostrap')
        self.lbl.pack()
        self.mte = ttk.Meter(self.janela,
                             amountused=23,
                             metersize=300,
                             metertype='full',
                             interactive=False).pack()

app = ttk.Window(themename='litera')#tk.Tk()
Tela(app)
app.mainloop()