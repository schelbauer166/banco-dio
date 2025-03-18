import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent
#print(ROOT_PATH)

#os.mkdir(ROOT_PATH/'teste')

#arquivo = open(ROOT_PATH / "teste.txt", 'w')
#arquivo.close()

#shutil.move(ROOT_PATH/'teste.txt', ROOT_PATH/'teste2.txt')

#os.remove(ROOT_PATH / "teste2.txt")

#shutil.move(ROOT_PATH / "teste.txt", ROOT_PATH / "teste" / "teste.txt" )


#try:
#    arquivo = open(ROOT_PATH / "teste", 'r' )
#except FileNotFoundError as exc:
#    print(f"Arquivo nao encontrado {exc}")
#except IsADirectoryError as exc:
#    print(f'Aqruivo nao encontrado: {exc}')