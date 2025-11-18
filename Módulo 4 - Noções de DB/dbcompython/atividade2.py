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
    
    cursor = conn.cursor()
    
    cursor.executemany("
    DELETE FROM cargos WHERE id_emp = %s", cargo))


    conn.commit()
    print("Registros excluídos com sucesso!")
    print("Cargo inserido com sucesso!")
    
except Exception as e:
 print("Erro ao inserir cargo:", e)
 conn.rollback()
if cursor:
 cursor.close()
if conn:
 conn.close()
 