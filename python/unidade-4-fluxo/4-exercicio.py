"""
Escreva um programa que peça ao usuário quantos números deseja introduzir. Depois, leia todos os números e calcule uma média aritmética.

"""

# Pede ao usuário quantos números deseja introduzir
quantidade = int(input("Quantos números você deseja introduzir? "))

# Lista para armazenar os números
numeros = []

# Lê os números
for contador in range(quantidade):
    numero = float(input(f"Digite o {contador+1}º número: "))
    numeros.append(numero)

# Calcula a média aritmética
media = sum(numeros) / len(numeros)

# Mostra o resultado
print(f"\nA média aritmética dos números é: {media:.2f}")