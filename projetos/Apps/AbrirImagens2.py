import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# # Lista para manter referências das imagens
# imagens_carregadas = []

# def carregarI():
#     # Limpar imagens anteriores da tela
#     for imagem in frame_imagens.winfo_children():
#         imagem.destroy()
#     imagens_carregadas.clear()

#     # Pega os caminhos das entradas
#     caminhos = [
#         nome_entry1.get(),
#         nome_entry2.get(),
#         nome_entry3.get(),
#         nome_entry4.get(),
#         nome_entry5.get()
#     ]

#     for caminho in caminhos:
#         if not caminho.strip():
#             continue  # Pula entradas vazias

#         if not os.path.isfile(caminho):
#             messagebox.showerror("Erro", f"Arquivo '{caminho}' não encontrado.")
#             continue

#         try:
#             img_p = Image.open(caminho)
#             img_p = img_p.resize((200, 150))  # Redimensiona todas para o mesmo tamanho
#             img_tk = ImageTk.PhotoImage(img_p)

#             # Cria um rótulo com a imagem e adiciona no frame
#             label = tk.Label(frame_imagens, image=img_tk)
#             label.pack(side=tk.LEFT, padx=5)

#             imagens_carregadas.append(img_tk)  # Guarda referência
#         except Exception as e:
#             messagebox.showerror("Erro", f"Erro ao carregar imagem '{caminho}':\n{e}")

# janela = tk.Tk()
# janela.title("Visualizador de Imagens")
# janela.geometry("1100x600")

# # Campo de entrada
# label_entrada = tk.Label(janela, text="Digite o caminho das imagens\nEx: imagem.jpg")
# label_entrada.pack(pady=(10, 0))

# nome_entry1 = tk.Entry(janela, width=50)
# nome_entry1.pack(pady=4)

# nome_entry2 = tk.Entry(janela, width=50)
# nome_entry2.pack(pady=4)

# nome_entry3 = tk.Entry(janela, width=50)
# nome_entry3.pack(pady=4)

# nome_entry4 = tk.Entry(janela, width=50)
# nome_entry4.pack(pady=4)

# nome_entry5 = tk.Entry(janela, width=50)
# nome_entry5.pack(pady=4)

# # Botão
# botao_c = tk.Button(janela, text="Carregar Imagens", command=carregarI)
# botao_c.pack(pady=10)

# # Frame onde as imagens vão aparecer
# frame_imagens = tk.Frame(janela)
# frame_imagens.pack(pady=10)

# janela.mainloop()




#correçao
#lista para armazenar as imagens
imagem_tk = []

#funçao para carregar as imagens
def carregarI():
    nomes_a = [
        entrada1.get().strip(),
        entrada2.get().strip(),
        entrada3.get().strip(),
        entrada4.get().strip(),
    ]

    #limpar as imagens anteriores
    for widget in frame_imagens.winfo_children():
        widget.destroy()
    
    imagem_tk.clear()

    for i, nome in enumerate(nomes_a):
        if not nome:
            continue
        if not os.path.isfile(nome):
            messagebox.showerror("Erro", f"imagem {i+1}: \nArquivo '{nome}' Nao encontrado")
            continue
        try:
            image_pil = Image.open(nome)
            image_pil = image_pil.resize((150, 150))
            imagens_tk = ImageTk.PhotoImage(image_pil)
            imagem_tk.append(imagens_tk)

            label = tk.Label(frame_imagens, image=imagens_tk)
            label.grid(row=i // 2, column=i % 2, padx=10, pady=10)
        except Exception as e:
            messagebox.showerror("Erro", f"imagem {i+1}: \nErro ao carregar: {e}")

#criacao das janelas
janela = tk.Tk()
janela.title("exibindo a janela")
janela.geometry("800x600")

tk.Label(janela, text="Digite ate 5 nomes de imagem\nEX: foto.jpg").pack(pady=(10, 5))

#entrada para nomes
entrada1 = tk.Entry(janela, width=50)
entrada1.pack(pady=2)

entrada2 = tk.Entry(janela, width=50)
entrada2.pack(pady=2)

entrada3 = tk.Entry(janela, width=50)
entrada3.pack(pady=2)

entrada4 = tk.Entry(janela, width=50)
entrada4.pack(pady=2)

#botao
botao_c = tk.Button(janela, text="Carregar imagem", command=carregarI)
botao_c.pack(pady=10)

#frame onde as imagens vao aparecer
frame_imagens = tk.Frame(janela)
frame_imagens.pack(pady=10)

janela.mainloop()