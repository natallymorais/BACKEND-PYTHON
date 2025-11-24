import requests
import json

def consultaAPI():
    url = "http://localhost:8000/api/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao acessar a API: {response.status_code}")
        return []
    
def formataResposta(pessoas):
    return (
    f"\nID: {pessoas['id']}\n"
    f"Nome: {pessoas['nome']}\n"
    f"Email: {pessoas['email']}\n"
    f"Telefone: {pessoas['telefone']}\n"
    f"Cidade: {pessoas['cidade']}\n")
    
def main():
    pessoas = consultaAPI()
    print("\n===Lista de Pessoas da API:===\n")
    for pessoa in pessoas:
        print(formataResposta(pessoa))
        print("-"*40)
        
        
if __name__ == "__main__":
    main()