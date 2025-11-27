#conjuntos
veiculo = {
    "carro",
    "moto",
    "bike",
}

#add
veiculo.add("barco")
print(veiculo)

#adicionando um elemento repetido
veiculo.add("barco") #sem erro e o outro barco nao aparece
veiculo.remove("moto") #remove algo


#pega dois dic e compara eles mostrando apenas a diferença
veiculo_a = {
    "caminhao",
    "onibus",
    "moto"
} 

veiculos_b = {
    "caminhao",
    "onibus",
    "bike"
}

diferenca = veiculo_a.difference(veiculos_b)# a.difference(b)
print(diferenca)

#uniao de dois ou mais conjuntos
uniao = veiculo_a.union(veiculos_b)# unifica os dics sem repetir itens
print(uniao)


print(f"Conjunto Original: {veiculo}")

#limpando um conjunto usando clear()
veiculo.clear()
print(f"Conjunto pos clear(): {veiculo}")