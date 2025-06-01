'''
Crie uma classe Calculadora com um método de classe chamado soma que aceita dois números como argumentos e retorna a soma deles. Em seguida, use este método para realizar algumas operações de adição.
'''

class Calculadora:
    @classmethod # Define o método como um método de classe
    def soma(cls, a, b):
        """Retorna a soma de dois números."""
        return a + b

# Solicita ao usuário os valores de a e b
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

resultado = Calculadora.soma(a, b)
print("Resultado da soma:", resultado)
