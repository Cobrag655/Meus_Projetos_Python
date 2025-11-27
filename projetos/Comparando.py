#variaveis
# numero1 = float(input("digite o primeiro numero: \n"))
# numero2 = float(input("digite o segundo numero: \n"))

# #comparando
# print("comparando os numeros\n")
# print(numero1, "==", numero2, ":", numero1 == numero2 )#identico
# print(numero1, "!=", numero2, ":", numero1 != numero2 )#diferente
# print(numero1, ">", numero2, ":", numero1 > numero2 )#1 maior que 2
# print(numero1, "<", numero2, ":", numero1 < numero2 )#2 maior que 1
# print(numero1, ">=", numero2, ":", numero1 >= numero2 )#1 maior/igual a 2
# print(numero1, "<=", numero2, ":", numero1 <= numero2 )#1 menor/igual a 1

#comparar a idade de 2 pessoas e falar a comparaçao

#nomes e idades
nome1 = str(input("qual o nome da primeira pessoa?\n"))
nome2 = str(input("qual o nome da segunda pessoa?\n"))
pessoa1 =int(input("Qual a idade da pessoa 1? \n"))
pessoa2 =int(input("Qual a idade da pessoa 2? \n"))

#def
def comparacao(pessoa1, pessoa2):
        #se ou nao
        if pessoa1 == pessoa2:
            print(f"as idades sao iguais")
        elif pessoa1 > pessoa2:
            print(f"{nome1} e mais velho que {nome2}")
        elif pessoa1 < pessoa2:
            print(f"{nome2} e mais velha que {nome1}")

#printa
comparacao(pessoa1, pessoa2)