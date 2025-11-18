# entrada e vizualização de dados
class ProdutoView:
    @staticmethod
    def menu_principal():
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Listar produtos cadastrados")
        print("2 - Cadastrar novo produto(nome e preço)")
        print("3 - Atualizar produto existente")
        print("4 - Excluir produto pelo ID")
        print("0 - Sair")
        try:
            return int(input("\nEscolha uma opção: "))
        except ValueError:
            print('Entrada inválida. Digite um número.')
            return -1
        
    @staticmethod
    def mostrar_produtos(produtos):
        if not produtos:
            print("Nenhum produto encontrado.")
        else:
            print("\n=== Lista de Produtos ===")
            for produto in produtos:
                print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: {produto[2]:.2f}")
    @staticmethod           
    def solicitar_dados_produto():
        nome = input("Nome: ")
        try:
            preco = float(input("Preço: "))
            return nome, preco # pode retornar n valores de uma vez só
        except Exception as e:
            print(f'\nValor inválido')
            return None, None
    
    @staticmethod
    def solicitar_id():
        try:
            id_produto = int(input("ID do produto: "))
            nome = input('Novo nome: ')
            preco = float(input('Novo preço: '))
        except ValueError:
            print("\nEntrada inválido!")
            return None, None
        
    @staticmethod
    def excluir():
        try:
            id_produto = int(input("ID do produto: "))
            return id_produto
        except ValueError:
            print("\nEntrada inválido!")
            return None
        
    def mensagem(texto): # impressão generica
        print(texto)