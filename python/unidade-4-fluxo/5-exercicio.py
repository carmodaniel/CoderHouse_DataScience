"""
Escreva um programa que peça ao usuário um número inteiro de 0 a 9, e enquanto o número não for correto, repita o processo. Depois, deve verificar se o número se encontra na lista de números e notificá-lo:
🖐 Ajuda: A sintaxe "valor in lista" permite verificar facilmente se um valor se encontra em uma lista (devolve True ou False).

"""
# Inclusão do Número:
numero = int(input("Digite um número  de 0 a 9: "))

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Verificação do Número:
while numero in lista == False:
    print("Número digitado fora do intervalo, favor digitar um número entre 0 e 9.")
    numero = int(input("Digite um número inteiro de 0 a 9: ")) 
# Lista de Números:
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Verificação do Número na Lista:

if numero in lista:
    print(f"O número {numero} se encontra na lista.")
else:
    print(f"O número {numero} não se encontra na lista.")   