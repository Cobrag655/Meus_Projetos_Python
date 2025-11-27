#utilizando while, true, try, loop, break e except.

#variaveis

#looping
while True:
    #tenta converter a entrada para inteiro
    try:
        idade = int(input("Digite sua idade:\n"))
        if 0 <= idade <= 100: #a idade esta entre 0 e 120
            print(f"Idade Valida {idade} anos")
            break#trava o codigo
        else:
            print("Idade Idade Invalida, insira uma idade entre 0 e 100.")
    except ValueError: #exceto que ele coloque algo sem ser um numero
        print("Insira um numero inteiro")
        False

#indentaçao
# while True:
#     try:
#         ...
#     except ...: