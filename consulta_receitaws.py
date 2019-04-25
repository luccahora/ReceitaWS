import requests
import csv
import time

def ler_csv():
    Resultado = [] 
    with open('empresas.csv','r',encoding='utf-8-sig') as csvfile: 
        reader = csv.DictReader(csvfile,delimiter=";",lineterminator="\n")
        for row in reader:
            Resultado.append(row)   
    return Resultado

lista_empresa = ler_csv()
lista_cnpj = ["13347016000117","19518764000100"] # Caso queira importar o cnpj SEM csv, adiciona aqui.

for cnpj in lista_cnpj: # Caso queira usar o csv, troca o (lista_cnpj) por (lista_empresa) 
    time.sleep(1) # O receita WS, no modo free faz 3 consultas por minuto. Então caso esteja usando o modo free recomendo alterar o time para 30 ou mais. time.sleep(31) 
    url = "https://www.receitaws.com.br/v1/cnpj/" + (cnpj) # Caso tenha usado o csv, trocar o (cnpj) por (cnpj['cnpj'])
    conteudo = requests.request("GET", url)
    conteudo = conteudo
    print(conteudo.text)
    
    arquivo = open('saidajson.txt','a')
    arquivo.write(conteudo.text)
    arquivo.write('\n')
   