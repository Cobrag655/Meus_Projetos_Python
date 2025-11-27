#Ngc inutil
nome = str(input("Qual seu nome: \n"))
print("Quantos anos vc tem?: ")
Idade1 = int(input())
if Idade1 <= 12:
    print(f"Voce e uma criança")
elif Idade1 <= 18:
    print(f"vc e um adolecente")
elif Idade1 <= 59:
    print(f"Vc e um adulto")
elif Idade1 >= 60:
    print(f"vc e um idoso")