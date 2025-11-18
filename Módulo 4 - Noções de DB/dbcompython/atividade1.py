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
    
    cursor.execute("""
    SELECT
    e.id_emp, e.matricula, e.pr_nome || ' ' || e.sobre_nome AS nome_funcionario, sexo, e.salario, e.comissao, 
    c.nome_cargo,
    d.nome_dept
    FROM empregados e
    JOIN cargos c ON e.id_cargo = c.id_cargo
    JOIN departamentos d ON e.id_dept = d.id_dept;
    """)
    # cursor.fetchall pega o resultado do ultimo select
    resultados = cursor.fetchall()
 # Exibindo os dados
    for res in resultados:
        print(f"ID: {res[0]}, Matrícula: {res[1]}, Nome: {res[2]}, Sexo: {res[3]}, Salário: R${res[4]}, Comissão: {res[5]}, Cargo: {res[6]}, Departamento: {res[7]}")
except Exception as e:
 print("Erro ao consultar o banco:", e)
# Fechando conexões
if cursor:
 cursor.close()
if conn:
 conn.close()
