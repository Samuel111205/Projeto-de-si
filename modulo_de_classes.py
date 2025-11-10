import banco_de_funcionarios
from datetime import datetime

#classe banco
class Banco:
    def __init__(self):
        self.banco=banco_de_funcionarios

    def conectar(self):
        return banco_de_funcionarios.conectar()

#Classe departamento
class Departamento:
    def __init__(self, banco):
        self.banco=banco

    def cadastrar_departamento(self,nome,localizacao):
        conn=self.banco.conectar()
        cursor=conn.cursor()

        try:
            cursor.execute("""INSERT INTO departamentos (nome_departamento,localizacao)
             VALUES (?, ?)""",(nome,localizacao)
            )
            conn.commit()
            conn.close()
        except:
            print("Erro ao tentar cadastrar departamento")

    def listar_departamento(self):
        conn=self.banco.conectar()
        cursor=conn.cursor()

        cursor.execute("SELECT departamento_id,nome_departamento FROM departamentos ORDER BY nome_departamento")
        dep=cursor.fetchall()
        if dep:
            print("==========Departamentos==========")
            for i in dep:
                print(f"Id: {i[0]}| Nome: {i[1]}")
            print("="*25)
            conn.close()

        else:
            print("Nenhum departamento cadastrado")

    def deletar_departamento(self,id_departamento):
        conn=self.banco.conectar()
        cursor=conn.cursor()

        cursor.execute("DELETE FROM departamentos WHERE departamento_id=?",(id_departamento,))
        conn.commit()
        conn.close()
        print("Departamento cadastrado com sucesso")


#Classe cargo
class Cargo:
    def __init__(self,banco):
        self.banco=banco

    def cadastrar_cargo(self,nome_cargo):
        conn=self.banco.conectar()
        cursor=conn.cursor()

        cursor.execute("INSERT INTO cargos (nome_cargo) VALUES (?)",(nome_cargo,))
        conn.commit()
        conn.close()
        print("Cargo cadastrado com sucesso")

    def listar_cargo(self):
        conn=self.banco.conectar()
        cursor=conn.cursor()

        cursor.execute("SELECT cargo_id,nome_cargo FROM cargos ORDER BY nome_cargo")
        cargo=cursor.fetchall()
        if cargo:
            print("========== Cargos ==========")
            for i in cargo:
                print(f"Id: {i[0]}| Nome: {i[1]}")
            print("="*25)
            conn.close()

        else:
            print("Nenhum cargo cadastrado")

    def deletar_cargo(self,id_cargo):
        conn=self.banco.conectar()
        cursor=conn.cursor()

        cursor.execute("DELETE FROM cargos WHERE cargo_id=?",(id_cargo,))
        conn.commit()
        conn.close()


