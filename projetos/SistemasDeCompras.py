def calculo(preco):
    preco = preco * quantidade
    return preco

produtos = []

while True: 
    try:
        item = str(input(f"Qual produto voce gostaria?: "))
        
        precos = []
        preco = float(input("Qual o preco desse produto?: "))
        quantidade = int(input("Quantos vc quer?: "))
        precos.append(preco)

        produto = {
            "Item" : item,
            "preco" : preco,
            "quantidade" : quantidade,
            "Preco final" : calculo(preco)
        }

        produtos.append(produto)

        print("\nRecibo: ")
        for produto in produtos:
            print(f"Item: {produto['Item']} | Preco: {produto['preco']:.2f} | quantidade: {produto['quantidade']} | Preco Final: {produto['Preco final']:.2f}")
        escolha = input(f"Gostaria de adicionar mais itens?: (s/n)\n").lower()
        if escolha == "s":
            print()
        else:
            break
    except ValueError:
        print("tente novamente")





