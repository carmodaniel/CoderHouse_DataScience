'''
Crie uma classe Produto com atributos de instância como nome, preço, quantidade_disponível e código_do_produto. A seguir, crie uma classe ShoppingCart que permite aos clientes adicionar produtos, remover produtos e calcular o total da compra. Usa um atributo de classe para rastrear a quantidade total de produtos nos carrinhos de compras de todos os clientes. Crie instâncias de ambas as classes e simule operações de compra.
'''
# Definindo a classe Produto com os atributos solicitados
class Produto:
    def __init__(self, nome, preco, quantidade_disponivel, codigo_do_produto):
        # Atributos de instância - cada produto tem suas próprias informações
        self.nome = nome  # Nome do produto
        self.preco = preco  # Preço unitário do produto
        self.quantidade_disponivel = quantidade_disponivel  # Quantidade em estoque
        self.codigo_do_produto = codigo_do_produto  # Código único do produto

    def __str__(self):
        # Método especial para facilitar a exibição das informações do produto
        # Retorna uma string formatada com os detalhes do produto
        return f"Produto: {self.nome}, Preço: R$ {self.preco:.2f}, Quantidade disponível: {self.quantidade_disponivel}, Código: {self.codigo_do_produto}"

# Definindo a classe ShoppingCart com métodos para adicionar, remover produtos e calcular o total
class ShoppingCart:
    # Atributo de classe para rastrear a quantidade total de produtos em todos os carrinhos
    # Este valor é compartilhado entre todas as instâncias de ShoppingCart
    total_produtos_carrinhos = 0

    def __init__(self):
        # Lista para armazenar os produtos no carrinho (atributo de instância)
        # Cada carrinho de compras (instância) terá sua própria lista de produtos
        self.produtos = [] # Armazena tuplas (produto, quantidade)

    def adicionar_produto(self, produto, quantidade=1):
        """Adiciona um produto ao carrinho e atualiza o contador total"""
        # Verifica se a quantidade solicitada está disponível no estoque do produto
        if produto.quantidade_disponivel >= quantidade:
            # Adiciona o produto e a quantidade desejada à lista do carrinho
            self.produtos.append((produto, quantidade))
            # Diminui a quantidade disponível do produto no estoque
            produto.quantidade_disponivel -= quantidade
            # Incrementa o contador total de produtos em todos os carrinhos
            ShoppingCart.total_produtos_carrinhos += quantidade
            print(f"{quantidade} unidade(s) do produto '{produto.nome}' adicionada(s) ao carrinho.")
        else:
            # Informa se a quantidade não está disponível
            print(f"Quantidade solicitada ({quantidade}) não disponível para o produto '{produto.nome}'. Disponível: {produto.quantidade_disponivel}.")

    def remover_produto(self, codigo_do_produto, quantidade=1):
        """Remove um produto do carrinho e atualiza o contador total"""
        # Itera sobre os produtos no carrinho para encontrar o produto a ser removido
        for i, (prod_no_carrinho, qtd_no_carrinho) in enumerate(self.produtos):
            if prod_no_carrinho.codigo_do_produto == codigo_do_produto:
                # Verifica se a quantidade a ser removida é maior ou igual à quantidade no carrinho
                if quantidade >= qtd_no_carrinho:
                    # Remove o produto completamente do carrinho
                    ShoppingCart.total_produtos_carrinhos -= qtd_no_carrinho # Decrementa o total global
                    prod_no_carrinho.quantidade_disponivel += qtd_no_carrinho # Devolve ao estoque
                    self.produtos.pop(i) # Remove da lista do carrinho
                    print(f"Produto '{prod_no_carrinho.nome}' removido completamente do carrinho.")
                else:
                    # Remove parcialmente a quantidade do produto
                    # Atualiza a quantidade do produto no carrinho
                    self.produtos[i] = (prod_no_carrinho, qtd_no_carrinho - quantidade)
                    ShoppingCart.total_produtos_carrinhos -= quantidade # Decrementa o total global
                    prod_no_carrinho.quantidade_disponivel += quantidade # Devolve ao estoque
                    print(f"{quantidade} unidade(s) do produto '{prod_no_carrinho.nome}' removida(s) do carrinho.")
                return # Sai do método após remover/atualizar
        # Informa se o produto não foi encontrado no carrinho
        print(f"Produto com código {codigo_do_produto} não encontrado no carrinho.")

    def calcular_total(self):
        """Calcula o total da compra no carrinho"""
        total = 0
        # Itera sobre os produtos no carrinho para somar os preços
        for produto, quantidade in self.produtos:
            total += produto.preco * quantidade
        return total

    def mostrar_carrinho(self):
        """Exibe os produtos no carrinho"""
        # Verifica se o carrinho está vazio
        if not self.produtos:
            print("Carrinho vazio.")
            return
        print("Produtos no carrinho:")
        # Itera sobre os produtos e exibe suas informações
        for produto, quantidade in self.produtos:
            print(f"- {produto.nome} (x{quantidade}) - R$ {produto.preco:.2f} cada")
        # Exibe o total da compra formatado
        print(f"Total da compra: R$ {self.calcular_total():.2f}")

    @classmethod
    def mostrar_total_produtos_em_todos_carrinhos(cls):
        """
        Método de classe para exibir a quantidade total de produtos 
        considerando todos os carrinhos de compras existentes.
        """
        print(f"Quantidade total de produtos em todos os carrinhos: {cls.total_produtos_carrinhos}")

