'''
Define uma classe Figure com um método de instância de área que retorna a área da figura. Em seguida, 
crie classes filhas como Circle e Rectangle que herdam de Shape e fornecem diferentes implementações do método area.
'''

import math

# Classe base para figuras geométricas
class Figure:
    def area(self):
        """
        Método que retorna a área da figura.
        Deve ser sobrescrito pelas subclasses.
        """
        raise NotImplementedError("Subclasses devem implementar este método.")

# Classe para círculo, herda de Figure
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calcula a área do círculo usando a fórmula: π * raio^2
        """
        return math.pi * (self.radius ** 2)

# Classe para retângulo, herda de Figure
class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Calcula a área do retângulo usando a fórmula: largura * altura
        """
        return self.width * self.height

# Exemplos de uso:
if __name__ == "__main__":
    circle = Circle(5)
    print(f"Área do círculo: {circle.area()}")

    rectangle = Rectangle(4, 6)
    print(f"Área do retângulo: {rectangle.area()}")