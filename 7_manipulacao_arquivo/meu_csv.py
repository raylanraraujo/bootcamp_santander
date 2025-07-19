import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# criando planilha e o escritor
try:
    with open(ROOT_PATH / "usuarios.csv", "w", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['id', 'nome'])
        escritor.writerow(['1', 'Maria'])
        escritor.writerow(['2', 'João'])
except IOError as exc:
    print(f'Erro ao criar o arquivo.\n{exc}')


# lendo o arquivo CSV criado
try:
    with open(ROOT_PATH / "usuarios.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)
except IOError as exc:
    print(f'Erro ao criar o arquivo.\n{exc}')