# Criando instâncias da classe Produto
produto1 = Produto("Notebook Gamer", 4500.00, 10, "P001")
produto2 = Produto("Mouse Sem Fio", 150.00, 25, "P002")
produto3 = Produto("Teclado Mecânico", 300.00, 15, "P003")
produto4 = Produto("Monitor 24 polegadas", 1200.00, 5, "P004")

# Exibindo informações dos produtos criados
print("--- Catálogo de Produtos ---")
print(produto1)
print(produto2)
print(produto3)
print(produto4)
print("-" * 30)

# Criando um carrinho de compras para um cliente
carrinho_cliente1 = ShoppingCart()
print("\n--- Carrinho Cliente 1 ---")

# Adicionando produtos ao carrinho do cliente 1
carrinho_cliente1.adicionar_produto(produto1, 1)  # Adiciona 1 Notebook
carrinho_cliente1.adicionar_produto(produto2, 2)  # Adiciona 2 Mouses
carrinho_cliente1.adicionar_produto(produto4, 1)  # Adiciona 1 Monitor
carrinho_cliente1.mostrar_carrinho() # Mostra o carrinho

# Tentando adicionar mais produtos do que o disponível
carrinho_cliente1.adicionar_produto(produto4, 5) # Tenta adicionar mais 5 monitores (só há 4 restantes)

# Exibindo o total de produtos em todos os carrinhos (neste caso, apenas no carrinho_cliente1)
ShoppingCart.mostrar_total_produtos_em_todos_carrinhos()
print(f"Estoque atual do {produto1.nome}: {produto1.quantidade_disponivel}") # Verifica estoque
print(f"Estoque atual do {produto4.nome}: {produto4.quantidade_disponivel}") # Verifica estoque
print("-" * 30)

# Removendo um produto do carrinho do cliente 1
print("\n--- Removendo Produto (Cliente 1) ---")
carrinho_cliente1.remover_produto("P002", 1)  # Remove 1 Mouse
carrinho_cliente1.mostrar_carrinho() # Mostra o carrinho atualizado
ShoppingCart.mostrar_total_produtos_em_todos_carrinhos()
print(f"Estoque atual do {produto2.nome}: {produto2.quantidade_disponivel}") # Verifica estoque
print("-" * 30)

# Criando outro carrinho de compras para um segundo cliente
carrinho_cliente2 = ShoppingCart()
print("\n--- Carrinho Cliente 2 ---")
carrinho_cliente2.adicionar_produto(produto3, 3) # Adiciona 3 Teclados
carrinho_cliente2.adicionar_produto(produto1, 1) # Adiciona 1 Notebook (do estoque restante)
carrinho_cliente2.mostrar_carrinho()

# Exibindo o total de produtos em todos os carrinhos (agora considerando ambos)
ShoppingCart.mostrar_total_produtos_em_todos_carrinhos()
print(f"Estoque atual do {produto1.nome}: {produto1.quantidade_disponivel}") # Verifica estoque
print(f"Estoque atual do {produto3.nome}: {produto3.quantidade_disponivel}") # Verifica estoque
