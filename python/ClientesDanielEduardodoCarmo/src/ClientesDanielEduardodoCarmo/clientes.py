# classe Clientes
class Clientes:
    def __init__(self, nome, idade, email, telefone):
        # Inicializa os atributos do Clientes
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

    # Método para atualizar o email do Clientes
    def atualizar_email(self, novo_email):
        self.email = novo_email

    # Método para atualizar o telefone do Clientes
    def atualizar_telefone(self, novo_telefone):
        self.telefone = novo_telefone

    # Método especial que define como o objeto será representado como string
    def __str__(self):
        return f"Clientes: {self.nome}"


# classe PaginaCompras
class PaginaCompras:
    def __init__(self):
        # Inicializa a lista de Clientes cadastrados na página de compras
        self.Clientes = []

    # Método para adicionar um novo Clientes à lista
    def adicionar_Clientes(self, Clientes):
        self.Clientes.append(Clientes)

    # Método para listar todos os Clientes cadastrados, usando o __str__ da classe Clientes
    def listar_Clientes(self):
        for Clientes in self.Clientes:
            print(Clientes)


# Exemplo de uso:
# Criação de dois objetos Clientes
Clientes1 = Clientes("João Teste", 30, "joao@email.com", "1234-5678")
Clientes2 = Clientes("Maria Teste", 25, "maria@email.com", "8765-4321")
Clientes3 = Clientes("Carlos Teste", 40, "carlos@email.com", "1122-3344")

# Criação da página de compras
pagina = PaginaCompras()

# Adicionando os Clientes à página de compras
pagina.adicionar_Clientes(Clientes1)
pagina.adicionar_Clientes(Clientes2)
pagina.adicionar_Clientes(Clientes3)

# Listando os Clientes cadastrados na página de compras
pagina.listar_Clientes()
