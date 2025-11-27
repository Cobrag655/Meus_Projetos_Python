#pedir, calcular e exibir

#def de calculo para preço
def  calculo(unidade, preco):
    valor_total = (unidade * preco)
    return valor_total

#variaveis
produto = str(input("Qual produto gostaria? \n"))
unidade = int(input("Quantos gostaria? \n"))
preco = float(input("Quanto custa? \nR$|"))

#puxar def
valor = calculo(unidade, preco)

#resultado
print(f"o valor da compra e de R$| {valor:.2f}")