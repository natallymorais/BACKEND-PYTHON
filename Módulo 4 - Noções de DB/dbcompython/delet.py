import psycopg2

try:
 # Conectando ao banco de dados
    conn = psycopg2.connect(
    dbname="empresabd", # substituir pelos dados do seu banco
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
    )
    
#  Delete com python:
    
    cursor = conn.cursor()
 # Executando os DELETEs
    cursor.execute("DELETE FROM empregados WHERE id_emp = %s", (14,)) # Verificar os IDs na tabela e substituir aqui
    cursor.execute("DELETE FROM empregados WHERE id_emp = %s", (15,))
    conn.commit()
    print("Registros excluídos com sucesso!")
except Exception as e:
 print("Erro ao excluir registros:", e)
 conn.rollback()
if cursor:
 cursor.close()
if conn:
 conn.close()
