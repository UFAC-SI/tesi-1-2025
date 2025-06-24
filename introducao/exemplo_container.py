import tkinter as tk

janela = tk.Tk()
#Características básicas
janela.title('Primeira Janela com Tkinter')
janela.geometry('400x200')
janela.resizable(width=False, height=True)
janela.maxsize(400,500)
#Adicionar um componente do tipo Frame
container = tk.Frame(janela, width=100, height=100, bg='red') #Declaração do frame com o parâmetro pai (janela)
#Gerenciador de layout
#container.pack() #Adiciona o componente na janela

janela.mainloop()