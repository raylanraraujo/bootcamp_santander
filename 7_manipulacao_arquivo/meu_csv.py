import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# criando planilha e o escritor
try:
    with open(ROOT_PATH / "usuarios.csv", "w", newline='', encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['id', 'nome'])
        escritor.writerow(['1', 'Maria'])
        escritor.writerow(['2', 'João'])
except IOError as exc:
    print(f'Erro ao criar o arquivo.\n{exc}')


# lendo o arquivo CSV criado
try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline='', encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha[0], linha[1])
except IOError as exc:
    print(f'Erro ao criar o arquivo.\n{exc}')

    
# outro modo de fazer a leitura e deixar o código mais legível
COLUNA_ID = 0
COLUNA_NOME = 1

try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline='', encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha[COLUNA_ID], linha[COLUNA_NOME])
except IOError as exc:
    print(f'Erro ao criar o arquivo.\n{exc}')

# usando o enumerate para pular cabecalhos
COLUNA_ID = 0
COLUNA_NOME = 1

try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline='', encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for idx, linha in enumerate(leitor):
            if idx == 0:
                continue
            print(f'ID: {linha[COLUNA_ID]}')
            print(f'Nome: {linha[COLUNA_NOME]}')
except IOError as exc:
    print(f'Erro ao criar o arquivo.\n{exc}')


# acessando como um dicionário
try:
    with open(ROOT_PATH / "usuarios.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"ID: {row["id"]}")
            print(f"Nome: {row["nome"]}")            
except IOError as exc:
    print(f"Erro ao criar o arquivo {exc}")

