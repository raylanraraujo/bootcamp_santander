texto = input("Informe um texto: ")
VOGAIS = "AEIOU" #a qui temos uma constante em Python

#exemplo usando um iterável
for letra in texto:
	if letra.upper() in VOGAIS:
		print(letra, end = "")
else:	
	print() # adiciona quebar de linha


# exemplo usando a função built-in range
for numero in range(0,51, 5):
	print(numero, end = " ")
