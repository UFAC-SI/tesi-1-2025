import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('500x500')
        lbl1 = tk.Label(self.janela, text='Label 1', fg='white', bg='red')
        lbl1.place(relx=0.5, rely=0.5, anchor='center')
        lbl2 = tk.Label(self.janela, text='Label 2', fg='white', bg='blue')
        lbl2.place(x=0, y=215, width=250)

gui = tk.Tk()
Tela(gui)
gui.mainloop()