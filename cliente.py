class Client:
    def __init__(self, value):
        self.name = value['name']
        self.cpf = value['cpf']
        self.uf = value['uf']
        self.age = value['age']
        self.renda_mensal = value['renda_mensal']
        self.produto_emprestimo = []

    def popula_produto(self, value):
        self.produto_emprestimo.append(value)