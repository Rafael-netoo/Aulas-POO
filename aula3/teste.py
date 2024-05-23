import requests


print("Verificando o cep")
cep = input("Digite o cep : ")

if (len(cep) !=8):
    print("Cep inválido!")
    exit()
consulta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

print(consulta.json())