#Classe funcionarios
class Funcionario:
    def __init__(self,banco):
        self.banco=banco

    def cadastrar(self,nome,data_nascimento,genero,estado_civil,email,telefone,data_admissao,departamento_id,cargo_id):
        conn=self.banco.conectar()
        cursor=conn.cursor()

        cursor.execute("""
            INSERT INTO funcionarios(
                nome,
                data_nascimento,
                genero,estado_civil,
                email,
                telefone,
                data_admissao,
                departamento_id,
                cargo_id
            )
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,(nome,data_nascimento,genero,estado_civil,email,telefone,data_admissao,departamento_id,cargo_id))
        conn.commit()
        conn.close()
        print(f"Funcionario {nome} cadastrado com sucesso")

    def listar_funcionario(self):
        conn=self.banco.conectar()
        cursor = conn.cursor()
        # Consulta SQL com JOINs para trazer o nome do departamento e cargo
        cursor.execute("""
            SELECT 
                f.funcionario_id,
                f.nome,
                d.nome_departamento,
                c.nome_cargo
            FROM funcionarios f
            LEFT JOIN departamentos d ON f.departamento_id = d.departamento_id
            LEFT JOIN cargos c ON f.cargo_id = c.cargo_id ORDER BY f.nome;
        """)

        # Buscar todos os registros
        funcionarios = cursor.fetchall()

        print("\n--- LISTA DE FUNCIONÁRIOS (COM DEPARTAMENTO E CARGO) ---")
        if funcionarios:
            for f in funcionarios:
                print(f"ID: {f[0]}| Nome: {f[1]}| Departamento: {f[2] if f[2] else 'Não atribuído'}| Cargo: {f[3] if f[3] else 'Não atribuído'}")
        else:
            print("Nenhum funcionário cadastrado.")
        conn.close()

    def ver_dados_de_um_funcionario(self,nome):
        conn=self.banco.conectar()
        cursor=conn.cursor()

        cursor.execute("""
            SELECT 
                nome,
                data_nascimento,
                genero,
                estado_civil,
                email,
                telefone
            FROM funcionarios
            WHERE nome LIKE?
        """,(f"%{nome}%",))
        dados=cursor.fetchall()

        if dados:
            print(f"\t  ======Dados pessoais do/a {nome}=======")
            for i in dados:
                print(f"""
                    Nome: {i[0]}
                    Data de nascimento: {i[1]}
                    Genero: {i[2]}
                    Estado civil: {i[3]}
                    Email: {i[4]}
                    Nºtelefone: {i[5]}
                """)

            conn.close()
        else:
            print(f"Funcionario {nome} não foi encotrado na base de dados")

    def ver_por_departamento(self,departemento_nome):
        conn=self.banco.conectar()
        cursor=conn.cursor()

        cursor.execute("""
            SELECT
                f.nome,
                c.nome_cargo
            FROM funcionarios f
            LEFT JOIN cargos c ON f.cargo_id=c.cargo_id
            LEFT JOIN departamentos d ON f.departamento_id=d.departamento_id
            WHERE d.nome_departamento LIKE ?
        """,(f"%{departemento_nome}%",))

        registro=cursor.fetchall()
        if registro:
            for i in registro:
                print(f"Nome: {i[0]}| Cargo: {i[1]}")
            conn.close()

        else:
            print("Nenhum funcionario cadastrado neste departamento ou o departamento não existe")

    def atualizar_funcionario(self):
        conn=self.banco.conectar()
        cursor=conn.cursor()

        funcionario_id=int(input("Digite o id do aluno que deseja atualizar: "))

        cursor.execute("SELECT nome FROM funcionarios WHERE funcionario_id=?",(funcionario_id,))
        registros=cursor.fetchone()
        if not registros:
            print("Funcionario não encotrado")
            conn.close()
            return

        print(f"Atuanlizando os dados de {registros[0]}")

        # Menu de opções
        print("""
        1 - Atualizar Email
        2 - Atualizar Telefone
        3 - Atualizar Departamento
        4 - Atualizar Cargo
        """)
        opcao = input("Escolha o que deseja atualizar: ")

        if opcao == "1":
            novo_email = input("Novo email: ")
            cursor.execute("UPDATE funcionarios SET email = ? WHERE funcionario_id = ?", (novo_email, funcionario_id))

        elif opcao == "2":
            novo_telefone = input("Novo telefone: ")
            cursor.execute("UPDATE funcionarios SET telefone = ? WHERE funcionario_id = ?", (novo_telefone, funcionario_id))

        elif opcao == "3":
            cursor.execute("SELECT departamento_id,nome_departamento FROM departamentos ")
            dep = cursor.fetchall()
            if dep:
                print("==========Departamentos==========")
                for i in dep:
                    print(f"Id: {i[0]}| Nome: {i[1]}")
                print("=" * 25)
            else:
                print("Nenhum departamento cadastrado")

            novo_dep = input("Novo ID de departamento: ")
            cursor.execute("UPDATE funcionarios SET departamento_id = ? WHERE funcionario_id = ?", (novo_dep, funcionario_id))

        elif opcao == "4":
            cursor.execute("SELECT cargo_id,nome_cargo FROM cargos ")
            cargo = cursor.fetchall()
            if cargo:
                print("========== Cargos ==========")
                for i in cargo:
                    print(f"Id: {i[0]}| Nome: {i[1]}")
                print("=" * 25)
            else:
                print("Nenhum departamento cadastrado")
            novo_cargo = input("Novo ID de cargo: ")
            cursor.execute("UPDATE funcionarios SET cargo_id = ? WHERE funcionario_id = ?", (novo_cargo, funcionario_id))

        else:
            print("Opção inválida.")
            conn.close()
            return

        conn.commit()
        print("✅ Dados atualizados com sucesso!")
        conn.close()

    def deletar_funcionario(self, funcionario_id):
        conn=self.banco.conectar()
        cursor=conn.cursor()

        cursor.execute("DELETE FROM funcionarios WHERE funcionario_id=?",(funcionario_id,))
        print("funcionario deletado com sucesso")
        conn.commit()
        conn.close()


#Classe presenças
class Presencas:
    def __init__(self,banco):
        self.banco=banco

    def cadastrar_presencas(self,id_funcionario,hora_entrada,hora_saida,turno):
        conn=self.banco.conectar()
        cursor=conn.cursor()

        agora=datetime.now()
        data=agora.date()

        cursor.execute("""
            INSERT INTO presencas(
                funcionario_id,
                data,
                hora_entrada,
                hora_saida,
                turno,
                presente
            )
            VALUES (?, ?, ?, ?, ?)
        """,(id_funcionario,data,hora_entrada,hora_saida,turno))
        conn.commit()
        conn.close()

    def listar_presenca(self):
        conn=self.banco.conectar()
        cursor=conn.cursor()

        cursor.execute("""
            SELECT 
                presenca_id,
                f.nome, 
                p.data, 
                p.hora_entrada, 
                p.hora_saida, 
                p.turno
            FROM presencas p 
            LEFT JOIN funcionarios f ON p.funcionario_id= f.funcionario_id;
        """)
        presenca=cursor.fetchall()

        if presenca:
            for i in presenca:
                print(f"Id: {i[0]}| Nome: {i[1]}| Data: {i[2]}| Hora de entrada: {i[3]}| Hora de saida: {i[4]}| Turno: {i[5]}")
            conn.close()

        else:
            print("Presença não encotrado")



#Classe licença
class Licenca:
    def __init__(self,banco):
        self.banco=banco

    def cadastrar_licenca(self,funcionario_id,tipo_licenca,data_inicio,data_fim,estado):
        conn=self.banco.conectar()
        cursor=conn.cursor()

        cursor.execute("""
            INSERT INTO licenca(
                funcionario_id,
                tipo_licenca,
                data_inicio,
                data_fim,
                estado
            )
            VALUES (?, ?, ?, ?, ?)
        """,(funcionario_id,tipo_licenca,data_inicio,data_fim,estado))
        conn.commit()
        conn.close()

    def listar_licencas(self):
        conn=self.banco.conectar()
        cursor=conn.cursor()

        cursor.execute("""
            SELECT 
                l.licenca_id,
                f.nome,
                l.tipo_licenca,
                l.data_inicio,
                l.data_fim,
                l.estado
            FROM licenca l
            LEFT JOIN funcionarios f ON l.funcionario_id=f.funcionario_id;
        """)
        licenca=cursor.fetchall()

        if licenca:
            for i in licenca:
                print(f"Id: {i[0]}| Nome: {i[1]}| Tipo de Contrato: {i[2]}| Data de inicio: {i[3]}| Data do fim: {i[4]}| Estado: {i[5]}")
            conn.close()

        else:
            print("Nenhuma licença cadastrada")


#classe Salario
class Salario:
    def __init__(self,banco):
        self.banco=banco

    def cadastrar_salario(self,funcionario_id,valor):
        conn=self.banco.conectar()
        cursor=conn.cursor()

        cursor.execute("""
            INSERT INTO salario(
                funcionario_id,
                valor
            )
            VALUES(?, ?)
        """,(funcionario_id,valor))
        conn.commit()
        conn.close()
        print("Salario cadastrado com sucesso")

    def listar_salario(self):
        conn=self.banco.conectar()
        cursor=conn.cursor()

        cursor.execute("""
            SELECT
                s.salario_id,
                f.nome,
                s.valor
            FROM salario s
            LEFT JOIN funcionarios f ON s.funcionario_id=f.funcionario_id;
        """)
        salario=cursor.fetchall()
        for i in salario:
            print(f"Id: {i[0]}| Nome: {i[1]}| Salario: {i[2]}")
        conn.close()

