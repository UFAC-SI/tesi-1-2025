import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('500x500')
        lbl1 = tk.Label(self.janela, text='Label 1', fg='white', bg='red')
        lbl1.pack(fill='both', expand=True, side='left', padx=10, pady=10)
        lbl2 = tk.Label(self.janela, text='Label 2', fg='white', bg='blue')
        lbl2.pack(fill='both', expand=True, side='left')
        lbl3 = tk.Label(self.janela, text='Label 3', fg='white', bg='green')
        lbl3.pack(fill='both', expand=True, side='left')

gui = tk.Tk()
Tela(gui)
gui.mainloop()