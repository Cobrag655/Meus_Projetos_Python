#Mexendo com bibli
#precisa importar a bibli adequada
# import pandas as pd

# #lendo o documento .xlsx (excel)
# df = pd.read_excel("plan_py.xlsx", sheet_name="Douglas")

# #printa/ .head() puxa 5 linhas por padrao, podendo ser definido quantas linhas quiser.
# print(df.head(6))

#imprtacao
import openpyxl
from openpyxl import Workbook
import os

arquivo = "banco.xlsx"

#se o arquivo nao existir cria outro
if not os.path.exists(arquivo):
    wb = Workbook()
    ws = wb.active
    ws.title = "Alunos"

    #cabeçario para planilhas
    ws.append(["Nome", "Idade", "Nota"])
    wb.save(arquivo)

#abrindo o arquivo existente
wb = openpyxl.load_workbook(arquivo)
ws = wb["Alunos"]

#add as info (dic)
alunos = [
    ["Gabriell", 16, 8.5],
    ["Pedro", 18, 7.0],
    ["Guilherme", 17, 8.5]
]
for aluno in alunos:
    ws.append(aluno)

#salvando o documento
wb.save(arquivo)


print("Dados add com sucesso!, em arquivo")
