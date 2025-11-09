import banco_de_funcionarios

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

        cursor.execute("""INSERT INTO departamentos (nome_departamento,localizacao)
            VALUES (?, ?)""",(nome,localizacao)
        )
        conn.commit()
        conn.close()

    def listar_departamento(self):
        conn=self.banco.conectar()
        cursor=conn.cursor()

        cursor.execute("SELECT departamento_id,nome_departamento FROM departamentos ORDER BY nome_departamento")
        dep=cursor.fetchall()
        print("==========Departamentos==========")
        for i in dep:
            print(f"Id: {i[0]}| Nome: {i[1]}")
        print("="*25)
        conn.close()

    def deletar_departamento(self,id_departamento):
        conn=self.banco.conectar()
        cursor=conn.cursor()

        cursor.execute("DELETE FROM departamentos WHERE departamento_id=?",(id_departamento,))
        conn.commit()
        conn.close()


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
        print("========== Cargos ==========")
        for i in cargo:
            print(f"Id: {i[0]}| Nome: {i[1]}")
        print("="*25)
        conn.close()

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
            WHERE nome=?
        """,(nome,))
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
            print(f"Funcionario {nome} nãon foi encotrado na base de dados")


#Classe presenças
class Presencas:
    def __init__(self,banco):
        self.banco=banco

    def cadastrar_presencas(self,id_funcionario,data,hora_entrada,hora_saida,turno):
        conn=self.banco.conectar()
        cursor=conn.cursor()

        cursor.execute("""
            INSERT INTO presencas(
                funcionario_id,
                data,
                hora_entrada,
                hora_saida,
                turno
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
        for i in presenca:
            print(f"Id: {i[0]}| Nome: {i[1]}| Data: {i[2]}| Hora de entrada: {i[3]}| Hora de saida: {i[4]}| Turno: {i[5]}")
        conn.close()


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
        for i in licenca:
            print(f"Id: {i[0]}| Nome: {i[1]}| Tipo de Contrato: {i[2]}| Data de inicio: {i[3]}| Data do fim: {i[4]}| Estado: {i[5]}")
        conn.close()


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


#menu principal
def menu():

    banco_de_funcionarios.criar_tabelas()

    banco=Banco()
    departamento=Departamento(banco)
    cargo=Cargo(banco)
    funcionarios=Funcionario(banco)
    presenca=Presencas(banco)
    licenca=Licenca(banco)
    salario=Salario(banco)

    while True:
        print("="*25)
        print("1.Gerenciar departamentos")
        print("2.Gerenciar cargos")
        print("3.Gerenciar funcionarios")
        print("4.Gerenciar Presenças")
        print("5.Gerenciar contratos")
        print("6.Gerenciar salarios")
        print("7.Sair")
        print("="*25)
        opcao=int(input("Digite a sua opção: "))

        if opcao==1:
            while True:
                print("=" * 25)
                print("1.Adicionar departamento")
                print("2.Listar departamento")
                print("3.Deletar departamento")
                print("4.Sair")
                print("=" * 25)
                escolha_dep=int(input("Digite sua opção: "))

                if escolha_dep==1:
                    print("Cadastrando um departamento")
                    nome=input("Digite o nome do departamento: ").title()
                    licalizacao=input("Digite a localização do departamento: ").title()
                    departamento.cadastrar_departamento(nome,licalizacao)
                    print("Departamento cadastrado com sucesso")

                elif escolha_dep==2:
                    departamento.listar_departamento()

                elif escolha_dep==3:
                    departamento.listar_departamento()
                    id_departamento=int(input("Digite o id do departamento: "))
                    departamento.deletar_departamento(id_departamento)
                    print("Departamento excluido com sucesso")

                elif escolha_dep==4:
                    break
                else:
                    print("Opção invalida")

        elif opcao==2:
            while True:
                print("=" * 25)
                print("1.Adicionar cargo")
                print("2.Listar cargo")
                print("3.Deletar cargo")
                print("4.Sair")
                print("=" * 25)
                escolha_car=int(input("escolha sua opção: "))

                if escolha_car==1:
                    print("Cadastrar cargo")
                    nome_cargo=input("Digite o nome do cargo: ").title()
                    cargo.cadastrar_cargo(nome_cargo)

                elif escolha_car==2:
                    cargo.listar_cargo()

                elif escolha_car==3:
                    cargo.listar_cargo()
                    id_cargo=int(input("Digite o id do cargo: "))
                    cargo.deletar_cargo(id_cargo)
                    print("cargo excluido com sucesso")

                elif escolha_car==4:
                    break
                else:
                    print("Opção invalida")

        elif opcao==3:

            while True:
                print("1.Cadastrar funcionarios")
                print("2.Listar funcionario")
                print("3.Ver dados de um aluno")
                print("4.Sair")
                escolha_fun=int(input("Digite a sua escolha: "))

                if escolha_fun==1:
                    quant=int(input("Quantos funcionarios serão cadastradas: "))
                    for i in range(0,quant+1):
                        nome=input("Nome do funcionario: ").title()
                        data_nascimento=input("Data de nascimento: ")
                        genero=input("Genero(F/M): ").upper()
                        estado_civil=input("Estado Civil: ").title()
                        email=input("Email: ")
                        telefone=input("Nº de telefone: ")
                        data_admissao=input("Data de admissão: ")
                        departamento.listar_departamento()
                        departamento_id=int(input("Departamento: "))
                        cargo.listar_cargo()
                        cargo_id=int(input("Cargo: "))
                        funcionarios.cadastrar(nome,data_nascimento,genero,estado_civil,email,telefone,data_admissao,departamento_id,cargo_id)

                elif escolha_fun==2:
                    funcionarios.listar_funcionario()

                elif escolha_fun==3:
                    nome=input("Digite o nome do funcionario: ").title()
                    funcionarios.ver_dados_de_um_funcionario(nome)

                elif escolha_fun==4:
                    break

                else:
                    print("Opção invalida")

        elif opcao==4:
            while True:
                print("1.Cadastrar presença")
                print("2.Listar presença")
                print("3.Sair")
                escolha_pre=int(input("Digite sua opção: "))

                if escolha_pre==1:
                    funcionarios.listar_funcionario()
                    id_funcionario=int(input("Id do funcionario: "))
                    data=input("Data: ")
                    hora_entrada=input("Hora de entrada: ")
                    hora_saida=input("Hora de saida: ")
                    turno=input("Turno (Manhã/Tarde/Noite): ").title()
                    presenca.cadastrar_presencas(id_funcionario,data,hora_entrada,hora_saida,turno)

                elif escolha_pre==2:
                    presenca.listar_presenca()
                elif escolha_pre==3:
                    break

        elif opcao==5:
            while True:
                print("1.Cadastrar licença")
                print("2.Listar licença")
                print("3.Sair")
                escolha_li=int(input("Digite a  sua opção: "))

                if escolha_li==1:
                    funcionarios.listar_funcionario()
                    funcionario_id=int(input("Id do funcionario: "))
                    tipo_licenca=input("Tipo de contrato (Colaborador/Prestador de serviço/Efetivo): ").title()
                    data_inicio=input("Inicio do contrato: ")
                    data_fim=input("Fim do contrato: ")
                    estado=input("Estado (ativo/despedido/fimdo ciclo): ").title()
                    licenca.cadastrar_licenca(funcionario_id,tipo_licenca,data_inicio,data_fim,estado)

                elif escolha_li==2:
                    licenca.listar_licencas()

                elif escolha_li==3:
                    break

        elif opcao==6:
            while True:
                print("1.Cadastrar salario")
                print("2.Listar salario")
                print("3.Sair")
                escolha_sal=int(input("Digite a sua opção: "))

                if escolha_sal==1:
                    funcionarios.listar_funcionario()
                    funcionario_id=int(input("Digite o id do funcionario: "))
                    valor=float(input("Valor do salario: "))
                    salario.cadastrar_salario(funcionario_id,valor)

                elif escolha_sal==2:
                    salario.listar_salario()

                elif escolha_sal==3:
                    break

        elif opcao==7:
            break

        else:
            print("Opção invalida")

if __name__=="__main__":
    menu()
    