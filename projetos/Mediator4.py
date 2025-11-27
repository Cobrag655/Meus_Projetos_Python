import tkinter as tk
from tkinter import ttk, messagebox

# Lista para guardar os alunos
alunos = []

# adiciona um aluno na lista
def add_a():
    turma = entrada_turma.get().strip()
    professor = entrada_professor.get().strip()
    aluno = entrada_aluno.get().strip()
    if not turma or not professor:
        messagebox.showerror("Atenção", "Preencha Turma e Professor!")
        return
    if not aluno:
        messagebox.showerror("Atenção", "Digite o Nome do Aluno!")
        return
    
    try:
        n1 = float(entrada_nota1.get())
        n2 = float(entrada_nota2.get())
        n3 = float(entrada_nota3.get())
        n4 = float(entrada_nota4.get())
    except ValueError as e:
        messagebox.showerror("Erro", f"{e}\nDigite números válidos nas notas.")
        return

    if any(n < 0 or n > 10 for n in (n1, n2, n3, n4)):
        messagebox.showerror("Erro", "Notas devem estar entre 0 e 10!")
        return
    
    # calculando a media
    media = (n1 + n2 + n3 + n4) // 4
    situacao = "Aprovado!" if media >= 6 else "Reprovado! :("
    
    alunos.append([aluno, n1, n2, n3, n4, media, situacao])
    messagebox.showinfo("Sucesso", f"{aluno} adicionado.\nMédia: {media:.1f} - Situação: {situacao}")

    # Limpar Campos do Aluno (Mantem Turma e Professor)
    entrada_aluno.delete(0, tk.END)
    entrada_nota1.delete(0, tk.END)
    entrada_nota2.delete(0, tk.END)
    entrada_nota3.delete(0, tk.END)
    entrada_nota4.delete(0, tk.END)
    
# mostrar os dados da tabela
def mostrar_result():
    turma = entrada_turma.get().strip()
    professor = entrada_professor.get().strip()
    
    label_turma.config(text=f"Turma: {turma}")
    label_professor.config(text=f"Professor: {professor}")
    
    # limpar tabela antes de preencher
    for i in tabela.get_children():
        tabela.delete(i)

    tabela.tag_configure("aprovado", foreground="green")
    tabela.tag_configure("reprovado", foreground="red")

    for aluno_dados in alunos:
        corte = "aprovado" if aluno_dados[6] == "Aprovado!" else "reprovado"
        tabela.insert("", tk.END, values=aluno_dados, tags=(corte,))

janela = tk.Tk()
janela.title("-----------------Sistema de notas 4.0-------------------")
janela.geometry("800x500")

# linhas para entrada de info
tk.Label(janela, text="Turma:").grid(row=0, column=0, padx=6, pady=8, sticky="e")
entrada_turma = tk.Entry(janela, width=25)
entrada_turma.grid(row=0, column=1, padx=6, pady=8, sticky="w")

tk.Label(janela, text="Professor:").grid(row=0, column=2, padx=6, pady=8, sticky="e")
entrada_professor = tk.Entry(janela, width=25)
entrada_professor.grid(row=0, column=3, padx=6, pady=8, sticky="w")

tk.Label(janela, text="Aluno:").grid(row=1, column=0, padx=6, pady=8, sticky="e")
entrada_aluno = tk.Entry(janela, width=40)
entrada_aluno.grid(row=1, column=1, padx=6, pady=8, sticky="w")

# linha para entrada das 4 notas
tk.Label(janela, text="Nota 1º Bimestre:").grid(row=2, column=0, padx=6, sticky="e")
entrada_nota1 = tk.Entry(janela, width=8)
entrada_nota1.grid(row=2, column=1, padx=6, sticky="w")

tk.Label(janela, text="Nota 2º Bimestre:").grid(row=3, column=0, padx=6, sticky="e")
entrada_nota2 = tk.Entry(janela, width=8)
entrada_nota2.grid(row=3, column=1, padx=6, sticky="w")

tk.Label(janela, text="Nota 3º Bimestre:").grid(row=2, column=2, padx=6, sticky="e")
entrada_nota3 = tk.Entry(janela, width=8)
entrada_nota3.grid(row=2, column=3, padx=6, sticky="w")

tk.Label(janela, text="Nota 4º Bimestre:").grid(row=3, column=2, padx=6, sticky="e")
entrada_nota4 = tk.Entry(janela, width=8)
entrada_nota4.grid(row=3, column=3, padx=6, sticky="w")

# botoes
btn_a = tk.Button(janela, text="Adicionar", width=15, command=add_a)
btn_a.grid(row=4, column=1, pady=12)

btn_m = tk.Button(janela, text="Mostrar Tabela", width=18, command=mostrar_result)
btn_m.grid(row=4, column=2, pady=12)

# criar area de resultados
label_turma = tk.Label(janela, text="Turma: ")
label_turma.grid(row=5, column=0, columnspan=2, sticky="w", padx=6)

label_professor = tk.Label(janela, text="Professor: ")
label_professor.grid(row=5, column=2, columnspan=2, sticky="w", padx=6)

# criar tabela para resultados
colunas = ("Nome", "N1", "N2", "N3", "N4", "Media", "Situação")
tabela = ttk.Treeview(janela, columns=colunas, show="headings", height=12)

# looping para criar os cabeçalhos da tabela
for c in colunas:
    tabela.heading(c, text=c)

# largura da tabela
tabela.column("Nome", width=220)
tabela.column("N1", width=60, anchor="center")
tabela.column("N2", width=60, anchor="center")
tabela.column("N3", width=60, anchor="center")
tabela.column("N4", width=60, anchor="center")
tabela.column("Media", width=80, anchor="center")
tabela.column("Situação", width=100 , anchor="center")

tabela.grid(row=6, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")

# permitir que a tabela cresça junto com a janela
janela.grid_rowconfigure(6, weight=1)
janela.grid_columnconfigure(3, weight=1)

janela.mainloop()

#terminal powershell para back
#pyinstaller -- onefile Mediator4.py com console
#python -m PyInstaller --onefile --noconsole --icon="python_94570.ico" Mediator4.py sem console e icon
#rode quando chegar


