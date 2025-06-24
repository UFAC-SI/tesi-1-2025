import tkinter as tk

janela = tk.Tk()
janela.title('Primeira Janela com Tkinter')
janela.geometry('400x200')
janela.resizable(width=False, height=True)
janela.maxsize(400,500)

janela.mainloop()