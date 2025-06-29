#criar a classe
class Bicicleta:
    #método construtor que serve para definir as características (os atibutos) 
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor 
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1

    def buzinar(self):
        print("Trimmm-trimmm")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada")

    def correr(self):
        print("Vrummm")

    def trocar_marcha(self, nro_marcha):
        if nro_marcha > self.marcha:
            print("Marcha trocada...")
        else:
            print("Não foi possível trocar de marcha...")

    # def __str__(self): #nos mostra as instâncias dos nossos objetos
    #     return f"Bicicleta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}"
    
    # def __str__(self):
    #     return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

#com isso já temos uma instâancia de Bicicleta
b1 = Bicicleta("vermelha", "caloi", 2022, 600)

b1.correr()
b1.buzinar()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 160)

b2.buzinar = Bicicleta.buzinar(b2)
print(b2.cor) #acessando o atributo de cor do objeto
print(b2) #ao fazer isso o método __str__ é executdo e mostra as instancias do objeto