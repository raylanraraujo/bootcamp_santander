nome = "rAYlAn"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  olá mundo    !"
print(texto)
print(texto.strip() + ".") # remove os espaços em branco de ambos os lados da string
print(texto.rstrip() + ".") # remove os espaços em branco apenas do lado direito
print(texto.lstrip() + ".") # remove os espaços em branco apenas do lado esquerdo


menu = "Python"
print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))