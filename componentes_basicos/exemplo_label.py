import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('500x200')
        self.lbl_titulo = tk.Label(self.janela,
                                   text='Copa do Mundo',
                                   bg='red',
                                   fg='black',
                                   width=30,
                                   height=5,
                                   anchor='ne',
                                   #bd=10,
                                   #relief='ridge',
                                   font=('ubuntu', 20, 'bold')
                                   )
        self.lbl_titulo.pack()

gui = tk.Tk()
Tela(gui)
gui.mainloop()