"""
Utilizando a função range() e a conversão para listas, gere as seguintes listas dinamicamente:
Todos os números de 0 a 10 [0, 1, 2, ..., 10]
Todos os números de -10 a 0 [-10, -9, -8, ..., 0]
Todos os números pares de 0 a 20 [0, 2, 4, ..., 20]
Todos os números ímpares entre -20 e 0 [-19, -17, -15, ..., -1]
Todos os números múltiplos de 5 de 0 a 50 [0, 5, 10, ..., 50]
🖐 Ajuda: a conversão de listas é minha_lista=list(range(início,fim,passo))
"""
# Gera a lista de todos os números de 0 a 10
numeros_0_a_10 = list(range(0, 11))
print(f"Todos os números de 0 a 10: {numeros_0_a_10}")

# Gera a lista de todos os números de -10 a 0
numeros_menos10_a_0 = list(range(-10, 1))
print(f"Todos os números de -10 a 0: {numeros_menos10_a_0}")

# Gera a lista de todos os números pares de 0 a 20
numeros_pares_0_a_20 = list(range(0, 21, 2))
print(f"Todos os números pares de 0 a 20: {numeros_pares_0_a_20}")

# Gera a lista de todos os números ímpares entre -20 e 0
numeros_impares_menos20_a_0 = list(range(-19, 0, 2))
print(f"Todos os números ímpares entre -20 e 0: {numeros_impares_menos20_a_0}")

# Gera a lista de todos os números múltiplos de 5 de 0 a 50
numeros_multiplos_5_0_a_50 = list(range(0, 51, 5))
print(f"Todos os números múltiplos de 5 de 0 a 50: {numeros_multiplos_5_0_a_50}")