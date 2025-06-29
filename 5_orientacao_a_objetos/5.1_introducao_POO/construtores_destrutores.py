class Cachorro:
  def __init__(self, nome, cor, acordado=True):
    print("Inicializando a classe...")
    self.nome=nome
    self.cor=cor
    self.acortado=acordado
  
  def __del__(self):
    print("Removendo a instância da classe.")
    
  def falar(self):
    print("Auau")

def criar_cachorro():
  c = Cachorro("Zeus", "Branco e preto", False)
  print(c.nome)


c = Cachorro("Chapie", "amarelo")
c.falar()

print("Olá mundo")

del c

print("Olá mundo")
print("Olá mundo")
print("Olá mundo")

# Inicializando a classe...
# Auau
# Olá mundo
# Removendo a instância da classe.
# Olá mundo
# Olá mundo
# Olá mundo