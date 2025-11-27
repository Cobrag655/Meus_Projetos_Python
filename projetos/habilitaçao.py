idade = int(input("Qual sua idade?:\n"))
t_h = input("Possui habilitaçao? (sim/nao):\n").strip().lower() == "sim"

pode_dirigir = idade >= 18 and t_h
pode_p_s = idade >= 18 or t_h
nao_pode = not pode_p_s

#exibir as mensagems
print(f"pode dirigir: {pode_dirigir}\npode participar do sorteio?: {pode_p_s}\nNao pode participar: {nao_pode}")
