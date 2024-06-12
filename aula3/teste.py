import requests
import json
import mysql.connector

banco = mysql.connector.connect(
    host = "localHost",
    user = "root",
    password="123456",
    database = "desafioFinal"
)


def retornaConsulta():
    print("Verificando o cep")
    cep = input("Digite o cep : ")
    if (len(cep) !=8):
        print("Cep inválido!")
        exit()
    return requests.get(f'https://viacep.com.br/ws/{cep}/json/')

requisicao = retornaConsulta()
endereco = requisicao.json()

nome = input("Digite o seu nome: ")

cep = endereco['cep']
logradouro = endereco['logradouro']
complemento = endereco['complemento']
bairro = endereco['bairro']
localidade = endereco['localidade']
uf = endereco['uf']

cursor  = banco.cursor()
sql = "insert into clientes(nome, cep, logradoruro, complemento, bairro, localidade, uf) values (%s,%s, %s,%s, %s,%s, %s)"
data = (nome, cep, logradouro, complemento, bairro, localidade, uf)

cursor.execute(sql,data)
banco.commit()
