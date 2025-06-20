#criando conjuntos
carros = ({"palio", "gol", "celta", "palio"}) # passado um objeto iterável pra o construtor set
print(carros)

numeros = {1, 2, 3, 4}
print(numeros)

num = set([1, 2, 3, 1, 3, 4]) 
print(num)

fruta = set("abacaxi") 
print(fruta)

populares = set(("palio", "gol", "celta", "palio")) 
print(populares)


# Acessando dados
numeros = list(numeros)
n1 = numeros[0]
print(n1)

# Iterar conjuntos
numeros = set(numeros)

for numero in numeros:
    print(numero)

# Funcao enumerate
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Métodos da classe Set
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
conjunto_c = {4, 1, 2, 5, 6, 3}
conjunto_d = {1, 2, 3, 4, 5}
conjunto_e = {6, 7, 8, 9}
conjunto_f = {0, 1}

# union
print(conjunto_a.union(conjunto_b))

# intersection
print(conjunto_a.intersection(conjunto_b))

#isdisjoint
print(conjunto_d.isdisjoint(conjunto_e))
print(conjunto_d.isdisjoint(conjunto_f))

#add
sorteio = {1, 23}

sorteio.add(25)
sorteio.add(42)
sorteio.add(25)
print(sorteio)

#copy
copia_sorteio = sorteio.copy()
print(copia_sorteio)

# clear
sorteio.clear()
print(sorteio)
print(copia_sorteio)

# discard
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1) 
numeros.discard(45) 

print(numeros)

#pop
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros)

numeros.pop() 
numeros.pop() 
numeros.pop() 
numeros.pop()

print(numeros)

#remove
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros)
numeros.remove(1)
# numeros.remove(45)
print(numeros)

# comprimento len
print(len(numeros))

# in
print( 0 in numeros)
print(10 in numeros)