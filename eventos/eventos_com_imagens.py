import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageTk
class Tela:
    def __init__(self, master):
        self.janela = master
        self.btn_abrir = tk.Button(self.janela, text='Abrir arquivo...')
        self.btn_abrir.pack()
        self.lbl_imagem = tk.Label(self.janela)
        self.lbl_imagem.pack()
        self.btn_abrir.bind('<Button-1>', self.abrir)
        self.btn_salvar = tk.Button(self.janela, text='Salvar como...')
        self.btn_salvar.pack()
        self.btn_salvar.bind('<ButtonRelease-1>', self.salvar)

    def salvar(self, event):
        pass


    def abrir(self, event):
        tipos = (('Imagens', '*.jpeg *.jpg'), ('Todos', '*.*'))
        caminho_imagem = fd.askopenfilename(filetypes=tipos)
        imagem = Image.open(caminho_imagem)
        imagem_tk = ImageTk.PhotoImage(imagem)
        self.lbl_imagem.config(image=imagem_tk)
        self.lbl_imagem.image = imagem_tk



app = tk.Tk()
Tela(app)
app.mainloop()