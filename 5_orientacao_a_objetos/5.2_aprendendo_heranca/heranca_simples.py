class Veiculo:
    def __init__(self, cor, placa, numero_de_rodas): #características que sao comuns em todos os veículos
        self.cor = cor
        self.placa = placa
        self.numero_de_rodas = numero_de_rodas


    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    

    def ligar_motor(self):
        print("Ligando o motor")      
    

class Motocileta(Veiculo):
    pass

class Carro(Veiculo):
        pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_de_rodas, carregado):
         super().__init__(cor, placa, numero_de_rodas) # ele chama a implementação da classe pai. Nesse caso estamos implementando o étodo __init__ da classe pai
         self.carregado = carregado

    
    def estar_carregado(self): #declarando um método específico para a classe filha
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado") #verifica se o caminhão está carregado ou não


moto = Motocileta("preta", "abc-1234", 2) #criando uma moto
moto.ligar_motor()

carro = Carro("branco", "xde-0098", 4) #instanciando um carro
carro.ligar_motor()\

caminhao = Caminhao("roxo", "gft-8712", 8, False) #criando um caminhao
caminhao.ligar_motor()

print(f"Caminhão está carregado: ", end="")
caminhao.estar_carregado()
print()

print(moto)
print(carro)
print(caminhao)
print()