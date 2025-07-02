class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade 

    def __str__(self):
        return f"{self.nome}: {self.idade} anos"

    @classmethod
    def criar_apartior_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return Pessoa(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

# p1 = Pessoa("Raylan", 35)
# print(p1.nome, p1.idade)

p2 = Pessoa.criar_apartior_data_nascimento(1994, 10, 12, "Debora")
print(p2.nome, p2.idade)


print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))

