# #programa que o professor mandara as notas, calcular e mostrar o resultado
# def calcular (nota1, nota2, nota3, nota4):
#     result = (nota1 + nota2 + nota3 + nota4) / 4
#     return result

 
# notas = []

# while True:
#     try:
#         nome = str(input("Qual o nome do aluno\n"))
#         nota1 = float(input("Qual a nota do aluno no primeiro bimestre?\n"))
#         nota2 = float(input("Qual a nota do aluno no segundo bimestre?\n"))
#         nota3 = float(input("Qual a nota do aluno no terceiro bimestre?\n"))
#         nota4 = float(input("Qual a nota do aluno no quarto bimestre?\n"))
#         notas.append(nome)
#         notasf = (nota1, nota2, nota3, nota4)
#         notas.append(notasf)
#         result = calcular (nota1, nota2, nota3, nota4)
#         print(result)
#         if result < 5:
#             print(f"O aluno/a {nome}, Foi reprovado.\n")
#         else:
#             print(f"Meus parabens!, aluno/a {nome} passou!.\n")
#         escolha = str(input("Deseja continuar? (s/n)\n")).lower()
#         if escolha == "s":
#             print(notas)
#         else:
#             break
#     except ValueError:
#         print("Erro de numero, tente novamente")


#mesma def acima mas com lens.
# alunos = []
# notas = []

# #funçao
# def calcular (notas):
#     return sum(notas) / len(notas) conta quantos caracteres exitem na lista, criando tuplas para aquela lista

#outra forma de solicitar notas
# for i in range(5):
#     nome = input(f"digite o nome do {i+1}° aluno")
#     alunos.append(nome)

#jeito ainda melhor que o acima
# print("\nResultados: ")
# for i in range(len(nome)):
#     media = result
#     situacao = "aprovado" if media >= 5
#     print(f"Alunos: {nome[i]} / Notas: {notas[i]} / Media: {notas:.2f} / Situacao: {situacao}")



#funçao
def calcular_media(notas):
    return sum(notas) / len(notas)

#lista de alunos
alunos = []

#solicita os dados de 5 alunos
for i in range(5):
    nome = input(f"Digite o nome do {i+1}° aluno: ")
    
    notas = []
    for j in range(3):
        nota = float(input(f"Digite a {j+1}° nota de {nome}: "))
        notas.append(nota)

    aluno = {
        "nome" : nome,
        "notas" : notas,
        "media" : calcular_media(notas),
    }

    #define a situacao do aluno
    aluno["situacao"] = "Aprovado" if aluno["media"] >= 6.0 else "reprovado"
    alunos.append(aluno)

#exibe o result
print("\nResultados: ")
for aluno in alunos:
    print(f"Aluno: {aluno['nome']} | notas: {aluno['notas']} | Media: {aluno['media']:.2f} | situacao: {aluno['situacao']}")
    