arquivo = open(
    "/Users/raylanaraujo/Documents/estudos/bootcamp_santander/7_manipulacao_arquivo/lorem.txt",
    "r"
    )
print(arquivo.read())
print(arquivo.readline())
print(arquivo.readlines())

arquivo.close()

#Dica:
#Esse é o caminho mais rápido se você não quiser fazer um gerador e quiser explorar um arquivo grande da sua máquina

# while len(linha := arquivo.readline()):
#    print(linha)
