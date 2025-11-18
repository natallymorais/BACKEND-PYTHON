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
    
#  Insert com python:

    cursor = conn.cursor()
 # Lista de empregados a serem inseridos
    empregados = [
    (1007, 'Inocêncio', 'Coitadinho da Silva', 'M', 5000.00, None, 4, 3),
    (1008, 'Luciana', 'Ferraz', 'F', 3800.00, 200.00, 3, 1),
    (1009, 'Eduardo', 'Pereira', 'M', 2500.00, None, 1, 4)
    ]
# Executando os INSERTs com executemany para inserir várias de uma vez
    cursor.executemany("""
    INSERT INTO empregados (
    matricula, pr_nome, sobre_nome, sexo, salario, comissao, id_cargo, id_dept
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, empregados)
    conn.commit()
    print("Empregados inseridos com sucesso!")
except Exception as e:
 print("Erro ao inserir empregados:", e)
 conn.rollback()
if cursor:
 cursor.close()
if conn:
 conn.close()