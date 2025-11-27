def imc (peso, altura):
    imc = peso / (altura**2)
    return imc

while True:
    try:
        peso = float(input("Qual seu peso: "))
        altura = float(input("Qual sua altura: "))

        resultado = imc(peso, altura)
        print(f"seu imc e igual a {resultado:.2f}")
        if resultado < 18.5:
            print("Class: Abaixo")
        elif resultado >= 18.5 and resultado < 24.9:
            print("Class: Okay")
        elif resultado > 24.9 and resultado < 40:
            print("Class: Acima")
        else:
            print("Class: Megazord")

        escolha = str(input("gostaria de tentar novamente?: (s/n)\n")).lower()
        if escolha == "s":
            print()
        else:
            break
    except ValueError:
        print("ta dando erro bonitao")