"""
Inventário
Imagine que você gerencia um pequeno armazém e deseja acompanhar os produtos em seu estoque. 
Escreva um programa que permita inserir o nome e a quantidade de vários produtos. 
Ele usa um loop para percorrer os produtos e exibir seu nome e quantidade. 
Ao final, mostra o total de produtos em estoque.
"""

# Inicializa uma lista para armazenar os produtos
produtos = []

# Inicializa uma variável para armazenar o total de produtos
total_produtos = 0

# Loop para inserir produtos
while True:
    # Solicita o nome do produto
    nome_produto = input("Digite o nome do produto (ou 'sair' para encerrar): ")
    
    # Verifica se o usuário deseja sair
    if nome_produto.lower() == 'sair':
        break
    
    # Solicita a quantidade do produto
    try:
        quantidade_produto = int(input(f"Digite a quantidade de {nome_produto}: "))
        # Adiciona o produto à lista
        produtos.append((nome_produto, quantidade_produto))
        # Atualiza o total de produtos
        total_produtos += quantidade_produto
    except ValueError:
        print("Por favor, insira um número válido para a quantidade.")

# Exibe os produtos e suas quantidades
print("\nProdutos em estoque:")
for nome, quantidade in produtos:
    print(f"- {nome}: {quantidade} unidade(s)")

# Exibe o total de produtos
print(f"\nTotal de produtos em estoque: {total_produtos} unidade(s)")
