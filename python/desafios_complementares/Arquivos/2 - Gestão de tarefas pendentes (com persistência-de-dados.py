from datetime import datetime
import os
import json

# Define o caminho do arquivo JSON
CAMINHO_ARQUIVO = r"C:\Users\carmo\Documents\CoderHouse_DataScience\python\desafios_complementares\Arquivos\expenses.json"

def carregar_despesas():
    """
    Carrega as despesas do arquivo JSON.
    Se o arquivo não existir ou estiver vazio, retorna uma lista vazia.
    """
    try:
        # Tenta abrir e ler o arquivo JSON
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        # Se o arquivo não existir, retorna lista vazia
        print("Arquivo de despesas não encontrado. Criando novo arquivo.")
        return []
    except json.JSONDecodeError:
        # Se o arquivo estiver vazio ou corrompido, retorna lista vazia
        print("Arquivo de despesas está vazio ou corrompido. Criando novo arquivo.")
        return []

def salvar_despesas(despesas):
    """
    Salva a lista de despesas no arquivo JSON.
    """
    try:
        with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
            json.dump(despesas, arquivo, ensure_ascii=False, indent=4)
        print("\nDespesas salvas com sucesso!")
    except Exception as e:
        print(f"\nErro ao salvar as despesas: {e}")

def registrar_despesa(despesas):
    """
    Registra uma nova despesa e a adiciona à lista de despesas.
    """
    # Obtém a data atual
    data_atual = datetime.now().strftime("%d/%m/%Y")
    
    # Solicita informações ao usuário
    descricao = input("Digite a descrição da despesa: ")
    
    # Validação do valor
    while True:
        try:
            valor = float(input("Digite o valor da despesa: R$ "))
            if valor < 0:
                print("O valor não pode ser negativo. Tente novamente.")
                continue
            break
        except ValueError:
            print("Por favor, digite um valor numérico válido.")
    
    # Cria um dicionário com os dados da despesa
    nova_despesa = {
        "data": data_atual,
        "descricao": descricao,
        "valor": valor
    }
    
    # Adiciona a nova despesa à lista
    despesas.append(nova_despesa)
    print("\nDespesa registrada com sucesso!")

def exibir_despesas(despesas):
    """
    Exibe todas as despesas registradas.
    """
    if not despesas:
        print("\nNenhuma despesa registrada.")
        return
    
    print("\n=== Despesas Registradas ===")
    for despesa in despesas:
        print(f"Data: {despesa['data']} - Descrição: {despesa['descricao']} - Quantidade: R$ {despesa['valor']:.2f}")

def main():
    # Carrega as despesas existentes
    despesas = carregar_despesas()
    
    while True:
        print("\n=== Registro de Despesas ===")
        print("1. Registrar nova despesa")
        print("2. Exibir despesas")
        print("3. Sair")
        
        opcao = input("\nEscolha uma opção (1-3): ")
        
        if opcao == "1":
            registrar_despesa(despesas)
            # Salva as despesas após cada novo registro
            salvar_despesas(despesas)
        elif opcao == "2":
            exibir_despesas(despesas)
        elif opcao == "3":
            # Salva as despesas antes de sair
            salvar_despesas(despesas)
            print("\nPrograma finalizado!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    main()