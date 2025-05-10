"""
Escreva um programa que leia dois números pelo teclado e permita escolher entre 4 opções em um menu:
Mostrar a soma dos dois números
Mostrar a subtração dos dois números (o primeiro menos o segundo)
Mostrar a multiplicação dos dois números
Se escolher esta opção, a impressão do menu será interrompida e o programa finalizará
Caso não introduza uma opção válida, o programa informará que não é correta.
"""

# Inclusão dos Números:
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Menu de Opções:
print("Escolha uma opção:")
print("1 - Somar os dois números")
print("2 - Subtrair os dois números")
print("3 - Multiplicar os dois números")
print("4 - Sair do programa")
opcao = int(input("Digite a opção desejada: ")) 
# Verificação da Opção:
if opcao == 1:
    print(f"A soma dos números é: {num1 + num2}")   
elif opcao == 2:
    print(f"A subtração dos números é: {num1 - num2}")
elif opcao == 3:            

    print(f"A multiplicação dos números é: {num1 * num2}")
elif opcao == 4:    
    print("Saindo do programa...")  


