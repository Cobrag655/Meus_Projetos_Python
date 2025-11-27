 #algoritimo, argumentos, valor unitario * quantidade
def calculo(valor, quantidade):
    valor_f = valor * quantidade
    print(f"O produto {produto}\ncusta: R$|{valor:.2f}\nquantidade e: {quantidade}\nO valor total custara: R$|{valor_f:.2f}")

while True:
    try:

        produto = str(input("Qual produto gostaria?:\n"))
        valor = float(input("Qual o valor do prodruto?\n"))
        quantidade = int(input("Qual a quantidade?:\n"))
        calculo(valor, quantidade)
        escolha = str(input(f"deseja tentar novamente? s/n: ")).lower()
        if escolha == "s":
            continue
        else:
            break
    except ValueError:
        print("Coloque as informaçoes corretamente, pois algo esta errado")

            
