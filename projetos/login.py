#sistema de login

#variaveis
usuario = "admin" , "pedro" , "manuel" , "gabriell"
senha = "papagaio" , "5656" , "sim" , "thiago"

#definindo as credenciais corretas
usuario_correto = "admin" , "pedro" , "manuel" , "gabriell"
senha_correta = "papagaio" , "5656" , "sim" , "thiago"

#realizando as comparaçoes
credenciais_validas = (usuario == usuario_correto) and (senha == senha_correta)

#utilizando "Or"
acesso_negado = (usuario != usuario_correto) or (senha != senha_correta)

#not
acesso_permitido = not acesso_negado

print(f"credenciais validas: {credenciais_validas}")
print(f"acesso negado: {acesso_negado}")
print(f"acesso permitido: {acesso_permitido}")


user = input("Qual o login?:\n")
password = input("Qual a senha correta?:\n")

def senhas(user, password, usuario, senha):
    if user  == usuario:
        print("login correto")
        if password == senha:
            print("senha correta")
            print("seu login esta autorizado")
    elif user or password != credenciais_validas:
        print("Login/senha errados, tente novamente")

senhas(user, password, usuario, senha)
