# o código abaixo é interrompido quando o número for 12. Assim ele só exibe até o 11
for numero in range(100):
	if numero == 12:
		break
	print(numero, end = " ")

# o código abaixo exibe apenas os numeros impares
for numero in range(100):
	if numero % 2 == 0:
		continue
	print(numero, end = " ")
	

# usando BREAK e CONTINUE juntos.
while True:
    numero = int(input("Infomre um número: "))
	
    if numero == 10: # caso o número digitado for 10 o programa será interrompido
        break

    if numero % 2 == 0: # caso o número for par o laço sera pulado nao exibir esse número
        continue
	
    print(numero) #exibe o número impar digitado