import tkinter as tk
import pyautogui

def cordenadas():
    x, y = pyautogui.position()
    coord_label.config(text=f"Coordenadas globais: X={x}, Y={y} ")
    janela.after(100, cordenadas)

#criar janela principal
janela = tk.Tk()
janela.title("Nao aguento mais")

#cria um rotulo para exibir
coord_label = tk.Label(janela, text="Coordenadas: X=0, Y=0")
coord_label.pack(pady=20)

cordenadas()

janela.mainloop()