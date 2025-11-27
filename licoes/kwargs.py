# #permite maiores numeros dentro de uma unica variavel
# def somar_t(*numeros):
#     #resultado e sum faz a soma
#     total = sum(numeros)
#     return total

# #mostra o resultado
# resultado = somar_t(1, 2, 3, 4, 95, 987, 3728)
# print(resultado)

#usando (**kwargs)
#cria como no exemplo superior, mas ao inves de uma lista nao udavel cira um dicionario
def exibir(**info):
    #para chaves e valor in info.items(organiza os items por valor)
    for key, valor in info.items():
        #print os dois
        print(f"{key} : {valor}")

#chamando a funcao (fora do for)
exibir(nome = "Gabriell", idade = 16, cidade = "Osasco", peso = 60)