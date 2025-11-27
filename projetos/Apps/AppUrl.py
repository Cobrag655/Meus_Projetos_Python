# import webbrowser

# #url aleatoria
# url = "https://tryhackme.com"

# #comando para abrir a url
# webbrowser.open(url)

#-------------------------------------------------------------------

import tkinter as tk
import webbrowser

#def para abrir a url no navegador
def abrir_n():
    url = url_entry.get()
    webbrowser.open(url)

#criar a janela principal
janela = tk.Tk()
janela.title("Abrir navegador.")

#label para entrada
tk.Label(janela, text="DIGITA ESSA PORRA = ").pack(pady=5)
url_entry = tk.Entry(janela, width=50)
url_entry.pack(pady=5)

#botao para abrir url
abrir = tk.Button(janela, text="Clique aqui para abrir", command=abrir_n)
abrir.pack(pady=10)

#manter a janela em looping
janela.mainloop()

