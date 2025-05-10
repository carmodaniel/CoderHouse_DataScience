"""
Vogais perdidas?
Crie um programa que solicite ao usuário que digite uma palavra. Em seguida, analise a palavra e conte quantas vogais ela contém. Ao final, caso não sejam encontradas vogais, exibe uma mensagem comunicando que a palavra digitada contém apenas consoantes.
"""
# Solicita ao usuário que digite uma palavra
palavra = input("Digite uma palavra: ").lower()

# Inicializa o contador de vogais
contador_vogais = 0

# Lista de vogais
vogais = ['a', 'e', 'i', 'o', 'u']

# Verifica cada letra da palavra
for letra in palavra:
    if letra in vogais:
        contador_vogais += 1

# Exibe o resultado
if contador_vogais > 0:
    print(f"A palavra digitada contém {contador_vogais} vogal(is).")
else:
    print("A palavra digitada contém apenas consoantes.")