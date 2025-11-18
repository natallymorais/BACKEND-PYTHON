import psycopg2

class UsuarioModel:
    def __init__(self):
        try:
            self.conexao = psycopg2.connect(
            host="localhost",
            database="meu_banco",
            user="postgres",
            password="admin"
            )
        except Exception as e:
            print("Erro ao conectar ao banco:", e)
            
    def listar_usuarios(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT id, nome, email FROM usuarios ORDER BY id;")
            usuarios = cursor.fetchall()
            cursor.close()
            return usuarios
        except Exception as e:
            print("Erro ao listar usuários:", e)
            return []
        
    def inserir_usuario(self, nome, email):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s);", (nome, email))
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            print("Erro ao inserir usuário:", e)
        # sempre usar rollback() quando cair na exeção
            self.conexao.rollback()
        
    def atualizar_usuario(self, id_usuario, nome, email):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("UPDATE usuarios SET nome = %s, email = %s WHERE id = %s;", (nome, email, id_usuario))
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            print("Erro ao atualizar usuário:", e)
        # sempre usar rollback() quando cair na exeção
            self.conexao.rollback()
            
    def excluir_usuario(self, id_usuario):
        try:
            cursor = self.conexao.cursor()
            # quando é passado só um parametro sempre colocar uma virgula no final porque sim.
            cursor.execute("DELETE FROM usuarios WHERE id = %s;", (id_usuario,))
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            print("Erro ao excluir usuário:", e)
            self.conexao.rollback()