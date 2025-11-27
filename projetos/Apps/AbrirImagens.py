import tkinter as tk
from PIL import Image, ImageTk

# Caminho da imagem
caminhoI = r"bluezao_1.jpeg"

janela = tk.Tk()
janela.title("Exibir Imagem")
#janela.geometry("1200x800")  # Tamanho inicial para janela, se quiser

imagem_P = Image.open(caminhoI)
imagem_P = imagem_P.resize((130, 750))  # Resize espera uma tupla de inteiros
imagem_TK = ImageTk.PhotoImage(imagem_P)  # Corrigido aqui

# Criar rótulo para exibir
label_i = tk.Label(janela, image=imagem_TK)
label_i.pack(pady=20)

# Inicia o loop
janela.mainloop()
