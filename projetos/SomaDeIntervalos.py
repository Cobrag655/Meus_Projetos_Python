#crie um programa que calule a soma dos numeros em um intervalo
#somar todos os numeros de 1 a 10

def calculo(numero1, numero2):
    #printa um titulo
    print(f"A soma de {numero1} a {numero2} e:\n")
    #soma e 0
    soma = 0
    #para cada numero em um range definido pelo cliente, com o final + 1
    for num in range(numero1, numero2 + 1):
        #adicione a soma o valor de numero
        soma += num
        #printa tudo
        print(f"{soma}")

while True:
    try:
        numero1 = int(input("Qual numero voce gostaria de começar?: "))
        numero2 = int(input("E o segundo?: "))
        calculo(numero1, numero2)
        break
    except ValueError:
        print("coloque um numero correto")
