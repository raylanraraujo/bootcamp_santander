#criando dicionario
pessoa = { "nome": "Guilherme", "idade": 28}
eu = dict(nome = "Raylan", idade = 35)

#se não existe a chave que estamos atribuindo valor ela sera adicionada. Caso contrario, a chave pré-existente será apenas atualizada
pessoa["telefone"] = "3333-1234" 
print(pessoa)

#acessando valores
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["telefone"])

#alterando valores
pessoa["telefone"] = "9988-1781"

print(pessoa["telefone"])
print(pessoa["telefone"])

#Dicionarios aninhados
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}
print(contatos)

# Maneira 1: percorrendo pelas chaves
for chave in contatos:
    print(chave, contatos[chave])

# Maneira 2: percorrendo por chave e valor com items()
for chave, valor in contatos.items():
    print(chave, valor)