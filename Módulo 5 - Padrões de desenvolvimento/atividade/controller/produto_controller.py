from model.produto_model import ProdutoModel
from view.produto_view import ProdutoView

class ProdutoController:
    def __init__(self): # construtor
        self.model = ProdutoModel()
        self.model = ProdutoView()
    
    def executar(self):
       while True:
           opcao = self.view.menu()
           if opcao == 1:
               produtos = self.view.listar()
               self.view.listar(produtos)  
               
           elif opcao == 2:
               nome, preco = self.view.cadastrar()
               if nome and preco:
                   self.model.inserir(nome, preco)
                   self.view.mensagem('\nproduto cadastrado com sucesso!\n')
           
           elif opcao == 3:
               id_produto, nome, preco = self.view.atualizar()
               if id_produto and nome and preco:
                   sucesso = self.model.atualizar(id_produto)
                   if sucesso:
                       self.view.mensagem('\nProduto atualizado com sucesso!')
                   else:
                       self.view.mensagem("Falha ao atualizar produto.")
            
           elif opcao == 4:
               id_produto, nome, preco = self.view.atualizar()
               if id_produto and nome and preco:
                   sucesso = self.model.atualizar(id_produto)
                   if sucesso:
                       self.view.mensagem('\nProduto atualizado com sucesso!')
                   else:
                       self.view.mensagem("Falha ao atualizar produto.")
            
           elif opcao == 0:
               self.view.mensagem("\nSaindo do sistema\n")
               
           else:
                
                
    