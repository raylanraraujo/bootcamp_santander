class Animal:
    def __init__(self, numero_de_patas):
        self.numero_de_patas = numero_de_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

    
class Ave (Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico


class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    pass


gato = Gato(numero_de_patas=4, cor_pelo="preto")
print(gato)

ornitorrinco = Ornitorrinco(numero_de_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)