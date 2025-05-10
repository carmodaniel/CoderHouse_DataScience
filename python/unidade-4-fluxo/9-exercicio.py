"""
Pulando palavras
Escreva um programa que receba uma lista de palavras digitadas pelo usuário. Depois peça-lhe que mostre cada palavra, uma por uma. Se a palavra for “exit”, o programa termina. Se a palavra for "omitir", passa para a próxima iteração. Ao final, caso nenhuma palavra tenha sido “saída”, será exibida uma mensagem alertando sobre a situação.
"""
# Solicita ao usuário que digite uma lista de palavras separadas por espaço
palavras = input("Digite uma lista de palavras separadas por espaço: ").split()

# Inicializa uma variável para verificar se "exit" foi digitado
exit_encontrado = False

# Itera sobre cada palavra na lista
for palavra in palavras:
    if palavra == "exit":
        exit_encontrado = True
        print("Programa encerrado.")
        break  # Encerra o programa se a palavra for "exit"
    elif palavra == "omitir":
        continue  # Passa para a próxima iteração se a palavra for "omitir"
    else:
        print(f"Palavra: {palavra}")

# Verifica se "exit" não foi encontrado
if not exit_encontrado:
    print("Nenhuma palavra foi 'exit'.")