#mediator + estrutura simples de looping
# #defindo medias
aluno = "Gabriell"
a = True

while a == True:
    bm1 = int(input(" coloque a primeira nota: \n"))
    bm2 = int(input(" coloque a segunda nota: \n"))
    bm3 = int(input(" coloque a terceira nota: \n"))
    bm4 = int(input(" coloque a quarta e ultima nota: \n"))

    notas = [bm1,bm2,bm3,bm4]

    print(f" Suas Notas Foram: {notas}\n") 

    #calculando a media
    def Calculadora(bm1, bm2, bm3, bm4):
       #calcula a media
     media = (bm1, bm2, bm3, bm4) / 4
     print(" sua media de nota e: \n NOTA: {:.1f}" .format(media))

     if media < 6:
         print(" reprovado")
     elif media >= 6:
        print(" aprovado")

    escolha = input("Gostaria de continuar?\n")
    if escolha == "y":
        print()
        continue
    else:
        a = False