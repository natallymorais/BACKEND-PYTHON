import requests

# URL do endpoint de autores
url = 'http://localhost:8000/api/autores/'
# Requisição GET sem autenticação (permitida conforme sua configuração)
response = requests.get(url)
# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    autores = response.json()# lista de autores em formato JSON
    # Imprime os autores obtidos
    for autor in autores:
        print(f"ID: {autor['id']} | Nome: {autor['nome']}")
else:
    print(f"Erro: {response.status_code}")# imprime o código de erro se a requisição falhar