#timedelta usado para calcular um intervalo de tempo ex: 2025 a 2026, retorna 1y

import time
from datetime import datetime, timedelta

while True:
    try:    
        h_atual = datetime.now()
        tempo = h_atual.strftime("%H:%M:%S")
        dia = h_atual.strftime("%d/%m/%y")
        data_f = h_atual + timedelta(days=30)
        diferenca = data_f - h_atual
        print(f"Hoje é:", dia, "e sao:", tempo, end="\r")
        print(f"Data futura (30 a partir de agora):", data_f, end="\r")
        print(f"A diferença de dias e de:", {diferenca.strftime()}, end="\r")
        time.sleep(1)
    except ValueError as e:
        print(f"Error: {e}, Tente Novamente!")

#terminar de arrumar a formataçao


