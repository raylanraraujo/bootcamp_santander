arquivo = open(
    "/Users/raylanaraujo/Documents/estudos/bootcamp_santander/7_manipulacao_arquivo/lorem.txt",
    "r"
    )
print(arquivo.read())
print(arquivo.readline())
print(arquivo.readlines())

arquivo.close()

#dica:
# while len(linha := arquivo.readline()):
#    print(linha)
