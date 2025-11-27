#calcular cordenadas simples
import math

#def com raiz quadrada math.sqrt
def calcular_d(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1)**2+(y2 - y1)**2)
    return distancia

print("\nBem Vindo ao Calculador De Distancia!")
while True:
    try:
        #pedindo as variaveis
        print("Digite as coordenadas do primeiro ponto:\n")
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        print("Digite as coordenadas do segundo ponto:\n")
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))

        #definindo a funçao
        distancia = calcular_d(x1, y1, x2, y2)

        print(f"\nA distancia entre os pontos ({x1}, {y1}) e ({x2}, {y2}) é de:\n{distancia:.2f}")

        print("Gostaria de usar nosso programa novamente? (s/n)\n")
        escolha = str(input()).strip().lower()

        if escolha == "s":
            continue
        else:
            break
    except ValueError as e:
        print(f"Error: {e}, Tente novamente")