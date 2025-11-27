#definindo um dicionario
aluno = {
    "Aluno" : "Gabriell",
    "Idade" : 16,
    "curso" : "Pyhton",
    "Notas" : [7, 8, 5, 9]
}


#acessando informaçoes do dicionario
# print(f"Nome: {aluno['Aluno']}\nIdade: {aluno['Idade']}\ncurso: {aluno['curso']}\nNotas: {aluno['Notas']}")

#Adiciona uma variavel
# aluno['Cidade'] = "Osasco-SP"

# #modificando
# aluno['curso'] = "Java"

#printa tudo
# print(aluno)

#verificando informaçoes
# try:
#     if "Aluno" in aluno:
#         print(f"A chave: {aluno['Aluno']}")
#     else:
#         print("nao tem nenhum campo assim")
# except ValueError:
#     print("Tente Novamente")

#itinerando pelas chaves e valores do dic
# for chave, valor in aluno.items():
#     print(f"{chave} : {valor}") 

#usando key() , no dicionario
dados = {
    "nome" : "Gabriell",
    "Idade" : 16,
    "Cidade": "Osasco-SP"
}

#.keys() diz quais variaveis vc tem la dentro
#.values() te da os valores dessas variaveis e por fim 
#.items() te traz as variaveis e seus resultados por inteiro

print(dados.keys())
print(dados.values())
print(dados.items())