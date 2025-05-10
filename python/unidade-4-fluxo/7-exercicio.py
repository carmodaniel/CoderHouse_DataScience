"""
Escreva um programa que pegue uma lista de nomes inseridos pelo usuário separados por um espaço e os liste mostrando sua localização.
"""
# Inclusão dos Nomes:
nomes = input("Digite os nomes separados por espaço: ").split()
# Verificação dos Nomes:
for i, nome in enumerate(nomes):
    print(f"{nome} está na posição {i}")
# Exibição dos Nomes:
print("Os nomes inseridos foram:")
