# conexão com o banco
import psycopg2

class ProdutoModel:
    def __init__(self):
        try:
            self.conexao = psycopg2.connect(
            host="localhost",
            database="produtosdb",
            user="postgres",
            password="admin"
            )
        except Exception as e:
            print("Erro ao conectar ao banco:", e)
            
    def listar_produto(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT id, nome, preço FROM produto ORDER BY id;")
            usuarios = cursor.fetchall()
            cursor.close()
            return usuarios
        except Exception as e:
            print("Erro ao listar produtos:", e)
            return []
        
    def inserir_produto(self, nome, preco):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("INSERT INTO produto (nome, preco) VALUES (%s, %s);", (nome, preco))
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            print("Erro ao inserir produto:", e)
        # sempre usar rollback() quando cair na exeção
            self.conexao.rollback()
          
    def existe_id (self, id_produto):
        try:
            self.cursor.execute("select 1 from produto where id=%s;", (id_produto))
            return self.cursor.fetchone is not None
        except Exception as e:
            print("Erro ao verificar a existência do produto: {e}\n")
            return False
            
    def atualizar_produto(self, id_produto, nome, preco):
        try:
            if not self.existe_id(id_produto):
                print("\nNenhum  produto encontrado com esse ID\n")
                return False
        
            cursor = self.conexao.cursor()
            cursor.execute("UPDATE produto SET nome = %s, preco = %s WHERE id = %s;", (nome, preco, id_produto))
            self.conexao.commit()
            cursor.close()
            print("Erro ao atualizar produto:", e)
            # sempre usar rollback() quando cair na exeção
            self.conexao.rollback()
        except Exception as e:
            print(f'\nErro ao atualizar produto: {e}\n')
            self.conexao.rollback()
            return False
        
    def excluir_produto(self, id_produto):
        try:
            if not self.existe_id(id_produto):
                print("\nNenhum  produto encontrado com esse ID\n")
                return False
        
            cursor = self.conexao.cursor()
            cursor.execute("delete from produto WHERE id = %s;", (id_produto))
            self.conexao.commit()
            cursor.close()
            print("Erro ao excluir produto:", e)
            # sempre usar rollback() quando cair na exeção
            self.conexao.rollback()
        except Exception as e:
            print(f'\nErro ao excluir produto: {e}\n')
            self.conexao.rollback()
            return False
        
        #sempre colocar no model um afunção "destrutor" 
    def __del__(self):
        if hasattr(self, "cursor") and hasattr(self, "conn"):
            self.cursor.close()
            self.conn.close()