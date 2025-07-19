from pathlib import Path


# Erro de arquivo não encontrado
try:
    arquivo = open('meu_arquivo.py')
except FileNotFoundError as exc:
    print(f'\n\033[31mArquivo não encontrado.\033[m\n')
    print(exc)

# Erro de tantar abrir um diretório
ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / 'novo-diretorio')
except IsADirectoryError as exc:
    print(f'\n\033[31mHouve a tentativa de abrir um diretório em vez de um arquivo\033[m\n{exc}')
    