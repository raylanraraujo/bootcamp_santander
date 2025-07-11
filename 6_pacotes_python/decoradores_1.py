#### exemplo 1
def dizer_oi(nome):
    return f"Oi {nome}"

def incentivar_aprender(nome):
    return f"Oi {nome}, vamos aprender Python juntos!"

def mensagem_para_guilherme(funcao_mensagem):
    return funcao_mensagem("Guilherme")

print(mensagem_para_guilherme(dizer_oi))
print(mensagem_para_guilherme(incentivar_aprender))

print()
#### exemplo 2 - Inner function
def pai():
    print("Escrevendo da pai() função")

    def filho1():
        print("Escrevendo da filho1() função")

    def filho2():
        print("Escrevendo da filho2() função")

    filho2()
    filho1()

pai()

print()
#### exemplo 3 - Retornndo funcoes com Funcoes
def calcular(operacao):
    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b

    if operacao == "+":
        return somar
    else:
        return subtrair

resultado = calcular("+")(1, 3)
print(resultado)

print()

#### 4 - PAssagem de parametros
def mensagem(nome):
    print("executando mensagem")
    return f"Oi {nome}"

def mensagem_longa(nome):
    print("executando mensagem longa")
    return f"Olá tudo bem com você {nome}?"

def executar(funcao, nome):
    print("executando executar")
    return funcao(nome)

print(executar(mensagem, "Joao"))
print(executar(mensagem_longa, "Joao"))

print()

#### 5 - funcao interna
def principal():
    print("executando a funcao principal")

    def funcao_interna():
        print("executando a funcao interna")

    def funcao_2():
        print("executando a funcao 2")

    funcao_interna()
    funcao_2()

principal()

print()

#### 6 - retorna funcao
def calculadora(operacao):
    def soma(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mul
        case "/":
            return div
        

op = calculadora("+")
print(op(2, 2))

op = calculadora("-")
print(op(2, 2))

op = calculadora("*")
print(op(2, 2))

op = calculadora("/")
print(op(2, 2))


#### Sem decorador
def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a função.")
        funcao()
        print("Faz algo depois de executar a função.")
    
    return envelope

def ola_mundo():
    print("Olá mundo!")

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()

print()

#### Com decorador
def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a função.")
        funcao()
        print("Faz algo depois de executar a função.")
    
    return envelope


@meu_decorador
def ola_mundo():
    print("Olá mundo!")

ola_mundo()