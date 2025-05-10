"""Escreva um programa que some todos os números inteiros ímpares de 0 até 100:

 🖐 Ajuda: Você pode utilizar as funções sum() e range() para facilitar. O terceiro parâmetro na função range(início, fim, passo) indica um passo de números.
"""
# Inicialização da Variável:
soma = 0
# Loop para somar os números ímpares de 0 a 100:    
for numimpar in range(1, 101, 2):
    soma += numimpar
# Impressão do Resultado:
print(f"A soma dos números ímpares de 0 a 100 é: {soma}")
# Verificação do Resultado:
if soma == 2500:
    print("A soma está correta!")   