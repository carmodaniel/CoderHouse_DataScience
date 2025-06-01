'''Crie uma classe Employee que possua os seguintes atributos de instância: nome, sobrenome, idade, salário. Em seguida, crie uma classe Manager que herde de Employee e tenha um atributo de departamento adicional. Define métodos de instância para ambas as classes, como show_info para exibir os detalhes de um funcionário e raise_salary para aumentar o salário de um funcionário em uma determinada porcentagem. Crie instâncias de ambas as classes e execute algumas operações.
'''
# Definindo a classe base Employee
class Employee:
    def __init__(self, nome, sobrenome, idade, salario):
        # Atributos de instância comuns a todos os funcionários
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.salario = salario

    def show_info(self):
        """
        Exibe as informações do funcionário.
        """
        print(f"Nome: {self.nome} {self.sobrenome}")
        print(f"Idade: {self.idade}")
        print(f"Salário: R$ {self.salario:.2f}")

    def raise_salary(self, percent):
        """
        Aumenta o salário do funcionário em uma determinada porcentagem.
        :param percent: porcentagem de aumento (ex: 10 para 10%)
        """
        aumento = self.salario * (percent / 100)
        self.salario += aumento
        print(f"Salário aumentado em {percent}%. Novo salário: R$ {self.salario:.2f}")

# Definindo a classe Manager, que herda de Employee
class Manager(Employee):
    def __init__(self, nome, sobrenome, idade, salario, departamento):
        # Usando super() para chamar o construtor da classe pai (Employee)
        super().__init__(nome, sobrenome, idade, salario)
        # Atributo adicional exclusivo do Manager
        self.departamento = departamento

    def show_info(self):
        """
        Exibe as informações do gerente, incluindo o departamento.
        """
        # Podemos reutilizar a função da classe pai e adicionar mais informações
        super().show_info()
        print(f"Departamento: {self.departamento}")

# Criando instâncias das classes
emp1 = Employee("José", "Brasil", 30, 3500.00)
mgr1 = Manager("Maria", "Brasil", 40, 7000.00, "TI")

# Exibindo informações e realizando operações
print("Funcionário:")
emp1.show_info()
emp1.raise_salary(15)  # Aumenta o salário em 15%
print("\nGerente:")
mgr1.show_info()
mgr1.raise_salary(20)  # Aumenta o salário em 20%
print("\nOperações concluídas com sucesso!")
# Exibindo informações dos funcionários e gerentes
print("\nDetalhes dos Funcionários:")   
emp1.show_info()
print("\nDetalhes do Gerente:")
mgr1.show_info()
# Exibindo informações dos funcionários e gerentes  
print("\nOperações concluídas com sucesso!")