import pyodbc

dados_conexao = (
"Driver={SQL Server};"
"Server=localhost\SQLEXPRESS;"
"Database=Master;"
)
try:
    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()
    print("Conexão bem-sucedida!")

except Exception as e:
    print("Erro ao conectar ao banco de dados:", e)
    exit()


operacao = int(input("Qual operação desejada? Ler(1) Adicionar(2) Excluir(3)"))

#operação ler
if operacao == 1:
    tabela = int(input("Escolha a tabela: Estudante(1) Emprestimo(2) Instituições Financeiras(3) Contratos(4): "))
    
    match tabela:
        case 1:
            comando = """SELECT * FROM estudante"""
            cursor.execute(comando)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        case 2:
            comando = """SELECT * FROM emprestimo"""  
            cursor.execute(comando)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        case 3:
            comando = """SELECT * FROM instituicoes_financeiras"""  
            cursor.execute(comando)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        case 4:
            comando = """SELECT * FROM contratos"""  
            cursor.execute(comando)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        case _:
            print("Opção inválida. Tente novamente.")








cursor.close()
conexao.close()