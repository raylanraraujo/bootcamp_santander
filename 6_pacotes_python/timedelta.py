import datetime

#criando data e hora
d = datetime.datetime(2025, 7, 19, 13, 45)
print(d) #2025-07-19 13:45:00

#adicionando uma semana
d = d + datetime.timedelta(weeks=1)
print(d)

##########
# EXEMPLO
##########
from datetime import datetime, timedelta

tipo_carro = 'P' # P, M , G
tempo_pequeno = 30 
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

def previsao(tempo):
    return data_atual + timedelta(minutes=tempo)

tipo_carro = input().upper()

print(f"Entrada: {data_atual}")
print("Saida: ", end='')

if tipo_carro == 'P':
    print(previsao(tempo_pequeno))
elif tipo_carro == 'M':
    print(previsao(tempo_medio))
else:
    print(previsao(tempo_grande))

