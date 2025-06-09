# em alguns momentos será necessario converter o tipo de uma variavel para manipular de forma diferente. Por exemplo, podemos ter uma variável do tipo string que armazena um número e precisamos fazer algum tipo de operação matemática.

preco = 10
print(preco)

# inteiro para float
preco = float(preco)
print(preco)

#   quando se divide um numero por outro:
#       se usar uma barra / o resultado sera de um float
preco = 10
print(preco / 2)
#       se usar duas barras // o resultado sera um inteiro
print(preco // 2)

# float para inteiro
preco = 10.30
print(preco)

preco = int(preco)
print(preco)

#numérido para string


# string para numero
preco = "10.50"
idade = "28"

print(float(preco)) #aqui a string está sendo passada para o tipo float

print(int(idade)) # aqui a string está sendo passada para o tipo int

valor = 99
valor_str = str(valor)
print(type(valor))  #aqui estamos solicitando que o programa imprima o tipo da variável. 
print(type(valor_str))  #aqui estamos solicitando que o programa imprima o tipo da variável. 
