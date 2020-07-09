import requests

def retorna_cep():
    response = requests.get('https://viacep.com.br/ws/05187631/json')
    print(response)
    print(response.text)
    dados_cpe = response.json()
    print(dados_cpe['cep'])
    return dados_cpe


if __name__ == '__main__':
    retorna_cep()