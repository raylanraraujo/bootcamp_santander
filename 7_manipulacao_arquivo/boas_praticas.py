from pathlib import Path

ROOT_PATH = Path(__file__).parent

# abrindo um arquvi existente
arquivo = open(ROOT_PATH / 'lorem.txt', 'r')

#fechar aquivo manualmente
arquivo.close()

#automatizando o fechamento do arquivo após a sua abertura sem nenhum problema
with open(ROOT_PATH / 'lorem.txt', 'r') as arquivo:
    print('trabalhando com um arquivo')
print(arquivo.read())


#verificando se um arquivo foi aberto com sucesso
try:
    with open(ROOT_PATH / 'llorem.txt') as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f'\033[31mNão foi possível abrir o arquivo.\033[m\n{exc}')

#codificando na codificação correta
try:
    with open(ROOT_PATH / 'arquivo-utf-8.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write('Aprendendo a manipular arquivos com Python.')
except IOError as exc:
    print(f'{exc}')

# codificando na codificação errada
try:
    with open(ROOT_PATH / 'arquivo-utf-8.txt', 'r', encoding='ascii') as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f'{exc}')
except UnicodeDecodeError as exc:
    print(f'\033[31mErro de UnicoDecodeError\033[m\n{exc}')

    # Nesse exemplo não apresentou nenhum erro porque todos os caracteres utilizados dentro do arquivo são possíveis de serem interpretados no 'ascii', mas se eu pegar um caracter que não existem em ascii como um acento 