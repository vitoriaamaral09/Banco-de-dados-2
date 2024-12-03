import pyodbc

dados_conexao = (
"Driver={SQL Server};"
"Server=localhost\SQLEXPRESS;"
"Database=model;"
)
try:
    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()
    print("Conexão bem-sucedida!")

except Exception as e:
    print("Erro ao conectar ao banco de dados:", e)
    exit()


operacao = int(input("Qual operação desejada? Ler(1) Adicionar(2) Excluir(3) Editar(4)"))

#operação select
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

#operação insert
elif operacao == 2:
    tabela = int(input("Escolha a tabela: Estudante(1) Emprestimo(2) Instituições Financeiras(3) : "))

    match tabela:
        case 1:
            try:
                id_estudante = int(input("Digite o ID do estudante: "))
                nome = input("Digite o nome do estudante: ")
                email = input("Digite o email do estudante: ")
                curso = input("Digite o curso do estudante: ")
                data_entrada = input("Digite a data de entrada (YYYY-MM-DD): ")

                comando = """INSERT INTO estudante (id_estudante, nome, email, curso, data_entrada)
                             VALUES (?, ?, ?, ?, ?)"""
                cursor.execute(comando, (id_estudante, nome, email, curso, data_entrada))
                conexao.commit()
                print("Informação cadastrada com sucesso")

            except Exception as e:
                print('Erro ao cadastras dado')
            
        case 2:
            try:
                id_emprestimo = int(input("Digite o ID do empréstimo: "))
                id_estudante = int(input("Digite o ID do estudante: "))
                valor_emprestimo = float(input("Digite o valor do empréstimo: "))
                data_inicio = input("Digite a data de início (YYYY-MM-DD): ")
                data_vencimento = input("Digite a data de vencimento (YYYY-MM-DD): ")
                taxa_juros = float(input("Digite a taxa de juros: "))

                comando = """INSERT INTO emprestimo (id_emprestimo, id_estudante, valor_emprestimo, data_inicio, data_vencimento, taxa_juros)
                             VALUES (?, ?, ?, ?, ?, ?)"""
                cursor.execute(comando, (id_emprestimo, id_estudante, valor_emprestimo, data_inicio, data_vencimento, taxa_juros))
                conexao.commit()
                print("Informação cadastrada com sucesso")
            except Exception as e:
                print('Erro ao cadastras dado')
        case 3:
            try:
                id_instituicao = int(input("Digite o ID da instituição: "))
                id_emprestimo = int(input("Digite o ID do empréstimo associado: "))
                nome_instituicao = input("Digite o nome da instituição: ")
                taxa_base = float(input("Digite a taxa base: "))

                comando = """INSERT INTO instituicoes_financeiras (id_instituicao, id_emprestimo, nome_instituicao, taxa_base)
                             VALUES (?, ?, ?, ?)"""
                cursor.execute(comando, (id_instituicao, id_emprestimo, nome_instituicao, taxa_base))
                conexao.commit()
                print("Informação cadastrada com sucesso")

            except Exception as e:
                print('Erro ao cadastras dado')
        
        case _:
            print("Opção inválida. Tente novamente.")


elif operacao == 3:
    tabela = int(input("Escolha a tabela: Estudante(1) Emprestimo(2) "))
    match tabela :
        case 1:
            try:
                id_estudante = int(input("Digite o ID do estudante: "))
                comando = """delete from estudante where id_estudante = ?"""
                cursor.execute(comando, (id_estudante,))
                conexao.commit()
                print("Informação deletada com sucesso")

            except Exception as e:
                print('Esse id não existe')

        case 2:
            try:
                id_emprestimo = int(input("Digite o ID do emprestimo: "))
                comando = """delete from emprestimo where id_emprestimo = ?"""
                cursor.execute(comando, (id_emprestimo,))
                conexao.commit()
                print("Informação deletada com sucesso")

            except Exception as e:
                print('Esse id não existe')
        case _ :
             print("Opção inválida. Tente novamente.")


elif operacao == 4:
    tabela = int(input("Escolha a tabela: Estudante(1)"))
    match tabela :
        case 1:
            try:
                id_estudante = int(input("Digite o ID do estudante: "))
                nome = input("Qual o nome do estudante?")
                email = input("Qual o email do estudante?")
                curso = input("Qual o curso do estudante?")
                data_entrada = input("Qual a data de entrada?")
                comando = """update estudante
                                set nome = ?, 
                                email = ?, curso = ?, 
                                data_entrada = ?
                                where id_estudante = ?"""
                cursor.execute(comando,( nome, email, curso, data_entrada, id_estudante))
                conexao.commit()
                print("Informação atualizada com sucesso")

            except Exception as e:
                print('Erro ao atualizar dado')



        case _:
             print("Opção inválida. Tente novamente.")


else:
    print('Operação Invalida')

cursor.close()
conexao.close()
print("Conexão Finalizada")