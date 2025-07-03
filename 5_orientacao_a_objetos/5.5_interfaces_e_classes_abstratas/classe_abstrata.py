from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC): #estou dizendo que a classe ControleRemoto é uma extensão de ABC
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV (ControleRemoto):
    def ligar(self):
        print("Liga TV")

    def desligar(self):
        print("Desliga TV")

    @property
    def marca(self):
        return "LG"
    
class controleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Liga Ar")
    
    def desligar(self):
        print("Desligar Ar")

    @property
    def marca(elf):
        return "Midea"

controle_1 = ControleTV()
controle_1.ligar()
controle_1.desligar()
print(controle_1.marca)

controle_2 = controleArCondicionado()
controle_2.ligar()
controle_2.desligar()
print(controle_2.marca)

# método abstrato é um método que não vai ter um corpo e todas as classes filhas que extendem desse cara vão ser obrigadas a implementar. 

#Outra caracteristica importante é que uma vez que você tem um método abstrato a classe se torna abstrata e ela não pode ser instanciada diretamente.

#quando se intancia uma classe 

#dessa forma eu consigo fazer com que a tv implemente a interface e nao cause mais erro.

# Na heranca eu tenho a opcaode herdar so um método do pai. E mesmo que o método nao tenha sido implementado ele vai funcionar. Agora com o conceito de contratos e classes abstratas, quando eu digo que um método é abstrato eu digo que a classe filha é obrigada a implementar. Entao isso faz com que o nosso códgo crie uma padronização. 

# Todas as classes que implementam a classe abstrat. Elas vao ter que obrigatoriamente implementar os métodos abstratos. 

# no exemplo os contratos é o método desligar que nao recebe nenhum argumento. E o métdoo ligar que não recebe nenhum argumento. E isso força que as minhas classes filhas elas consigam lidar com o comportamento e elas tenham que obrigatoriamente implementear o comportamento desejado


#é possivel forçar dentro de uma classe abstrata no Python uma propriedade.