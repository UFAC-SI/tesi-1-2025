import tkinter as tk

class MinhaTela:
    def __init__(self, master):
        self.janela = master
        # Características básicas
        self.janela.title('Primeira Janela com Tkinter')
        self.janela.geometry('400x200')
        self.janela.resizable(width=False, height=True)
        self.janela.maxsize(400, 500)
        # Adicionar um componente do tipo Frame
        self.container = tk.Frame(self.janela, width=100, height=100,
                             bg='red')  # Declaração do frame com o parâmetro pai (janela)
        # Gerenciador de layout
        self.container.pack() #Adiciona o componente na janela
        self.nome = tk.Label(self.container, text='Limeira')
        self.email = tk.Label(self.janela, text='juniorlimeiras@gmail.com')
        self.nome.place(x=10, y=10)
        self.email.pack()

gui = tk.Tk()
minhatela = MinhaTela(gui)
gui.mainloop()