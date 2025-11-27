#desenvolver codigo para uso em sala de aula
#que tenha turma
#nome do professor/aluno, quatro notas, media, situaçao aprovado reprovado >=6 utilizando loop, except (0, 10), para sair do looping sim
def calculo_media(notas):
    return sum(notas) / len(notas)
    

t1 = []

print("----------Sistema de notas 3.0--------------\n")
while True:
    try:
        
        professor = str(input("Qual seu nome?(ou se preferir sair, digite 'fim'): "))
        if professor.lower() == "fim":
            break
        turma = str(input("Qual turma?: "))
        nome_a = str(input("Nome do aluno: "))
        notas = []
        bimestres = ["1ªBimestre", "2ªBimestre", "3ªBimestre", "4ªBimestre"]
        for b in bimestres:
            while True:
                try:
                    nota = float(input(f"Qual a Nota do {b} do {nome_a} ?: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Insira um numero de 0 a 10!")
                except ValueError as e:
                    print(f"Erro; {e}, tente novamente")
        
        

        
        resultado = calculo_media(notas)
        situacao = "Aprovado!" if resultado >= 6 else "Reprovado"
            
            

        Bdd = {
            "Professor" : professor,
            "Turma" : turma,
            "Nome" : nome_a,
            "Nota" : notas,
            "Media" : calculo_media(notas),
            "Situacao" : situacao
        } 

        t1.append(Bdd)  
    
    except ValueError as e:
        print(f"Error: {e}, tente novamente.")



print("\nBoletim da Turma: ")
for Bdd in t1:
    print(f"Turma: {Bdd['Turma']} / Professor: {Bdd['Professor']} / Alunos: {Bdd['Nome']} / Notas: {Bdd['Nota']} / Media: {Bdd['Media']:.2f} / Situaçao: {Bdd['Situacao']}.")
