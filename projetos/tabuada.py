vezes = 1

def calculo(numero1):
    print(f"Tabuada do numero {numero1}:\n")
    for i in range(1,11):
        resultado = numero1 * 1
        print(f"{numero1} x {i} = {resultado * i:.2f}")



while True:
    try:
        numero1 = int(input("qual numero voce gostaria?: \n"))
        calculo(numero1)
        break
    except ValueError:
        print("esta errado energumeno")
