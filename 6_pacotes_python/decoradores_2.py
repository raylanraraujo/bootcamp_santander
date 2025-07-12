def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return envelope

@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}")

aprender("Python")

print()

#### exemplo 1 - adaptando

def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar a função")
        funcao(*args, **kwargs)
        print("Faz algo depois de executar a função.")
    
    return envelope


@meu_decorador
def ola_mundo(nome, outro_argmento):
    print(f"Olá mundo {nome}")


ola_mundo("Raylan", 1000)

print()

#### retornando valores de funcoes decoradas
def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return envelope

@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}")
    return tecnologia.upper()

tecnologia = aprender("Python")
print(tecnologia)


print()

#### Retornando com argumentos copy
def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar a função")
        resultado = funcao(*args, **kwargs)
        print("Faz algo depois de executar a função.")
        return resultado
    
    return envelope


@meu_decorador
def ola_mundo(nome, outro_argmento):
    print(f"Olá mundo {nome}")
    return nome.upper()


resultado = ola_mundo("Raylan", 1000)
print(resultado)

print()

#### decorador introspeccao

import functools
def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)
    
    return envelope


@meu_decorador
def ola_mundo(nome, outro_argmento):
    print(f"Olá mundo {nome}")


print(ola_mundo.__name__)