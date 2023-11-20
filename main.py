import pyodbc
import re

dados_conexao = (
    'Driver={SQL Server}; '
    'Server=PcNic;'
    'Database=cadastro;'
    'Trusted_Connection=yes;'
)

conexao = pyodbc.connect(dados_conexao)
print('Conexão sucedida')

cursor = conexao.cursor()

clientes = []


def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")

    while True:
        email = input("Digite o email do cliente: ")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Formato de email inválido. Tente novamente.")
        else:
            break

    while True:
        telefone = input("Digite o telefone do cliente (formato: XXXXX-XXXX): ")
        if not re.match(r"\d{5}-\d{4}", telefone):
            print("Formato de telefone inválido. Tente novamente.")
        else:
            break

    cliente = {
        'Nome': nome,
        'Email': email,
        'Telefone': telefone
    }

    clientes.append(cliente)

    # Inserir dados no banco de dados
    comando = "INSERT INTO cadastro (nome, email, numeroTelefone) VALUES (?, ?, ?)"
    cursor.execute(comando, nome, email, telefone)
    conexao.commit()

    print("Cliente cadastrado com sucesso!\n")


def mostrar_dados_cadastro():
    if not clientes:
        print("Nenhum cliente cadastrado ainda.\n")
        return

    for i, cliente in enumerate(clientes, start=1):
        print(f"Cliente {i}:")
        for key, value in cliente.items():
            print(f"{key}: {value}")
        print()


def listar_clientes_cadastrados():
    if not clientes:
        print("Nenhum cliente cadastrado ainda.\n")
        return

    print("Clientes cadastrados:")
    for i, cliente in enumerate(clientes, start=1):
        print(f"{i}. {cliente['Nome']}")


def gerar_relatorio():
    if not clientes:
        print("Nenhum cliente cadastrado ainda.\n")
        return

    print("Relatório:")
    for i, cliente in enumerate(clientes, start=1):
        print(f"Cliente {i}: {cliente['Nome']}, {cliente['Email']}, {cliente['Telefone']}")
    print()


while True:
    print("1 - Cadastrar")
    print("2 - Mostrar dados do cadastro")
    print("3 - Clientes cadastrados")
    print("4 - Relatório")
    print("0 - Sair")

    escolha = input("Escolha a opção desejada: ")

    if escolha == '1':
        cadastrar_cliente()
    elif escolha == '2':
        mostrar_dados_cadastro()
    elif escolha == '3':
        listar_clientes_cadastrados()
    elif escolha == '4':
        gerar_relatorio()
    elif escolha == '0':
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.\n")
