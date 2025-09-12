import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Tela:
    def __init__(self, master):
        self.janela = master
        self.lbl = ttk.Label(self.janela, text='Bem vindo ao ttkboostrap')
        self.lbl.pack()
        self.flo = (ttk.Floodgauge(self.janela, mode='determinate',
                                  value=0,
                                  maximum=100,

                                  mask='Transferindo {}%'))
        self.flo.pack()
        self.btn_start = ttk.Button(self.janela, text='Iniciar')
        self.btn_start.pack()
        self.btn_start.bind('<Button-1>', self.iniciar)
        self.btn_stop = ttk.Button(self.janela, text='Parar')
        self.btn_stop.pack()
        self.btn_stop.bind('<Button-1>', self.parar)


        #if self.flo.value == 100:

    def parar(self, event):
        self.flo.stop()

    def iniciar(self, event):
        self.flo.start()

app = ttk.Window(themename='litera')#tk.Tk()
Tela(app)
app.mainloop()