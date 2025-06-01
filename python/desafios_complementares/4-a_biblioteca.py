'''
Crie uma classe Book com atributos de instância como título, autor, ano_publicação e disponível (um valor booleano que indica se o livro está disponível ou não). Em seguida, crie uma classe Library que tenha uma lista de livros e métodos de instância para emprestar um livro, devolver um livro e exibir todos os livros disponíveis. Ele usa atributos de classe para registrar o número total de livros na biblioteca. Cria instâncias de ambas as classes e executa operações de empréstimo e devolução de livros.
'''
# Definindo a classe Book com os atributos solicitados
class Book:
    def __init__(self, titulo, autor, ano_publicacao, disponivel=True):
        # Atributos de instância - cada livro tem suas próprias informações
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel  # Booleano que indica se o livro está disponível

    def __str__(self):
        # Método especial para facilitar a exibição das informações do livro
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"{self.titulo} por {self.autor} ({self.ano_publicacao}) - {status}"

# Definindo a classe Library com lista de livros e métodos solicitados
class Library:
    # Atributo de classe - compartilhado por todas as instâncias
    total_livros = 0

    def __init__(self):
        # Lista para armazenar os livros da biblioteca (atributo de instância)
        self.livros = []

    def adicionar_livro(self, livro):
        """Adiciona um livro à biblioteca e atualiza o contador total"""
        self.livros.append(livro)
        Library.total_livros += 1  # Incrementa o atributo de classe

    def emprestar_livro(self, titulo):
        """Empresta um livro se estiver disponível"""
        for livro in self.livros:
            if livro.titulo == titulo and livro.disponivel:
                livro.disponivel = False
                print(f"Livro '{titulo}' emprestado com sucesso.")
                return
        print(f"Livro '{titulo}' não está disponível para empréstimo.")

    def devolver_livro(self, titulo):
        """Devolve um livro, marcando como disponível"""
        for livro in self.livros:
            if livro.titulo == titulo and not livro.disponivel:
                livro.disponivel = True
                print(f"Livro '{titulo}' devolvido com sucesso.")
                return
        print(f"Livro '{titulo}' não foi encontrado ou já está disponível.")

    def mostrar_livros_disponiveis(self):
        """Exibe todos os livros disponíveis"""
        print("Livros disponíveis na biblioteca:")
        for livro in self.livros:
            if livro.disponivel:
                print(livro)

    @classmethod
    def mostrar_total_livros(cls):
        """Método de classe para mostrar o total de livros"""
        print(f"Total de livros na biblioteca: {cls.total_livros}")

# Criando instâncias de Book
livro1 = Book("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Book("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)
livro3 = Book("A Revolução dos Bichos", "George Orwell", 1945)

# Criando instância da biblioteca
biblioteca = Library()

# Adicionando livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Verificando total de livros (usando método de classe)
Library.mostrar_total_livros()

# Mostrando livros disponíveis
biblioteca.mostrar_livros_disponiveis()

# Realizando operações de empréstimo
biblioteca.emprestar_livro("O Pequeno Príncipe")
biblioteca.emprestar_livro("O Pequeno Príncipe")  # Tentativa de emprestar novamente

# Verificando status após empréstimo
biblioteca.mostrar_livros_disponiveis()

# Devolvendo o livro
biblioteca.devolver_livro("O Pequeno Príncipe")

# Status final
biblioteca.mostrar_livros_disponiveis()
