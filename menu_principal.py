from modulo_de_classes import *
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
                    while True:
                        try:
                            departamento.listar_departamento()
                            id_departamento=int(input("Digite o id do departamento: "))
                            break
                        except:
                            print("Erro, por favor digite um numero valido")

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
                    while True:
                        try:
                            cargo.listar_cargo()
                            id_cargo = int(input("Digite o id do cargo: "))
                            break
                        except:
                            print("Erro, por favor digite um numero valido")

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
                print("3.Ver dados de um fucionario")
                print("4.Ver por departamento")
                print("5.Atualizar funcionario")
                print("6.Deletar funcionario")
                print("7.Sair")
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
                        while True:
                            try:
                                departamento.listar_departamento()
                                departamento_id = int(input("Digite o id do departamento: "))
                                break
                            except:
                                print("Erro, por favor digite um numero valido")
                        while True:
                            try:
                                cargo.listar_cargo()
                                cargo_id = int(input("Cargo: "))
                                break
                            except:
                                print("Erro, por favor digite um numero valido")

                        funcionarios.cadastrar(nome,data_nascimento,genero,estado_civil,email,telefone,data_admissao,departamento_id,cargo_id)

                elif escolha_fun==2:
                    funcionarios.listar_funcionario()

                elif escolha_fun==3:
                    nome=input("Digite o nome do funcionario: ").title()
                    funcionarios.ver_dados_de_um_funcionario(nome)

                elif escolha_fun==4:
                    departamento_nome = input("Digite o id do departamento: ").title()
                    funcionarios.ver_por_departamento(departamento_nome)

                elif escolha_fun==5:
                    funcionarios.listar_funcionario()
                    funcionarios.atualizar_funcionario()

                elif escolha_fun==6:
                    funcionarios.listar_funcionario()
                    funcionario_id=int(input("Digite o id do aluno: "))
                    funcionarios.deletar_funcionario(funcionario_id)

                elif escolha_fun==7:
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
                    while True:
                        try:
                            funcionarios.listar_funcionario()
                            id_funcionario = int(input("Id do funcionario: "))
                            break
                        except:
                            print("Erro, por favor digite um numero valido")

                    hora_entrada=input("Hora de entrada: ")
                    hora_saida=input("Hora de saida: ")
                    turno=input("Turno (Manhã/Tarde/Noite): ").title()
                    presenca.cadastrar_presencas(id_funcionario,hora_entrada,hora_saida,turno)

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
                    while True:
                        try:
                            funcionarios.listar_funcionario()
                            funcionario_id = int(input("Id do funcionario: "))
                            break
                        except:
                            print("Erro, por favor digite um numero valido")

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
                    while True:
                        try:
                            funcionarios.listar_funcionario()
                            funcionario_id = int(input("Id do funcionario: "))
                            break
                        except:
                            print("Erro, por favor digite um numero valido")
                    while True:
                        try:
                            valor = float(input("Valor do salario: "))
                            break
                        except:
                            print("Erro, por favor digite um numero valido")

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
