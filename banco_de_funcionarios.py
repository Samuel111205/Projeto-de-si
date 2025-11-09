import sqlite3

#conectar ao banco
def conectar():
    return sqlite3.connect("banco_funcionarios.db")

#Criar tabelas
def criar_tabelas():
    conn=conectar()
    cursor=conn.cursor()

    #tabela departamento
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departamentos(
            departamento_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_departamento TEXT NOT NULL,
            localizacao VARCHAR(100)
        )
    """)
    #Tabelas cargos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cargos(
            cargo_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_cargo TEXT NULL
        )
    """)
    # tabela funcionarios
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS funcionarios(
            funcionario_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data_nascimento DATE NOT NULL,
            genero TEXT CHECK(genero IN ('M','F')),
            estado_civil TEXT NULL,
            email TEXT NULL,
            telefone TEXT NOT NULL,
            data_admissao DATE NOT NULL,
            departamento_id INTEGER REFERENCES departamentos(departamento_id),
            cargo_id INTEGER REFERENCES cargos(cargo_id),
            gestor_id INTEGER REFERENCES funcionarios(funcionario_id)
        )
    """)
    #tabela presença
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS presencas(
            presenca_id INTEGER PRIMARY KEY AUTOINCREMENT,
            funcionario_id INTEGER REFERENCES funcionarios(funcionario_id),
            data DATE NOT NULL,
            hora_entrada TIME NOT NULL,
            hora_saida TIME NOT NULL,
            turno TEXT NOT NULL
        )
    """)
    #tabela Licença
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS licenca(
            licenca_id INTEGER PRIMARY KEY AUTOINCREMENT,
            funcionario_id INTEGER REFERENCES funcionarios(funcionario_id),
            tipo_licenca TEXT NULL,
            data_inicio DATE NULL,
            data_fim DATE NULL,
            estado TEXT NULL
        )
    """)
    #tabela salario
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS salario(
            salario_id INTEGER PRIMARY KEY AUTOINCREMENT,
            funcionario_id INTEGER REFERENCES funcionarios(funcionario_id),
            valor REAL
        )
    """)
    conn.commit()
    conn.close()

