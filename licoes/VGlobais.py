#variavies globais e locais

contador = 0

def incrementar():
    #global puxa uma variavel global do codigo
    global contador
    contador += 1
    print(f"Contador: {contador}")


#chamando a funçao varias vezes (global pode ser chamada varias vezes)
incrementar()
incrementar()
incrementar()
