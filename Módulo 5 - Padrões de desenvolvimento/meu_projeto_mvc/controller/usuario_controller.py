# importa a classe
from model.usuario_model import UsuarioModel
# importa todas as funções 
from view.usuario_view import *

# conexão entre todos
class UsuarioController:
    def __init__(self): # construtor
        self.model = UsuarioModel()
        
    def listar(self):
        try:
            usuarios = self.model.listar_usuarios()
            mostrar_usuarios(usuarios)
        except Exception as e:
            mensagem(f"Erro ao listar usuários: {e}")
            
    def cadastrar(self):
        try:
            nome, email = solicitar_dados_usuario()
            if not nome or not email:
                mensagem("Nome e e-mail são obrigatórios!")
                return
            self.model.inserir_usuario(nome, email)
            mensagem("\nUsuário cadastrado com sucesso!\n")
        except Exception as e:
            mensagem(f"\nErro ao cadastrar usuário: {e}\n")
            
    def atualizar(self):
        try:
            id_usuario = solicitar_id()
            if id_usuario is None:
                return
            nome, email = solicitar_dados_usuario()
            self.model.atualizar_usuario(id_usuario, nome, email)
            mensagem("\n ✏️ Usuário atualizado com sucesso!\n") 
        except Exception as e:
            mensagem(f"\nErro ao atualizar usuário: {e}\n")
            
    def excluir(self):
        try:
            id_usuario = solicitar_id()
            if id_usuario is None:
                return
            self.model.excluir_usuario(id_usuario)
            mensagem("Usuário excluído com sucesso!")
        except Exception as e:
            mensagem(f"Erro ao excluir usuário: {e}")