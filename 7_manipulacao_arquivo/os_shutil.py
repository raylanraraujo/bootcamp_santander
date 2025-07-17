import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# cria um novo diretório com o nome de novo-diretorio na pasta base do projeto
os.mkdir(ROOT_PATH / 'novo-diretorio')


#criando novo arquivo
arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

#renomeia arquivos
os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

#remove arquivo
os.remove(ROOT_PATH / "alterado.txt")

#cria arquivo 
arquivo = open(ROOT_PATH / "teste.txt", "w")

# movendo arquivos 
shutil.move(ROOT_PATH / "teste.txt", ROOT_PATH / "novo-diretorio" / "teste.txt")