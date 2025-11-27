# #open()
# # arquivo = open("nome do arquivo", "modo") #modo pode ser r, w, a, b, r=leitura, w=escrita, a=aacrecenta e b=modo binario etc
# #abrindo arquivo para leitura
# arquivo = open("Gabs.txt", "r", encoding='utf-8')
# #Lendo o arquivo
# conteudo = arquivo.read()
# print(conteudo)

# #fechando arquivo
# arquivo.close()

#abrindo um arquivo para escrita ou criando se nao existir.
# arquivo = open("mama.txt", "w")

# #reescrevendo o arquivo
# arquivo.write("Este e o novo arquivo\npnc")

# #fechando
# arquivo.close()

#abrindo o arquivo em modo de ediçao cm (append)
# arquivo = open("Cu.txt", "w")
# arquivo = open("Cu.txt", "a")

# #reescrevendo
# arquivo.write("Trabalhando com append em txt")

# #fechando
# arquivo.close()

#abrindo um arquivo usando with (fechamento automatico)
# with open("cu.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

#abrindo um arquivo no (modo texto "t")
# with open("gab.txt", "wt", encoding="utf-8") as arquivo:
#     #escrevendo no arquivo
#     arquivo.write("Este e um arquivo de texto.\n")
#     arquivo.write("Estamos escrevendo no modo texto ('t').\n")
#     arquivo.write("python facilita o manuseio de arquivos.\n")


# #Abrindo para leitura (modo texto "t")
# with open("gab.txt", "rt", encoding="utf-8") as arquivo:
#     #lendo o arquivo
#     conteudo = arquivo.read()

#     print("Conteudo do arquivo\n")
#     print(conteudo)

#planilhia excel/ plan / resultado / html-css / m10
#                   nome doc        plan        compo


