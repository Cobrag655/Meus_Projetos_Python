import tkinter as tk
from tkinter import messagebox

# Variáveis globais
nome = ""
profissao = ""

# Função para mostrar mensagem do menu
def mostra_mensagem(opcao):
    messagebox.showinfo("Opção Selecionada", f"{nome}, você selecionou: {opcao}\nProfissão: {profissao}")

# Função para capturar informações
def abrir_menu():
    global nome, profissao
    nome = nome_entry.get()
    profissao = profissao_entry.get()
    messagebox.showinfo("Informação Capturada", f"Nome: {nome}\nProfissão: {profissao}")

# Função para fechar a janela
def fechar_janela():
    if messagebox.askyesno("Confirmação", "Você tem certeza que deseja fechar?"):
        janela.destroy()

# Função para criar a janela principal
def criar_menu():
    global nome_entry, profissao_entry, janela

    # Criar a janela principal
    janela = tk.Tk()
    janela.title("Menu Pop-Up")

    # Entradas de texto
    tk.Label(janela, text="Digite seu nome:").pack(pady=5)
    nome_entry = tk.Entry(janela)
    nome_entry.pack(pady=5)

    tk.Label(janela, text="Digite sua profissão:").pack(pady=5)
    profissao_entry = tk.Entry(janela)
    profissao_entry.pack(pady=5)

    # Botão para salvar/capturar informações
    abrir_menu_button = tk.Button(janela, text="Salvar e capturar informações", command=abrir_menu)
    abrir_menu_button.pack(pady=10)

    # Botão para fechar a janela
    fechar_button = tk.Button(janela, text="Fechar", command=fechar_janela)
    fechar_button.pack(pady=10)

    # Criar menu
    menu = tk.Menu(janela)

    # Criar submenu
    submenu = tk.Menu(menu, tearoff=0)
    submenu.add_command(label="Opção1", command=lambda: mostra_mensagem("Opção1"))
    submenu.add_command(label="Opção2", command=lambda: mostra_mensagem("Opção2"))
    submenu.add_command(label="Opção3", command=lambda: mostra_mensagem("Opção3"))

    menu.add_cascade(label="Menu", menu=submenu)

    # Configurar menu na janela
    janela.config(menu=menu)

    # Iniciar loop principal
    janela.mainloop()

# Executar app
criar_menu()
