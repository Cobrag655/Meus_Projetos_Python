#usando while
# contador = 0

# while contador < 10:
#     contador += 0
#     if contador % 2 == 0: #pula os numeros pares sendo o % == negaçao
#         continue #pula os numeros pares
#     print(contador)

#loop for com range
#para cada numero in range de 1 a 4 (nao conta 5 por ser o break)
for i in range(1, 5):
    #printa i
    print(i)


#looping while
#contador vale 0
contador = 0
#enquanto nao chegar a MENOS QUE 5 (ou seja 4)
while contador < 5:
    #print e aumente 1
    contador += 1

#usando controle de fluxo > break e continue
#para cada numero num range de 5
for i in range(5):
    #chegando em 10...
    if i == 10:
        break #sair do looping assim que executado, ou seja chegando a 5
    elif i %2 == 0:
        continue# continua
    print(i)
