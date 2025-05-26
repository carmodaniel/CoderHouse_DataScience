import datetime  # biblioteca para manipulação de data
import re  # biblioteca para regex
from tabulate import tabulate  # biblioteca para formatar a tabela

usuarios = {}

def menuCadastro():
    while True:
        print("\n===== MENU DE CADASTRO =====")
        print("1 - Registrar Usuário")
        print("2 - Listar Usuários")
        print("3 - Login")
        print("4 - Encerrar Programa")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            registrarUsuario()
        elif opcao == "2":
            listarUsuarios()
        elif opcao == "3":
            loginUsuario()
        elif opcao == "4":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida, digite as opções do menu.")

def registrarUsuario():
    tentativas_usuario = 0
    while tentativas_usuario < 3:
        nome = input("\nDigite o nome do usuário (8-16 caracteres): ").strip()
        if len(nome) < 8 or len(nome) > 16:
            print("O nome do usuário digitado não é valido, por favor cadastre com o mínimo de 8 caracteres.")
            tentativas_usuario += 1
            continue
        if nome in usuarios:
            print("Usuário já cadastrado. Pressione ENTER para voltar ao menu.")
            input()
            return
        break
    else:
        print("Favor validar as informações e seguir com o cadastro na sequência.")
        return

    # E-mail
    while True:
        email = input("Digite o e-mail: ").strip()
        if email == "":
            print("Cadastro cancelado. Retornando ao menu principal.")
            return
        if "@" not in email:
            print("O domínio de e-mail não existe.")
            print("Digite novamente ou pressione ENTER para voltar ao menu principal.")
            continue
        break

    # Data de nascimento
    tentativas_data = 0
    while tentativas_data < 3:
        data_nasc = input("Digite a data de nascimento (dd/mm/aaaa): ").strip()
        if not re.match(r"^\d{2}/\d{2}/\d{4}$", data_nasc):
            print("Formato de data inválido! Utilize o formato dd/mm/aaaa")
            tentativas_data += 1
            continue
        try:
            dia, mes, ano = map(int, data_nasc.split("/"))
            data_nasc_obj = datetime.date(ano, mes, dia)
        except Exception:
            print("Formato de data inválido! Utilize o formato dd/mm/aaaa")
            tentativas_data += 1
            continue
        hoje = datetime.date.today()
        idade = hoje.year - ano - ((hoje.month, hoje.day) < (mes, dia))
        if idade < 18:
            print("Favor pedir o cadastro pelos seus pais ou responsáveis.")
            input("Pressione ENTER para voltar ao menu.")
            return
        break
    else:
        print("Favor validar as informações e seguir com o cadastro na sequência.")
        return

    # Senha
    tentativas_senha = 0
    especiais = "!@#$%^&*()?/"
    while tentativas_senha < 3:
        senha = input("Digite a senha (8-16 caracteres, mínimo 2 especiais !@#$%^&*()?/): ")
        if len(senha) < 8 or len(senha) > 16:
            print("Necessário que sua senha tenha no mínimo 8 caracteres sendo dois especiais.")
            tentativas_senha += 1
            continue
        cont_especiais = sum(1 for c in senha if c in especiais)
        if cont_especiais < 2:
            print("Necessário que sua senha tenha no mínimo 8 caracteres sendo dois especiais.")
            tentativas_senha += 1
            continue
        break
    else:
        print("Favor validar as informações e seguir com o cadastro na sequência.")
        return

    usuarios[nome] = {
        "email": email,
        "data_nasc": data_nasc,
        "idade": idade,
        "data_cadastro": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
        "senha": senha
    }
    print(f"Usuário '{nome}' cadastrado com sucesso!")

def listarUsuarios():
    if not usuarios:
        print("\nNenhum usuário cadastrado.")
        return
    tabela = []
    for nome, dados in usuarios.items():
        tabela.append([
            dados["data_cadastro"],
            nome,
            dados["email"],
            dados["data_nasc"],
            dados["idade"]
        ])
    print("\nUsuários cadastrados:")
    print(tabulate(tabela, headers=["Data Cadastro", "Nome", "E-mail", "Data Nasc.", "Idade"], tablefmt="grid"))

def loginUsuario():
    tentativas_usuario = 0
    while tentativas_usuario < 3:
        nome = input("\nDigite o nome do usuário: ").strip()
        if nome not in usuarios:
            tentativas_usuario += 1
            print(f"Usuário '{nome}' não encontrado. Tentativa {tentativas_usuario} de 3.")
            if tentativas_usuario >= 3:
                print("Verifique as informações fornecidas e tente posteriormente.")
                return
        else:
            break
    else:
        return

    tentativas_senha = 0
    while tentativas_senha < 3:
        senha = input("Digite a senha: ").strip()
        if senha == usuarios[nome]["senha"]:
            print(f"Bem-vindo, {nome}!")
            return
        else:
            tentativas_senha += 1
            print(f"Senha incorreta. Tentativa {tentativas_senha} de 3.")
            if tentativas_senha >= 3:
                print("Seu usuário foi bloqueado por tentativa por mais de 3 vezes com senha errada.")
                print("Favor entrar em contato com o suporte.")
                return

# Para rodar o programa
menuCadastro()