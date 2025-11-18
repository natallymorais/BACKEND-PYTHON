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
 # Atualizando salário e comissão
    cursor.execute("""
    UPDATE empregados
    SET salario = %s, comissao = %s
    WHERE id_emp = %s
    """, (5500.00, 400.00, 3)) # Verificar ID do funcionário na tabela
    conn.commit()
    print("Empregado atualizado com sucesso!")
except Exception as e:
 print("Erro ao atualizar empregado:", e)
 conn.rollback()
if cursor:
 cursor.close()
if conn:
 conn.close()