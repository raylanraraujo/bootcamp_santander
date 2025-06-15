nome = "Guilerme"
idade = 28
profissao = "Programador"
linguagem = "Python"
pessoa = {"nome": "Guilherme", "idade": 28, "profissao":"Programador", "linguagem": "Python"}
saldo = 45.435

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s."%(nome, idade, profissao, linguagem))

print()

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print()

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(nome, idade, profissao, linguagem))

print()

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print()

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))

print()

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

print()
print(f"Saldo: {saldo}")
print(f"Saldo: {saldo: .2f}")
print(f"Saldo: {saldo:10.2f}")


