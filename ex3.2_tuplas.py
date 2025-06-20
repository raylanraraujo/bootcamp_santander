letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

frutas = ("laranja", "pera", "uva",)
print(frutas)

pais = ("Brasil",)
print(pais)

#acesso direto e índice negativo
print(frutas[0])  
print(frutas[2])  
print(frutas[-1]) 
print(frutas[-3]) 

# tuplas aninhadas
matriz = (       # aqui temos tuplas detr de outra tupla
	(1, "a", 2),   # aqui foi criado uma matriz 3 por 3 (3x3)
	("b", 3, 4),
	(6, 5, "c"),
)

print(matriz[0])       #(1, "a", 2)
print(matriz[0][0])    #1
print(matriz[0][-1])   #2
print(matriz[-1][-1])  #"c" 

# Fatiamento
lista = ("p", "y", "t", "h", "o", "n",)

print(lista[2:])      #("t", "h", "o", "n")
print(lista[:2])      #("p", "y")
print(lista[1:3])     #("y", "t")
print(lista[0:3:2])   #("p", "t")
print(lista[::])      #("p", "y", "t", "h", "o", "n")
print(lista[::-1])    #("n", "o", "h", "t", "y", "p")

#Iterado
carros = ("gol", "celta", "palio",)

for carro in carros:
	print(carro)

for indice, carro in enumerate(carros):
	print(f"{indice}: {carro}")
	
#Outros métodos da classe Tuplas

#().count
minha_tupla = (1, 2, 2, 3, 4, 2, 5)

ocorrencias_do_2 = minha_tupla.count(2)
ocorrencias_do_6 = minha_tupla.count(6)

print(ocorrencias_do_2)
print(ocorrencias_do_6)

#().index
minha_tupla = ('a', 'b', 'c', 'd', 'a', 'e')
posicao_do_c = minha_tupla.index('c')
posicao_do_primeiro_a = minha_tupla.index('a')

print(posicao_do_c)
print(posicao_do_primeiro_a)

#Função embutida len
minha_tupla = (10, 20, 30, 40, 50)
tamanho = len(minha_tupla)
print(tamanho)