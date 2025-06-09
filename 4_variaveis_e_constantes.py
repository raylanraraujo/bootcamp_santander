# Variáveis 
#explicacao de variáveis...
# exemplo 1
age = 23
name = 'Guilherme'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.') 

# podemos descrever várias variáveis em python numa única linha.
# os parênteses sao opcionais
age, name = (23, 'Guilherme')
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

#para alterar valores basta atribuir à variável um novo valor
age, name = (27, 'Giovanna')
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

# Constantes
#   Utilizadas para armazenar valores. 
#   Valor imutável
#   nasce com um valor e permanece com ele até o final da execução do programa
#   EM PYTHON NÃO TEM CONSTANTES
#   é usado uma convenção que diz ao programador que a variável é uma constante criando uma variável com o nome todo em LETRAS_MAIÚSCULAS
#   exemplos de contantes
ABS_PATH = ''
DEBUB = True
STATES = [
    'SP',
    'RJ',
    'MG'
]
AMOUNT = 30.2

# Boas práticas
#   padrão de nomes em snake_case
#   escolher nomes sugestivos
#   Nome de constantes todo em maiúsculo