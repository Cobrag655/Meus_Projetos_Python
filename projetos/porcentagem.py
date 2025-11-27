#porcentagem
#trabalhando com porcentagem
#definindo o funcionario, salario atual e a porcentagem de aumento
funcionarios = "Gabriell"
salario_atual = 10000
aumento_porcentagem = 20 #nao por 20%

#calculo do aumento
aumento = (salario_atual / 100) * aumento_porcentagem

#calculando o novo salario
novo_salario = salario_atual + aumento

#exibindoo o resultado
print(f"funcionario: {funcionarios}")
print("salario atual: R$| {:.2f}" .format(salario_atual))
print("aumento: R$| {:.2f}" .format(aumento))
print("salario novo: R$| {:.2f}" .format(novo_salario))