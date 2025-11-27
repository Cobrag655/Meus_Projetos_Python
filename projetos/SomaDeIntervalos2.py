#cria um programa com a soma, usar funçoes e laços
def calculo(numero1, numero2):
    print(f"Soma dos intervalos dos numeros {numero1} e {numero2}:\n")
    soma = 0
    for num in range(numero1, numero2 + 1):
        soma += num
    return soma



while True:
    try:
        numero1 = int(input("qual numero voce gostaria?: \n"))
        numero2 = int(input("e o segundo: \n"))
        result = calculo(numero1, numero2)
        print(f"{result:.2f}")
        break
    except ValueError:
        print("Numero incorreto, tente novamente")
