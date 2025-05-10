"""Escreva um programa que leia um número ímpar pelo teclado. Se o usuário não introduzir um número ímpar, deve-se repetir o processo até que ele seja introduzido corretamente.
"""
# Inclusão do Número:
numero = int(input("Digite um número ímpar: "))
# Verificação do Número:
while numero % 2 == 0:
    print('Número digitado é par, favor digitar um número ##ímpar##.')
    numero = int(input("Digite um número ímpar: "))