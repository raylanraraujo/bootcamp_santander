class Passaro:
    def voar(self):
       print("Voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar.")

class Pombo(Passaro):
    def voar(self):
        print("Pombo pode voar")

# a classe Aviao é um exemplo ruim de uso de herança para "ganhar"o método voar para entender que todo mundo que é filho de pássaro pode ser passado para plano de vôo.
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")

def plano_de_voo(objeto):
    objeto.voar()


p1 = Pardal()
p2 = Avestruz()

plano_de_voo(p1)
plano_de_voo(p2)
plano_de_voo(Pombo())
plano_de_voo(Aviao())

#em vez de criar variaveis, podemos passar logo a instância para o método plano_de_voo