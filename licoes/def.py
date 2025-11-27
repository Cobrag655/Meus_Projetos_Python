#o nome e o nome da funçao enquanto o entre () e os parametros que aquela funçao sera realizada
def nome(parametro, parametro2):
    #bloco qeu executa algo dentro dessa funçao
    resultado = (parametro + parametro2)
    #retorna o "resultado"
    return resultado

#variaveis
parametro = int(input())
parametro2 = int(input())
#mostra a soma
print(nome(parametro, parametro2))


#jeito diferente
# def saudacao(nome):
#     print(f"{nome}, Seja bem vindo ao nosso pais!")
#     return

# saudacao("Gabriell")

# #outra forma
# #funçao docs (parametro padrao)
# def cu(nome = "amigo"):
#     print(f"Ola, {nome}")

# cu() #ele vai usar o padrao pre estabelecido la em cima