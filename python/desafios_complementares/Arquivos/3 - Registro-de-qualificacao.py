"""
Escreva um programa que permita a um professor registrar as notas de seus alunos em um arquivo json chamado "grades.json".
O programa deve permitir que o professor insira os nomes dos alunos e suas notas. Então você precisa salvar esses dados em um arquivo quando o programa terminar
persista esses dados para execuções futuras do programa. Use os nomes dos alunos como chaves e as notas como valores.
"""

import json
import os

# Define o caminho do arquivo onde as notas serão salvas
arquivo_grades = r"C:\Users\carmo\Documents\CoderHouse_DataScience\python\desafios_complementares\Arquivos\grades.json"

def carregar_notas():
    """
    Carrega as notas existentes do arquivo JSON.
    Se o arquivo não existir, retorna um dicionário vazio.
    """
    if os.path.exists(arquivo_grades):
        with open(arquivo_grades, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    return {}

def salvar_notas(notas):
    """
    Salva as notas no arquivo JSON.
    """
    with open(arquivo_grades, 'w', encoding='utf-8') as arquivo:
        json.dump(notas, arquivo, indent=4, ensure_ascii=False)

def main():
    # Carrega as notas existentes
    notas = carregar_notas()
    
    while True:
        print("\n=== Sistema de Registro de Notas ===")
        print("1. Adicionar/Alterar nota")
        print("2. Ver todas as notas")
        print("3. Sair")
        
        opcao = input("\nEscolha uma opção (1-3): ")
        
        if opcao == "1":
            # Adiciona ou altera uma nota
            nome = input("\nDigite o nome do aluno: ").strip()
            try:
                nota = float(input("Digite a nota do aluno: "))
                if 0 <= nota <= 10:
                    notas[nome] = nota
                    print(f"Nota de {nome} registrada com sucesso!")
                else:
                    print("A nota deve estar entre 0 e 10!")
            except ValueError:
                print("Por favor, digite uma nota válida!")
                
        elif opcao == "2":
            # Mostra todas as notas
            if notas:
                print("\nNotas registradas:")
                for nome, nota in notas.items():
                    print(f"{nome}: {nota}")
            else:
                print("\nNenhuma nota registrada ainda.")
                
        elif opcao == "3":
            # Salva as notas e sai do programa
            salvar_notas(notas)
            print("\nNotas salvas com sucesso! Encerrando o programa...")
            break
            
        else:
            print("\nOpção inválida! Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()